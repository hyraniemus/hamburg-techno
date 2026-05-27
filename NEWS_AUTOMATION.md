# 📰 Tägliche AI-Post-Prod News – Automatisierung

**Automatische Zusammenfassung** für Video-Editors, Post-Production-Spezialisten und AI-Content-Creators

## 🎯 Was du bekommst

Jeden Tag um **06:30 CEST** eine personalisierte News-Zusammenfassung:

- ✨ **Top 3 News-Highlights** (Avid, DaVinci Resolve, Remotion, ComfyUI, Runway, Claude, Suno)
- 🛠️ **Tool-Updates & Praktische Tipps** (Batch-Skripte, Workflows, Integration)
- 💼 **Freelance-Chancen & Trends** (Jobs, Community-News, Industrie-Bewegungen)
- 🎬 **Personalisierte Action-Items** (Was du heute testen solltest)

## 🚀 Quick Start (5 Minuten)

### Option 1: Notion-Integration (Empfohlen)

```bash
# 1. Setup-Skript ausführen
bash scripts/setup_notion.sh

# 2. GitHub Secrets konfigurieren (siehe Prompt)
# NOTION_TOKEN: dein Notion Integration Token
# NOTION_DATABASE_ID: deine News-Datenbank ID

# 3. Test
python scripts/daily_news_summary.py
```

**Vorteil**: News landen direkt in deiner Notion-Datenbank, sortierbar, durchsuchbar

### Option 2: Lokale Markdown-Dateien

```bash
# Automatisch speichert das Skript in:
python scripts/daily_news_summary.py
# → /hamburg-techno/news_summaries/news_2026-05-27.md
```

**Vorteil**: Kein Notion-Token nötig, Git-trackbar

## 🔧 Konfiguration

### GitHub Actions aktivieren

Die tägliche Ausführung läuft automatisch durch:
- **Cron-Job**: `30 4 * * *` (04:30 UTC = 06:30 CEST)
- **Timezone**: Europe/Berlin (Sommerzeit wird berücksichtigt)
- **Auslöser**: Täglich + manuell mit `workflow_dispatch`

**Manuell triggern:**
```bash
# Via GitHub CLI (wenn gh installiert)
gh workflow run daily-news.yml

# Oder: GitHub UI → Actions → Daily News → "Run workflow"
```

### Umgebungsvariablen

```bash
# .env.local (nicht committen!)
NOTION_TOKEN=secret_xxxxx
NOTION_DATABASE_ID=xxxxx
```

## 📊 News-Quellen

Das Skript durchsucht diese Quellen **täglich**:

| Quelle | Fokus | Timing |
|--------|-------|--------|
| **Blackmagic Design Blog** | DaVinci Resolve Updates | Täglich |
| **Avid Knowledge Base** | Media Composer Fixes | Täglich |
| **ComfyUI Docs** | Video-Generierung | Täglich |
| **Runway Research** | Gen-4 Updates | Täglich |
| **Remotion Blog** | React Video Framework | Täglich |
| **Suno Docs** | AI Music Generation | Täglich |
| **Reddit** (r/Avid, r/davinciresolve) | Community-News | Täglich |
| **Hacker News** | Tech-Trends | Täglich |
| **Twitter/X** (#AIVideo, #PostProduction) | Breaking News | Täglich |

## 💡 Use Cases

### 1. **Täglich 10 Minuten News-Briefing**
Öffne deine Notion-Datenbank oder lies `news_YYYY-MM-DD.md` mit Kaffee

### 2. **Portfolio-Inspiration**
→ "Teste ComfyUI WAN 2.6" → Neuer Portfolio-Clip

### 3. **Freelance-Job-Alerts**
→ "Hambi Media sucht AI Videographer" → Bewerbung

### 4. **Workflow-Optimierung**
→ "Claude Code + Remotion" → Automatisiere deine Social-Media-Produktion

## 🔐 Sicherheit

- ✅ Token werden nur in GitHub Secrets gespeichert (nicht in Git)
- ✅ `.env.local` ist in `.gitignore`
- ✅ Keine hardcoded Credentials
- ✅ Read-only Zugriff auf Notion (nur Page Creation)

## 📁 Struktur

```
hamburg-techno/
├── scripts/
│   ├── daily_news_summary.py    # Hauptscript
│   └── setup_notion.sh          # Setup-Anleitung
├── .github/workflows/
│   └── daily-news.yml           # GitHub Actions
├── news_summaries/              # Lokal gespeicherte News
│   ├── news_2026-05-27.md
│   ├── news_2026-05-28.md
│   └── ...
└── NEWS_AUTOMATION.md           # Diese Datei
```

## 🛠️ Erweiterte Konfiguration

### Custom News-Kategorien hinzufügen

In `daily_news_summary.py`:

```python
NEWS_SOURCES = {
    "deine_kategorie": [
        "Suchbegriff 1",
        "Suchbegriff 2"
    ]
}
```

### E-Mail-Integration (optional)

```python
def send_email_summary(summary: str, email: str):
    # SMTP-Integration
    pass
```

### Discord/Slack Notifications

Bereits konfiguriert in `.github/workflows/daily-news.yml`:

```yaml
- name: 📧 Discord Notification
  uses: 8398a7/action-slack@v3
  with:
    webhook_url: ${{ secrets.DISCORD_WEBHOOK }}
```

## 🐛 Troubleshooting

### "NOTION_TOKEN nicht gesetzt"
→ Prüfe GitHub Secrets unter Settings → Secrets

### "Database ID nicht korrekt"
→ Database ID: Notion-URL nach `?p=` kopieren
→ Beispiel: `https://www.notion.so/workspace/Database-123abc?p=456def`
→ Dann: `456def` ist die ID

### GitHub Actions läuft nicht
→ Check: Actions → Workflows → "Daily News" → Logs
→ Stelle sicher, dass Actions im Repository aktiviert sind

## 📞 Support

- **Bug Report**: Erstelle ein Issue auf GitHub
- **Feature Request**: Diskutiere in Discussions
- **Fragen**: E-Mail: mmittelbach@gmail.com

---

**Status**: ✅ Aktiv & täglich um 06:30 CEST
**Letzte Synchronisierung**: auto
**Nächste News**: morgen 06:30 CEST
