# 📰 Tägliche AI-Post-Production News – Setup Guide

## 🚀 Schnellstart

Deine personalisierte News-Aggregation ist fast bereit! Folge diesen Schritten:

### 1️⃣ **Notion API-Zugang einrichten**

- Gehe zu: https://www.notion.com/my-integrations
- Klicke "New integration" → Name: "Hamburg Techno News"
- Kopiere das **Internal Integration Token**
- Gehe zu deiner Notion-Datenbank [AI Post-Production Daily News](notion://6c9bb5511848482aa0521ac18161c4c3)
- Klicke "..." (oben rechts) → "Connections" → Verbinde deine Integration

### 2️⃣ **GitHub Actions konfigurieren (automatisch täglich 06:30 CEST)**

Füge folgende **Secrets** zu deinem Repo hinzu (Settings → Secrets):

| Secret | Wert |
|--------|------|
| `NOTION_API_KEY` | Dein Integration Token von oben |
| `SENDER_EMAIL` | noreply@hamburg-techno.local |
| `SENDGRID_API_KEY` | (optional) Für Email-Versand |

**Workflow-Datei:** `.github/workflows/daily-news.yml` (bereits erstellt)

Die News werden **täglich um 06:30 CEST** automatisch aggregiert und zu Notion gepusht.

---

### 3️⃣ **Lokal testen (vor Automatisierung)**

```bash
# Dependencies installieren
pip install requests python-dotenv

# Notion API-Key als Env-Var setzen
export NOTION_API_KEY="your-integration-token"

# Script manuell ausführen
python news_aggregator.py
```

---

## ⏰ **Zeitplan Optionen**

### Option A: GitHub Actions (empfohlen)
- ✅ Kostenlos, zuverlässig
- ✅ 06:30 CEST automatisch
- Datei: `.github/workflows/daily-news.yml`

### Option B: Lokale Cron-Jobs (Linux/macOS)

```bash
# Crontab editieren
crontab -e

# Folgendes einfügen (für 06:30 CEST):
# CEST (UTC+2) = UTC 04:30
# CEST (Sommerzeit) = UTC 05:30
30 4 * * * cd /home/user/hamburg-techno && NOTION_API_KEY=xxx python news_aggregator.py

# Oder mit systemd timer (Linux, moderner):
# Siehe: systemd-timer-daily-news.service (unten)
```

**Systemd Timer (Linux – empfohlen für VPS):**

Datei: `/etc/systemd/system/hamburg-techno-news.timer`
```ini
[Unit]
Description=Hamburg Techno Daily News
After=network-online.target

[Timer]
OnCalendar=*-*-* 06:30:00
Persistent=true

[Install]
WantedBy=timers.target
```

Dann aktivieren:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hamburg-techno-news.timer
sudo systemctl status hamburg-techno-news.timer
```

### Option C: Zapier / IFTTT (keine Code nötig)
- 👉 Trigger: Daily at 06:30 CEST
- 👉 Action: REST API Call zu deinem Webhook oder Email

---

## 📧 **Email-Versand konfigurieren**

Für automatische Email-Benachrichtigungen an `mmittelbach@gmail.com`:

### Mit SendGrid (kostenfrei bis 100 Emails/Tag):

1. Registriere dich: https://sendgrid.com
2. Erstelle **API-Key** und speichere als `SENDGRID_API_KEY` Secret
3. Uncomment in `news_aggregator.py`:

```python
# Später: Email-Versand via SendGrid
import sendgrid
sg = sendgrid.SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
```

### Alternative: Gmail + Python SMTP

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText(email_body)
msg['Subject'] = f"Deine AI-Post-Prod News – {datetime.now().strftime('%d.%m.%Y')}"
msg['From'] = "noreply@hamburg-techno"
msg['To'] = "mmittelbach@gmail.com"

# Nutze App-Passwort (2FA aktiviert)
```

---

## 🎯 **Nächste Schritte**

- [ ] Notion Integration Token generiert & gespeichert
- [ ] GitHub Secrets konfiguriert
- [ ] Lokal getestet: `python news_aggregator.py`
- [ ] GitHub Actions aktiviert (sollte morgen um 06:30 laufen)
- [ ] Email-Setup (optional, aber empfohlen)

---

## 🔍 **Wie es funktioniert**

```
06:30 CEST (täglich)
        ↓
GitHub Action startet
        ↓
Python Script (`news_aggregator.py`)
        ├─ Reddit-Posts scrapen (r/Avid, r/davinciresolve, r/ML)
        ├─ Nach Keywords filtern (Avid, Resolve, ComfyUI, etc.)
        ├─ Top 3 Highlights auswählen
        └─ Zu Notion-Datenbank pushen
        ↓
Email an mmittelbach@gmail.com (optional)
```

---

## 📞 **Support**

- **Notion-Fehler?** → Prüfe Integration Permissions
- **GitHub Action läuft nicht?** → Gehe zu Actions Tab → Logs anschauen
- **Keine News gefunden?** → Reddit-API kann blockiert sein (VPN versuchen)

---

**Viel Erfolg mit deinen automatisierten AI-Post-Prod News! 🚀**
