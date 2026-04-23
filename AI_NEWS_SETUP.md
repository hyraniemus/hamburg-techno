# 📰 AI-Post-Production News Digest – Automatisiertes Setup

Tägliche personalisierte News-Zusammenfassung (max. 400 Wörter) um **06:30 CEST** als Notion-Seite oder E-Mail.

---

## 🚀 Schnellstart (5 Minuten)

### 1. Environment-Variablen setzen

```bash
# Anthropic API Token (für Claude)
export ANTHROPIC_API_KEY="sk-ant-..."

# Notion Integration (Optional, für Auto-Save zu Notion)
export NOTION_TOKEN="secret_..."
export NOTION_NEWS_DB_ID="your-database-id"

# E-Mail Versand (Optional, falls über SendGrid)
export SENDGRID_API_KEY="SG...."
export SENDGRID_FROM_EMAIL="noreply@hamburg-techno.de"
```

### 2. Python Dependencies installieren

```bash
pip install -r requirements-news.txt
```

### 3. Manuell testen

```bash
python3 daily_news_digest.py
```

Sollte folgende Datei erstellen: `ai_news/news_YYYY-MM-DD.md`

---

## ⏰ Automatisierung – Tägliche Ausführung (06:30 CEST)

### Option A: Cron Job (Linux/Mac)

```bash
# Editiere crontab
crontab -e

# Füge diese Zeile hinzu (06:30 CEST = 05:30 UTC im Sommer, 04:30 UTC im Winter):
30 5 * * * cd /home/user/hamburg-techno && python3 daily_news_digest.py >> logs/news_digest.log 2>&1

# Oder mit Notion-Integration:
30 5 * * * cd /home/user/hamburg-techno && NOTION_TOKEN=... NOTION_NEWS_DB_ID=... python3 daily_news_digest.py
```

### Option B: GitHub Actions (für Cloud-Automation)

Erstelle `.github/workflows/daily-news.yml`:

```yaml
name: Daily AI News Digest

on:
  schedule:
    - cron: '30 4 * * *'  # 06:30 CEST = 04:30 UTC (April-Oct)

jobs:
  generate-digest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements-news.txt
      
      - name: Generate news digest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          NOTION_NEWS_DB_ID: ${{ secrets.NOTION_NEWS_DB_ID }}
        run: python3 daily_news_digest.py
      
      - name: Commit & push
        run: |
          git config user.name "News Bot"
          git config user.email "bot@hamburg-techno.de"
          git add ai_news/
          git commit -m "Daily news digest - $(date +%Y-%m-%d)" || true
          git push
```

### Option C: Claude Code Loop (In-Session)

Nutze den `/loop` Skill (für Testing/Development):

```
/loop 1d python3 daily_news_digest.py
```

Dies würde täglich dieselbe Zeit in der Session ausführen.

---

## 📧 E-Mail Versand Einrichten

### Via SendGrid (Empfohlen für Einfachheit)

1. **SendGrid Account erstellen**: https://sendgrid.com
2. **API Key generieren** und in `.env` speichern
3. **Script anpassen** (`daily_news_digest.py`):

```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_digest(digest: str):
    msg = Mail(
        from_email="news@hamburg-techno.de",
        to_emails="mmittelbach@gmail.com",
        subject=f"Deine AI-Post-Prod News – {date}",
        plain_text_content=digest
    )
    
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(msg)
    print(f"Email sent: {response.status_code}")
```

### Via SMTP (für lokalen Mail-Server)

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText(digest)
msg['Subject'] = f'Deine AI-Post-Prod News – {date}'
msg['From'] = 'news@hamburg-techno.de'
msg['To'] = 'mmittelbach@gmail.com'

server = smtplib.SMTP('localhost', 587)
server.starttls()
server.send_message(msg)
server.quit()
```

---

## 📌 Notion Integration Einrichten

### 1. Notion Integration erstellen

- Gehe zu: https://www.notion.so/my-integrations
- **"New integration"** → Name: "AI News Bot"
- **Capabilities**: `INSERT`, `READ`, `UPDATE`
- Kopiere den **"Internal Integration Token"**

### 2. Notion Database vorbereiten

- Erstelle eine neue Seite in Notion (z.B. "AI-News")
- Gebe dem Bot Zugriff: **Share → Invite bot**

### 3. Environment-Variablen

```bash
export NOTION_TOKEN="secret_abc123..."
export NOTION_NEWS_DB_ID="12345678-1234-1234-1234-123456789012"
```

### 4. Test-Run

```bash
python3 notion_integration.py
```

Sollte eine neue Seite in Notion erstellen.

---

## 📊 Was wird aggregiert?

### News-Quellen (Automatisiert):
- 🔍 **Web-Search**: Blackmagic Design, GitHub Releases, Reddit, HackerNews
- 🎬 **Tool-Blogs**: DaVinci Resolve, ComfyUI, Runway, Remotion
- 📱 **Social**: X/Twitter #AIVideo, #PostProduction

### Fokus-Themen:
✓ **Tools**: Avid, DaVinci, ComfyUI, Runway Gen-4, Remotion, Claude Code
✓ **Workflows**: AI-Video-Generierung, Post-Prod-Automatisierung
✓ **Career**: Freelance-Chancen, Hamburg/Remote-Jobs
✓ **Skills**: Suno (Musik), Dokumentation
✗ **Ignorieren**: Politik, allgemeine Wirtschaft

---

## 🔧 Troubleshooting

### Problem: "ANTHROPIC_API_KEY not set"
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

### Problem: "Notion API error 401"
- Token abgelaufen? → Neuen Token generieren
- Bot hat keinen Zugriff? → Database share mit Bot

### Problem: "Email nicht versendet"
- SendGrid API Key korrekt?
- Email-Domain verified in SendGrid?
- Check logs: `tail logs/news_digest.log`

### Problem: "Script läuft nicht um 06:30"
- Cron-Zeit-Zone überprüfen: `timedatectl`
- Log überprüfen: `grep CRON /var/log/syslog | tail -20`
- Test: `run-parts --test /etc/cron.daily`

---

## 📝 Logs & Monitoring

Logs werden gespeichert in:
```
logs/news_digest.log
ai_news/news_YYYY-MM-DD.md  (Markdown-Export)
```

Letzten 5 Runs anzeigen:
```bash
tail -50 logs/news_digest.log
ls -lht ai_news/ | head -5
```

---

## 🎯 Nächste Schritte

1. ✅ **Environment-Variablen setzen**
2. ✅ **Manuell testen**: `python3 daily_news_digest.py`
3. ✅ **Notion-Integration testen** (Optional)
4. ✅ **Cron Job einrichten** für tägliche 06:30 CEST
5. ✅ **Logs monitoren** erste Woche

---

## 📞 Support & Customization

### Fokus ändern?
Edit `SEARCH_QUERIES` und `SYSTEM_PROMPT` in `daily_news_digest.py`

### Format anpassen?
Edit Struktur in `SYSTEM_PROMPT` (Top 3, Tool-Updates, etc.)

### Neue Quellen hinzufügen?
Ergänze `SEARCH_QUERIES`:
```python
SEARCH_QUERIES = [
    "your new query here",
    ...
]
```

---

**Erstellt für**: Video-Editor → AI-Post-Production-Specialist (Hamburg)
**Status**: ✓ Ready to deploy
**Letzte Aktualisierung**: 2026-04-23
