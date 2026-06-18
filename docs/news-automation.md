# 📰 Daily AI Post-Prod News Automation

Automatisierte tägliche News-Zusammenfassung für deine Karriere als AI-Post-Production Spezialist.

## 🎯 Übersicht

Diese Automation läuft **täglich um 06:30 CEST** und sammelt aktuelle News zu:
- Avid Media Composer (Updates, Bug Fixes, neue Tools)
- DaVinci Resolve (AI-Features, Color Grading)
- Runway Gen-4 (Video-Generierung, Character Consistency)
- ComfyUI (Modelle, Video-Generation)
- Claude Code (Integration in Workflows)
- Remotion (Animation Framework)
- Suno AI (Musikproduktion)
- Post-Production-Automatisierung & Freelance-Chancen

## ⚙️ Setup & Konfiguration

### 1. GitHub Actions Workflow
```
.github/workflows/daily-news.yml
```

Der Workflow läuft auf dem `ubuntu-latest` Runner und wird täglich um 06:30 CEST getriggert.

### 2. Python-Skript
```
scripts/generate_news_summary.py
```

Generiert die strukturierte News-Zusammenfassung im Markdown-Format.

### 3. Output-Speicherort
```
docs/news-summaries/news-YYYY-MM-DD.md
docs/news-summaries/news-YYYY-MM-DD.json
```

## 🚀 Features

### Aktuelle Version (Auto-Template)
- ✅ GitHub Actions Workflow (täglich 06:30 CEST)
- ✅ Python-Generierung
- ✅ Markdown + JSON Output
- ✅ Automatischer Git Commit

### Nächste Schritte (Erweiterte Integration)

#### Option 1: Notion Integration
```python
# In generate_news_summary.py hinzufügen:
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])
# Schreibe News in Notion-Datenbank
```

Notwendige GitHub Secrets:
- `NOTION_TOKEN`: Dein Notion Integration Token
- `NOTION_DATABASE_ID`: ID deiner News-Datenbank

#### Option 2: Email-Versand
```python
# Nutze SendGrid oder Mailgun für tägliche E-Mail-Updates
import sendgrid
```

Notwendige GitHub Secrets:
- `SENDGRID_API_KEY`

#### Option 3: Claude API Integration (Real-time Recherche)
```python
# Nutze Claude mit WebSearch für Live-News-Analyse
from anthropic import Anthropic

client = Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=2000,
    messages=[{
        "role": "user",
        "content": "Fasse die neuesten AI-Post-Production News zusammen..."
    }]
)
```

Notwendige GitHub Secrets:
- `ANTHROPIC_API_KEY`

## 📋 Konfiguration

### Workflow Timing anpassen
In `.github/workflows/daily-news.yml`:
```yaml
- cron: '30 5 * * *'  # UTC (adjusts for CEST automatically)
```

**Zeitzone-Konvertierung:**
- 06:30 CEST (Sommer) = 04:30 UTC
- 06:30 CET (Winter) = 05:30 UTC

### Interessen-Filter ändern
In `scripts/generate_news_summary.py`:
```python
INTERESTS = {
    "avid": "...",
    "davinci": "...",
    # Füge weitere hinzu...
}
```

## 🔐 GitHub Secrets Setup

Füge folgende Secrets zu deinem Repository hinzu:
- `NOTION_TOKEN`: Optional (für Notion-Integration)
- `SENDGRID_API_KEY`: Optional (für E-Mail-Versand)
- `ANTHROPIC_API_KEY`: Optional (für Claude API Integration)

Gehe zu: **Repository Settings → Secrets and variables → Actions**

## 📊 Monitoring

### Workflow-Status prüfen
```
GitHub → Actions → Daily AI Post-Prod News Summary
```

### Logs anschauen
```
GitHub → Actions → [Letzter Run] → Logs
```

## 🛠️ Troubleshooting

### Workflow läuft nicht
- Prüfe: Repository Settings → Actions → "Allow all actions and reusable workflows"
- Prüfe: Workflow ist nicht disabled (✅ enabled)

### Keine Output-Dateien
- Prüfe Python-Fehler in den Workflow-Logs
- Verifiziere, dass `docs/news-summaries/` Verzeichnis existiert

### Git Push schlägt fehl
- Prüfe: `GITHUB_TOKEN` hat Push-Permissions
- Prüfe: Branch-Protection-Rules

## 📝 Beispiel-Output

```markdown
# 📰 Deine AI-Post-Prod News – 18. Juni 2026

## Top 3 News-Highlights

1. **DaVinci Resolve 21 mit AI-Power gelauncht** 🎨
   - Object Mask AI, IntelliSearch, CineFocus
   - [Link zur Quelle]

2. **Runway Gen-4 mit Charakter-Konsistenz** 🎬
   - Camera Control, Native Audio
   - [Link zur Quelle]

3. **Suno v5.5: Custom Voice Cloning** 🎵
   - Voices, Custom Models, Studio Features
   - [Link zur Quelle]

...
```

## 🤖 Future Enhancements

- [ ] OpenAI GPT-4 für erweiterte News-Analyse
- [ ] Slack/Discord Integration für sofortige Benachrichtigungen
- [ ] RSS-Feed Integration (r/Avid, r/davinciresolve, etc.)
- [ ] Personalisierte Scoring (relevance ranking)
- [ ] Notion Database mit Tagging & Kategorisierung
- [ ] Mönatliche Trend-Reports

## 📧 Support

Für Fragen oder Erweiterungen:
- Bearbeite `.github/workflows/daily-news.yml` für Timing
- Bearbeite `scripts/generate_news_summary.py` für Content-Logik
- Füge neue Tools/Quellen im `INTERESTS` Dict hinzu

---

**Workflow-Status:** ✅ Active  
**Last Updated:** 2026-06-18  
**Timezone:** CEST (UTC+2)
