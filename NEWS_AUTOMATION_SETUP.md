# 🤖 AI Post-Prod Daily News Automation Setup

Deine personalisierte, automatisierte Daily News-Zusammenfassung für Video-Editing & AI-Post-Production – erstellt täglich um **06:30 CEST**.

## 🚀 Quick Start

### 1. GitHub Secrets konfigurieren

Gehe zu deinem Repository → **Settings → Secrets and variables → Actions** und füge diese Secrets hinzu:

#### `NOTION_API_KEY`
- Gehe zu [Notion Integrations](https://www.notion.com/my-integrations)
- Erstelle eine neue Integration: "AI Post-Prod News Generator"
- Kopiere den **Internal Integration Token**
- Format: `secret_xxxxxxxxxxxxxxxxxxxxx`

#### `ANTHROPIC_API_KEY`
- Gehe zu [Anthropic Console](https://console.anthropic.com/account/keys)
- Erstelle einen neuen API Key
- Format: `sk-ant-xxxxxxxxxxxxxxxxxxxxx`

### 2. Notion Database verbinden

Die Automation erstellt automatisch neue Seiten in dieser Datenbank:
- **Database ID**: `941d6c5a-b60d-44c1-a39e-8f947bfa0845`
- **URL**: [AI Post-Prod Daily News](https://www.notion.so/a9e2d82ca5f746caaf5cc85dec64466c)

Um die Integration zu aktivieren:
1. Öffne dein Notion Workspace
2. Gehe zur Integration "AI Post-Prod News Generator"
3. Unter "Connections" → Füge die "AI Post-Prod Daily News" Datenbank hinzu

### 3. Workflow aktivieren

Der GitHub-Actions-Workflow ist bereits konfiguriert:
- **Zeitplan**: Täglich um **06:30 CEST** (UTC: 04:30 winter, 05:30 sommer)
- **Datei**: `.github/workflows/daily-news-generator.yml`

Um zu testen:
```bash
# Manuell triggern
gh workflow run daily-news-generator.yml
```

## 📋 Was wird täglich erstellt?

Jede Ausgabe enthält:

### 1️⃣ **Top 3 News-Highlights**
- Kurze Updates zu deinen Top-Tools (Avid, DaVinci Resolve, Runway, ComfyUI)
- Mit Relevanz-Hinweis für deinen Workflow
- Direkter Link zur Quelle

### 2️⃣ **Tool-Updates & Tipps**
- Praktische Workflows & Code-Snippets
- Neue Features zum Testen
- Integration-Tipps (Claude Code + Remotion, etc.)

### 3️⃣ **Karriere & Trends**
- Freelance-Chancen für AI-Post-Production
- Skill-Positionierung (Hamburg/Remote)
- Automation als Differentiator

### 4️⃣ **Action für Heute**
- 1 personalisierter Next-Step (z.B. "Teste Runway Gen-4.5")
- Mit Zeitplan (Morgens/Mittags/Abends)
- Direkter Zugang zu Tools & Ressourcen

## 🔧 Customization

### News-Queries anpassen
In `scripts/daily_news_generator.py`:

```python
SEARCH_QUERIES = [
    "Deine Custom Search Query 1",
    "Deine Custom Search Query 2",
    # ...
]
```

### Prompt anpassen
Der `NEWS_STRUCTURE_PROMPT` in `daily_news_generator.py` steuert die Zusammenfassung. Editiere ihn für deine Prioritäten.

### Zeitplan ändern
In `.github/workflows/daily-news-generator.yml`:

```yaml
- cron: '30 4 * * *'  # 06:30 CEST → Ändere die Zeiten
```

[Cron Expression Generator](https://crontab.guru/)

## 📊 Notion Database Schema

Die Datenbank hat folgende Properties:

| Property | Typ | Funktion |
|----------|-----|---------|
| **Datum** | Title | Eindeutiges Datum + Überschrift |
| **Top Headlines** | Rich Text | 3 News-Highlights mit Links |
| **Tool Updates** | Rich Text | Praktische Tipps & Workflows |
| **Karriere & Trends** | Rich Text | Freelance-Chancen & Trends |
| **Action für Heute** | Rich Text | Dein personalisierter Next-Step |
| **Quellen** | Rich Text | Alle Links & Referenzen |
| **Kategorie** | Multi-Select | Avid, DaVinci, AI Tools, Automatisierung, Freelance |
| **Priorität** | Select | 🔴 High, 🟡 Medium, 🟢 Low |

## 🐛 Troubleshooting

### Notion-Fehler: "Integration not found"
- Gehe zu Notion → Integrations → "AI Post-Prod News Generator"
- Stelle sicher, dass die Datenbank unter "Connections" hinzugefügt ist

### API Key Errors
```
⚠️ "NOTION_API_KEY not set"
→ GitHub Secret nicht konfiguriert? Siehe Quick Start Punkt 1

⚠️ "ANTHROPIC_API_KEY not set"
→ Claude API Key nicht gesetzt? Siehe Quick Start Punkt 1
```

### Workflow läuft nicht um 06:30 CEST
- GitHub Actions nutzt UTC-Zeit
- 06:30 CEST = 04:30 UTC (Winter) oder 05:30 UTC (Sommer)
- Aktuell: `cron: '30 4 * * *'` für Winterzeit
- Ändere zu `'30 5 * * *'` für Sommerzeit

### Manueller Test
```bash
# Repository clonen
git clone https://github.com/hyraniemus/hamburg-techno.git
cd hamburg-techno

# Python deps installieren
pip install -r requirements.txt  # oder: pip install anthropic requests

# Manuell ausführen
export NOTION_API_KEY="secret_xxxxx"
export ANTHROPIC_API_KEY="sk-ant-xxxxx"
export NOTION_DATABASE_ID="941d6c5a-b60d-44c1-a39e-8f947bfa0845"
python scripts/daily_news_generator.py
```

## 📈 Nächste Schritte

- [ ] GitHub Secrets konfigurieren (NOTION_API_KEY, ANTHROPIC_API_KEY)
- [ ] Notion Integration verbinden
- [ ] Workflow manuell testen: `gh workflow run daily-news-generator.yml`
- [ ] Erste automatische Ausgabe um 06:30 CEST warten
- [ ] Notion Database öffnen und News überprüfen
- [ ] ggf. Prompt/Queries anpassen basierend auf Output

## 📞 Support

- GitHub Actions Logs: Settings → Actions → Daily AI Post-Prod News Generator
- Notion API Docs: [notion.com/developers](https://developers.notion.com/)
- Anthropic API Docs: [console.anthropic.com](https://console.anthropic.com/docs)

---

**Status**: ✅ Automation ist ready to go!

Deine erste automatische Daily News wird morgen um 06:30 CEST erstellt.
