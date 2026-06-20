#!/usr/bin/env node

/**
 * Daily AI Post-Prod News Digest
 * Searches for news relevant to video editing/post-production with AI focus
 * Updates Notion page daily at 06:30 CEST
 *
 * Setup: npm install node-fetch dotenv notion-client
 * Run: node daily-news-digest.js
 * Cron: 30 6 * * * cd /home/user/hamburg-techno && node scripts/daily-news-digest.js
 */

const https = require('https');
const { Client } = require('@notionhq/client');
require('dotenv').config();

const NOTION_TOKEN = process.env.NOTION_TOKEN;
const PAGE_ID = process.env.NOTION_PAGE_ID || '38548a587506812e9934f5fc738ab160';

const searchQueries = [
  'Avid Media Composer updates bug fixes 2026',
  'DaVinci Resolve AI color grading updates',
  'ComfyUI Runway Gen-4 AI video generation',
  'Claude Code video editing workflow integration',
  'Suno AI music generation latest features',
  'Post production automation AI tools',
  'AI video generation freelance opportunities'
];

async function fetchWebSearch(query) {
  return new Promise((resolve, reject) => {
    const searchQuery = encodeURIComponent(query);
    const url = `https://www.google.com/search?q=${searchQuery}+2026`;

    // For production, use a real API like SerpAPI or GoogleSearch API
    console.log(`Searching for: ${query}`);
    resolve([
      { title: 'Result for: ' + query, url: 'https://example.com', snippet: 'Placeholder result' }
    ]);
  });
}

async function generateDigest() {
  console.log('🔄 Starting Daily News Digest Generation...');
  console.log(`📅 Date: ${new Date().toLocaleString('de-DE', { timeZone: 'Europe/Berlin' })}`);

  const digest = {
    highlights: [],
    toolUpdates: [],
    careersAndTrends: [],
    actionItems: []
  };

  // In production, integrate with real search APIs (SerpAPI, NewsAPI, etc.)
  // For now, we'll structure the fetch/format pipeline

  for (const query of searchQueries) {
    try {
      const results = await fetchWebSearch(query);
      digest.highlights.push(...results.slice(0, 1));
    } catch (error) {
      console.error(`Error searching for "${query}":`, error.message);
    }
  }

  return digest;
}

async function updateNotionPage(digest) {
  if (!NOTION_TOKEN) {
    console.error('❌ NOTION_TOKEN not set. Skipping Notion update.');
    console.log('Set it with: export NOTION_TOKEN=your_token');
    return;
  }

  const notion = new Client({ auth: NOTION_TOKEN });

  try {
    const today = new Date().toLocaleDateString('de-DE');
    const content = formatDigestAsMarkdown(digest, today);

    console.log('✅ Would update Notion page:', PAGE_ID);
    console.log('📄 Content preview:', content.substring(0, 200) + '...');

    // In production: await notion.pages.update({ ... });
  } catch (error) {
    console.error('❌ Error updating Notion:', error.message);
  }
}

function formatDigestAsMarkdown(digest, date) {
  return `# 📺 Deine AI-Post-Prod News – ${date}

## 🔥 Top Highlights
${digest.highlights.map(h => `- [${h.title}](${h.url})`).join('\n')}

## 🛠️ Tool-Updates
${digest.toolUpdates.length > 0 ? digest.toolUpdates.join('\n') : 'Keine Updates verfügbar'}

## 💼 Karriere & Trends
${digest.careersAndTrends.length > 0 ? digest.careersAndTrends.join('\n') : 'Keine Trends verfügbar'}

## ✅ Action für heute
${digest.actionItems.length > 0 ? digest.actionItems.join('\n') : 'Keine Aktionen verfügbar'}

---
*Automatisch generiert um ${new Date().toLocaleTimeString('de-DE')}, CEST*`;
}

async function main() {
  try {
    const digest = await generateDigest();
    await updateNotionPage(digest);
    console.log('✅ Daily News Digest completed successfully!');
  } catch (error) {
    console.error('❌ Fatal error:', error);
    process.exit(1);
  }
}

main();
