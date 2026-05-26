# 🎬 Deine AI-Post-Prod Daily News Setup

Automatisierte tägliche News-Zusammenfassung für deinen Video-Editing & AI-Production Workflow.

---

## 📋 Features

✅ **Automatisch täglich um 06:30 CEST** (via GitHub Actions Cron)  
✅ **Personalisiert für:** Avid, DaVinci Resolve, ComfyUI, Runway, Claude Code, Suno  
✅ **Gespeichert in Notion** als tägliche Seite  
✅ **Zusammengefasst mit Claude AI** (400 Wörter max)  
✅ **Relevante Quellen:** Blackmagic, Avid, Hacker News, ProductHunt  
✅ **Strukturiert:** Top 3 News | Tool-Updates | Karriere/Trends | Action für heute  

---

## 🔧 Einrichtung (5 Min)

### 1️⃣ **Anthropic API Key** (für Claude)

- Gehe zu [console.anthropic.com](https://console.anthropic.com)
- Erstelle einen neuen API Key
- Kopiere den Schlüssel

### 2️⃣ **Notion Integration**

#### A) Notion Integration erstellen:
- Öffne [notion.com/my-integrations](https://notion.com/my-integrations)
- Klick "Create new integration"
- Name: "Hamburg Techno News Bot"
- Klick "Submit"
- **Internal Integration Secret kopieren** (wird `NOTION_API_KEY`)

#### B) Notion Database erstellen:
- Öffne Notion und erstelle eine neue **Inline Database**
- Nenne sie z.B. "AI Post-Prod Daily News"
- Eigenschaften:
  - **Title** (Standard)
  - **Date** (Datum) - für automatische Tagesdatum
  
#### C) Notion Integration mit Database verbinden:
- Database öffnen
- Klick **...** (oben rechts) → **Connections**
- Suche nach deiner Integration ("Hamburg Techno News Bot")
- Verbinde sie

#### D) Database ID kopieren:
- In der URL: `https://notion.so/f336d0bc-b841-465b-8045-024475c079dd?v=123`
- Die lange UUID vor `?v=` ist deine `NOTION_DATABASE_ID`

### 3️⃣ **GitHub Secrets einrichten**

Gehe zu deinem Repo:
- **Settings** → **Secrets and variables** → **Actions**
- Erstelle diese 3 Secrets:

| Name | Wert |
|------|------|
| `ANTHROPIC_API_KEY` | Dein Claude API Key |
| `NOTION_API_KEY` | Dein Notion Internal Integration Secret |
| `NOTION_DATABASE_ID` | Deine Notion Database ID |

---

## 🚀 Lokal Testen

```bash
# 1. Dependencies installieren
npm install

# 2. .env datei erstellen und Keys eintragen
cp .env.example .env

# 3. Lokal testen
npm run news:generate
```

**Erwartete Ausgabe:**
```
📰 Sammle News aus RSS-Feeds...
✓ Blackmagic (DaVinci Resolve): 3 relevante Artikel
✓ Hacker News: 5 relevante Artikel
...
🤖 Generiere Zusammenfassung mit Claude...
💾 Speichere in Notion...
✓ Notion-Seite erstellt: "Deine AI-Post-Prod News – 2026-05-26"
✅ News-Digest erfolgreich erstellt!
```

---

## ⏰ Automatische Ausführung

Die GitHub Action **läuft automatisch täglich um 06:30 CEST**.

### Manuell Triggern (für Tests):
- Gehe zu: **Repo** → **Actions** → **Daily AI Post-Prod News Digest**
- Klick **Run workflow** → **Run workflow**

### Logs ansehen:
- **Actions** → **Daily AI Post-Prod News Digest** → Aktueller Lauf → **Generate Daily News Summary**

---

## 🎯 Anpassen

### Neue Quellen hinzufügen
Bearbeite `scripts/daily-news.js`:

```javascript
const NEWS_SOURCES = [
  { name: 'Mein Blog', url: 'https://example.com/feed' },
  // ... weitere
];
```

### Neue Keywords
Bearbeite die `KEYWORDS` Liste in `scripts/daily-news.js`:

```javascript
const KEYWORDS = [
  'Avid', 'DaVinci Resolve', 'MeinNewsTool', // ...
];
```

### Datum/Zeit der Ausführung
Bearbeite `.github/workflows/daily-news.yml`:

```yaml
- cron: '30 4 * * *'  # 06:30 CEST = 04:30 UTC
```

**Cron-Format:** `<Minute> <Stunde> <Tag> <Monat> <Wochentag>`

---

## 📧 Optional: Email-Versand

Falls du lieber eine E-Mail bekommen möchtest, statt in Notion:

### Mit SendGrid (kostenlos bis 100/Tag):
1. Melde dich bei [sendgrid.com](https://sendgrid.com) an
2. Erstelle einen API Key
3. Addiere zu GitHub Secrets: `SENDGRID_API_KEY`
4. Ändere `scripts/daily-news.js`:

```javascript
// Nach saveToNotion() ersetzen:
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

const msg = {
  to: 'mmittelbach@gmail.com',
  from: 'news@hamburg-techno.local',
  subject: `Deine AI-Post-Prod News – ${today}`,
  text: summary,
};

await sgMail.send(msg);
```

---

## ⚡ Troubleshooting

| Problem | Lösung |
|---------|--------|
| "Notion API Error: Not found" | Notion DB ID falsch oder Integration nicht verbunden |
| "Anthropic API Error" | API Key ungültig oder GitHub Secret falsch gesetzt |
| Workflow läuft nicht | Prüfe: **Actions** → **Enable** workflows müssen aktiviert sein |
| Keine relevanten Artikel | Keywords in `scripts/daily-news.js` anpassen |

---

## 📚 Links

- [Anthropic API Docs](https://docs.anthropic.com)
- [Notion API Docs](https://developers.notion.com)
- [GitHub Actions Cron Syntax](https://crontab.guru)
- [RSS Parser Package](https://www.npmjs.com/package/rss-parser)

---

**Viel Erfolg mit deinem personalisierten News-Digest!** 🎬🤖
