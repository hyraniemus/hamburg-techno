import Anthropic from "@anthropic-ai/sdk";
import * as fs from "fs";
import * as path from "path";
import cron from "node-cron";
import nodemailer from "nodemailer";
import { Client } from "@notionhq/client";

// Load environment variables
require("dotenv").config();

interface NewsDigest {
  date: string;
  highlights: string[];
  toolUpdates: string[];
  careerTrends: string[];
  actionItem: string;
}

const client = new Anthropic();

async function fetchAINewsDigest(): Promise<NewsDigest> {
  const today = new Date().toLocaleDateString("de-DE", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  const prompt = `Du bist ein Spezialist für AI-gestützte Video-Produktion und Post-Production.
Erstelle eine tägliche News-Zusammenfassung für einen Video-Editor/Post-Production-Spezialist aus Hamburg, der zu AI-Produktion wechselt.

FOKUSGEBIETE:
- Avid Media Composer, DaVinci Resolve, Remotion
- ComfyUI, Runway Gen-4, Claude Code-Integration
- AI-Video-Generierung, Post-Production-Automatisierung
- Freelance-Chancen in AI-Editing
- Musikproduktion mit Suno
- Film/TV-News, Dokumentar-Produktion

STRUKTUR (max. 400 Wörter, auf Deutsch):

1. **Top 3 News-Highlights** (3 Bullet-Points):
   - Format: "Headline - [Kurze Beschreibung] (Quelle/Link, Relevanz für Workflow)"

2. **Tool-Updates & Tipps** (2-3 praktische Insights):
   - Konkrete Tipps zum Implementieren (z.B. Skripte, Integrationen)

3. **Karriere/Trends** (1-2 Chancen):
   - Freelance-Möglichkeiten, Startups, Trends

4. **Aktion für heute** (1 personalisierter Next-Step):
   - Konkrete Aufgabe zum Testen/Ausprobieren

Datum: ${today}

Recherchiere aktuelle Nachrichten (letzte 24h) von:
- Reddit (r/Avid, r/davinciresolve, r/MachineLearning, r/VideoEditing)
- Hacker News
- Tool-Blogs (Blackmagic Design, Anthropic, Runway)
- X/Twitter Hashtags (#AIVideo #PostProduction #DaVinciResolve)

Ignorierer Politik/Wirtschaft, außer wenn relevant für Tech/Film.
Sei konkret, handlungsorientiert, gib Links/Quellen an wo möglich.`;

  const response = await client.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 2048,
    messages: [
      {
        role: "user",
        content: prompt,
      },
    ],
  });

  // Parse response
  const content =
    response.content[0].type === "text" ? response.content[0].text : "";

  // Extract sections (simplified parsing)
  const sections = {
    date: today,
    highlights: extractSection(content, "Top 3 News-Highlights"),
    toolUpdates: extractSection(content, "Tool-Updates & Tipps"),
    careerTrends: extractSection(content, "Karriere/Trends"),
    actionItem: extractSection(content, "Aktion für heute")[0] || "...",
  };

  return sections as NewsDigest;
}

function extractSection(text: string, sectionTitle: string): string[] {
  const regex = new RegExp(
    `\\*\\*${sectionTitle}\\*\\*[\\s\\S]*?(?=\\*\\*|$)`,
    "i"
  );
  const match = text.match(regex);

  if (!match) return [];

  const lines = match[0]
    .split("\n")
    .filter((line) => line.trim().startsWith("-"))
    .map((line) => line.trim().substring(1).trim());

  return lines;
}

async function sendEmailDigest(digest: NewsDigest): Promise<void> {
  if (
    !process.env.SMTP_USER ||
    !process.env.SMTP_PASS ||
    !process.env.EMAIL_TO
  ) {
    console.log(
      "Email-Konfiguration nicht gesetzt. Speichern stattdessen in Notion..."
    );
    return;
  }

  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST || "smtp.gmail.com",
    port: parseInt(process.env.SMTP_PORT || "587"),
    secure: false,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS,
    },
  });

  const htmlContent = `
    <h2>Deine AI-Post-Prod News – ${digest.date}</h2>

    <h3>📰 Top 3 News-Highlights</h3>
    <ul>${digest.highlights.map((h) => `<li>${h}</li>`).join("")}</ul>

    <h3>🛠️ Tool-Updates & Tipps</h3>
    <ul>${digest.toolUpdates.map((t) => `<li>${t}</li>`).join("")}</ul>

    <h3>💼 Karriere/Trends</h3>
    <ul>${digest.careerTrends.map((c) => `<li>${c}</li>`).join("")}</ul>

    <h3>✅ Aktion für heute</h3>
    <p>${digest.actionItem}</p>

    <p><small>Automatisch generiert von deinem AI-Post-Production News Digest System</small></p>
  `;

  await transporter.sendMail({
    from: process.env.SMTP_USER,
    to: process.env.EMAIL_TO,
    subject: `Deine AI-Post-Prod News – ${digest.date}`,
    html: htmlContent,
  });

  console.log(`✅ Email versendet an ${process.env.EMAIL_TO}`);
}

async function saveToNotion(digest: NewsDigest): Promise<void> {
  if (!process.env.NOTION_API_KEY || !process.env.NOTION_DATABASE_ID) {
    console.log("Notion-Konfiguration nicht gesetzt. Nur lokale Speicherung.");
    return;
  }

  const notion = new Client({ auth: process.env.NOTION_API_KEY });

  await notion.pages.create({
    parent: { database_id: process.env.NOTION_DATABASE_ID },
    properties: {
      Titel: { title: [{ text: { content: `News – ${digest.date}` } }] },
      Datum: {
        date: {
          start: new Date().toISOString().split("T")[0],
        },
      },
    },
    children: [
      {
        object: "block",
        type: "heading_2",
        heading_2: {
          rich_text: [{ text: { content: "Top 3 News-Highlights" } }],
        },
      },
      ...digest.highlights.map((h) => ({
        object: "block",
        type: "bulleted_list_item",
        bulleted_list_item: {
          rich_text: [{ text: { content: h } }],
        },
      })),
    ],
  });

  console.log("✅ Notion-Seite erstellt");
}

async function saveLocally(digest: NewsDigest): Promise<void> {
  const fileName = `news-digest-${new Date().toISOString().split("T")[0]}.json`;
  const filePath = path.join(process.cwd(), "news-digests", fileName);

  // Create directory if it doesn't exist
  const dirPath = path.dirname(filePath);
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }

  fs.writeFileSync(filePath, JSON.stringify(digest, null, 2));
  console.log(`✅ Lokal gespeichert: ${filePath}`);
}

async function generateDigest(): Promise<void> {
  console.log(`\n🔄 Generiere News-Digest für ${new Date().toLocaleString("de-DE")}...`);

  try {
    const digest = await fetchAINewsDigest();

    // Try multiple delivery methods
    await saveLocally(digest);

    // Parallel: Email + Notion
    await Promise.allSettled([
      sendEmailDigest(digest),
      saveToNotion(digest),
    ]);

    console.log("✅ News-Digest erfolgreich generiert!");
  } catch (error) {
    console.error("❌ Fehler beim Generieren des Digests:", error);
  }
}

// Schedule daily execution
function startScheduler(): void {
  const scheduleTime = process.env.SCHEDULE_TIME || "06:30";
  const [hours, minutes] = scheduleTime.split(":").map(Number);

  // Cron format: Minute Hour Day-of-Month Month Day-of-Week
  const cronExpression = `${minutes} ${hours} * * *`;

  console.log(`📅 Scheduler gestartet. Tägliche Ausführung um ${scheduleTime} CEST`);
  console.log(`   (Cron: ${cronExpression})`);

  cron.schedule(cronExpression, generateDigest, {
    timezone: process.env.TIMEZONE || "Europe/Berlin",
  });

  // Run immediately if in development
  if (process.env.NODE_ENV !== "production") {
    console.log("🚀 Entwicklungsmodus: Generiere sofort einen Digest...");
    generateDigest();
  }
}

// Main entry point
if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.includes("--now")) {
    // Generate immediately without scheduling
    generateDigest();
  } else if (args.includes("--schedule")) {
    // Start the scheduler
    startScheduler();
  } else {
    console.log("Verwendung:");
    console.log("  npm run digest -- --now       (jetzt generieren)");
    console.log("  npm run digest -- --schedule  (täglich planen)");
  }
}

export { generateDigest, startScheduler };
