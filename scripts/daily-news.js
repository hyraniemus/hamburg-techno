#!/usr/bin/env node

require('dotenv').config();
const Anthropic = require('@anthropic-ai/sdk');
const { Client } = require('@notionhq/client');
const axios = require('axios');
const Parser = require('rss-parser');

const parser = new Parser();
const client = new Anthropic();
const notion = new (require('@notionhq/client').Client)({ auth: process.env.NOTION_API_KEY });

// RSS/API Quellen für Tech-News
const NEWS_SOURCES = [
  { name: 'Blackmagic (DaVinci Resolve)', url: 'https://www.blackmagicdesign.com/feed' },
  { name: 'Avid Knowledge Base', url: 'https://avid.secure.force.com/pkb/feeds/2' },
  { name: 'Hacker News', url: 'https://news.ycombinator.com/rss' },
  { name: 'ProductHunt', url: 'https://www.producthunt.com/feed' },
];

// Suchbegriffe für Filterung
const KEYWORDS = [
  'Avid', 'Media Composer', 'DaVinci Resolve', 'Remotion', 'ComfyUI', 'Runway',
  'Claude', 'AI video', 'Post-Production', 'Color Grading', 'Video editing',
  'Suno', 'Music generation', 'Automation', 'Workflow', 'Documentary',
  'AI-gestützt', 'Freelance', 'Hamburg', 'Cape Town'
];

async function fetchNews() {
  console.log('📰 Sammle News aus RSS-Feeds...');
  let allArticles = [];

  for (const source of NEWS_SOURCES) {
    try {
      const feed = await parser.parseURL(source.url);
      const filtered = (feed.items || [])
        .filter(item => {
          const text = `${item.title || ''} ${item.contentSnippet || ''}`.toLowerCase();
          return KEYWORDS.some(kw => text.includes(kw.toLowerCase()));
        })
        .slice(0, 5)
        .map(item => ({
          title: item.title || 'Untitled',
          link: item.link || '',
          description: item.contentSnippet || item.content || '',
          source: source.name,
          pubDate: item.pubDate || new Date().toISOString(),
        }));

      allArticles = [...allArticles, ...filtered];
      console.log(`✓ ${source.name}: ${filtered.length} relevante Artikel`);
    } catch (err) {
      console.warn(`✗ Fehler bei ${source.name}:`, err.message);
    }
  }

  // Sortiere nach Datum (neueste zuerst)
  allArticles.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));

  console.log(`\n📊 Insgesamt ${allArticles.length} Artikel gefunden\n`);
  return allArticles.slice(0, 20); // Top 20
}

async function generateSummary(articles) {
  console.log('🤖 Generiere Zusammenfassung mit Claude...');

  const articlesText = articles
    .map((a, i) => `${i + 1}. "${a.title}" (${a.source})\n   ${a.description.substring(0, 200)}...\n   Link: ${a.link}`)
    .join('\n\n');

  const prompt = `Du bist ein spezialisierter News-Digest-Ersteller für einen Video-Editor und Post-Production-Spezialisten aus Hamburg, der zu AI-gestützter Video-Produktion wechselt.

Erstelle eine tägliche Zusammenfassung (max. 400 Wörter, auf Deutsch, klar und handlungsorientiert) mit dieser Struktur:

1. **Top 3 News-Highlights**: Bullet-Points mit Link und Relevanz für Video-Editing-Workflows
2. **Tool-Updates & Tipps**: 2-3 praktische Insights für sofortige Anwendung
3. **Karriere/Trends**: 1-2 Chancen für AI-Post-Production-Freelancer
4. **Aktion für heute**: 1 personalisierter Next-Step

Fokus: Avid, DaVinci Resolve, ComfyUI, Runway, Claude Code, Suno, AI-Video, Post-Production-Automation.

ARTIKEL:
${articlesText}

Antworte mit der strukturierten Zusammenfassung. Nutze ggf. Markdown-Formatierung.`;

  try {
    const response = await client.messages.create({
      model: 'claude-opus-4-7',
      max_tokens: 1024,
      messages: [{ role: 'user', content: prompt }],
    });

    return response.content[0].type === 'text' ? response.content[0].text : '';
  } catch (err) {
    console.error('Fehler bei Claude API:', err.message);
    return 'Fehler bei der Zusammenfassung-Generierung.';
  }
}

async function saveToNotion(summary) {
  if (!process.env.NOTION_DATABASE_ID) {
    console.warn('⚠️  NOTION_DATABASE_ID nicht gesetzt. Überspringe Notion-Speicherung.');
    console.log('\n📰 GENERIERTE ZUSAMMENFASSUNG:\n');
    console.log(summary);
    return;
  }

  console.log('💾 Speichere in Notion...');

  try {
    const today = new Date().toISOString().split('T')[0];

    await notion.pages.create({
      parent: { database_id: process.env.NOTION_DATABASE_ID },
      properties: {
        Title: {
          title: [{ text: { content: `Deine AI-Post-Prod News – ${today}` } }],
        },
        Date: {
          date: { start: today },
        },
      },
      children: [
        {
          object: 'block',
          type: 'paragraph',
          paragraph: {
            rich_text: [{ text: { content: summary } }],
          },
        },
      ],
    });

    console.log(`✓ Notion-Seite erstellt: "Deine AI-Post-Prod News – ${today}"`);
  } catch (err) {
    console.error('Fehler bei Notion-Speicherung:', err.message);
    console.log('\n📰 GENERIERTE ZUSAMMENFASSUNG:\n');
    console.log(summary);
  }
}

async function main() {
  try {
    console.log('🚀 Starte tägliches News-Digest...\n');

    const articles = await fetchNews();

    if (articles.length === 0) {
      console.log('⚠️  Keine relevanten Artikel gefunden.');
      return;
    }

    const summary = await generateSummary(articles);
    await saveToNotion(summary);

    console.log('\n✅ News-Digest erfolgreich erstellt!');
  } catch (err) {
    console.error('❌ Fehler in main():', err);
    process.exit(1);
  }
}

main();
