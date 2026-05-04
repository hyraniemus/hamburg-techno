# 🎬 AI Post-Prod Daily News Generator

Automatisierte tägliche News-Zusammenfassung für Video-Editoren, spezialisiert auf AI-Video-Produktion.

## 📋 Features

✅ **Intelligente News-Recherche** mit Claude Opus 4.7
- Recherchiert Top-News zu: Avid, DaVinci Resolve, Remotion, ComfyUI, Runway, Claude Code, Suno
- Fokus auf: Tool-Updates, AI-Video-Tools, Post-Production-Automatisierung, Freelance-Chancen
- Ignoriert irrelevante Politik/Wirtschaft

✅ **Strukturierte Ausgabe** (4 Abschnitte)
1. **Top 3 Highlights** - Kurze News mit Links & Workflow-Relevanz
2. **Tool-Updates & Tipps** - Praktische Insights mit konkreten Actions
3. **Karriere & Trends** - Freelance-Chancen für AI-Post-Prod
4. **Aktion für Heute** - Personalisierte To-Dos

✅ **Notion-Integration**
- Erstellt automatisch neue Seite in Notion-Datenbank
- Strukturiert mit Status-Tags (Wichtig/Gelesen/Später)
- Alle Quellen als Links
- Maximal 400 Wörter (deutsch, handlungsorientiert)

✅ **Automatisierung**
- Täglich um 06:30 CEST
- 2 Setup-Optionen: Cron-Job oder systemd Timer
- Logs in `/tmp/daily-news.log`

## 🚀 Quick Start

### Option 1: Cron-Job (einfach, aber weniger timezone-robust)

```bash
# 1. API Keys besorgen
# Notion Token: https://www.notion.so/profile/integrations (Create Integration)
# Anthropic Key: https://console.anthropic.com/account/keys

# 2. Automatisches Setup
bash setup-daily-news.sh

# 3. Environment Variables setzen (wenn nicht automatisch)
export NOTION_TOKEN='ntn_...'
export ANTHROPIC_API_KEY='sk-ant-...'

# 4. Manuell testen
python3 daily-news-generator.py
```

### Option 2: systemd Timer (empfohlen auf Linux)

```bash
# 1. Wie oben: API Keys besorgen

# 2. Automatisches Setup
bash setup-systemd-timer.sh

# 3. Status überprüfen
systemctl --user status daily-news-generator.timer

# 4. Logs anschauen
journalctl --user-unit daily-news-generator.service -f
```

## 📖 API Keys einrichten

### Notion Integration Token

1. Gehe zu: https://www.notion.so/profile/integrations
2. Klick "New Integration"
3. Name: "Daily News Generator"
4. Wähle Permissions: "Read" + "Update" + "Create"
5. Token kopieren

### Anthropic API Key

1. Gehe zu: https://console.anthropic.com/account/keys
2. Klick "Create Key"
3. Name: "Daily News Generator"
4. Key kopieren

## 📁 Dateistruktur

```
hamburg-techno/
├── daily-news-generator.py      # Hauptskript
├── setup-daily-news.sh           # Cron-Setup
├── setup-systemd-timer.sh        # systemd-Setup
├── NEWS-GENERATOR-README.md      # Diese Datei
└── .env (optional)               # Environment Variables
```

## ⚙️ Konfiguration

### Notion Datenbank ID
Aktuell: `d15c4ffa-fa29-4608-919d-37bfc1766392` (AI Post-Prod Daily News)

Bei Bedarf ändern in `daily-news-generator.py` Zeile 14:
```python
NOTION_DATABASE_ID = "deine-id-hier"
```

### Tageszeit anpassen
- **Cron:** `crontab -e` und Zeile ändern (Syntax: `30 6 * * *` = 06:30 täglich)
- **systemd:** `nano ~/.config/systemd/user/daily-news-generator.timer`
  - Ändere: `OnCalendar=*-*-* 06:30:00`

### Claude Modell wechseln
In `daily-news-generator.py` Zeile 48:
```python
model="claude-opus-4-7",  # Zu claude-sonnet-4-6 für schneller/günstiger
```

## 📊 Logs & Debugging

### Cron-Logs
```bash
# Letzte 20 Zeilen
tail -20 /tmp/daily-news.log

# Live folgen
tail -f /tmp/daily-news.log

# Alle Cron-Logs (System)
grep CRON /var/log/syslog | tail -20
```

### systemd-Logs
```bash
# Status
systemctl --user status daily-news-generator.timer

# Logs
journalctl --user-unit daily-news-generator.service -f

# Letzte 50 Zeilen
journalctl --user-unit daily-news-generator.service -n 50
```

## 🧪 Manuell testen

```bash
# Mit API Keys aus Environment
python3 daily-news-generator.py

# Mit Debugging
export ANTHROPIC_LOG=debug
python3 daily-news-generator.py
```

## 🔧 Troubleshooting

### "NOTION_TOKEN nicht gesetzt"
```bash
# Checke:
echo $NOTION_TOKEN
# Sollte nicht leer sein

# Setze neu:
export NOTION_TOKEN='dein-token'
# Oder in ~/.bashrc speichern:
echo "export NOTION_TOKEN='dein-token'" >> ~/.bashrc
source ~/.bashrc
```

### "Notion API Fehler 401"
- Token überprüfen
- Integration hat Zugriff auf Datenbank? (Settings → Connections → Add Connection)

### "Claude API Fehler"
- API Key überprüfen (https://console.anthropic.com/account/keys)
- Kontingent überprüft? (Billing → Usage)

### "Cron läuft nicht"
```bash
# Check ob Cron aktiv ist
sudo systemctl status cron

# Cron-Liste überprüfen
crontab -l

# Logs überprüfen
sudo tail -20 /var/log/syslog | grep CRON
```

### "systemd Timer läuft nicht"
```bash
# Service aktivieren
systemctl --user enable daily-news-generator.timer

# Timer starten
systemctl --user start daily-news-generator.timer

# Status
systemctl --user list-timers daily-news-generator.timer
```

## 🎯 Erweiterte Nutzung

### Mit GitHub Actions (alternative Cloud-Automation)
```yaml
# .github/workflows/daily-news.yml
name: Daily AI News
on:
  schedule:
    - cron: '30 4 * * *'  # 06:30 CEST = 04:30 UTC

jobs:
  news:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run news generator
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: python3 daily-news-generator.py
```

### Mit integrierten Email-Benachrichtigungen (Pro)
Ändern in `daily-news-generator.py` (nach `create_notion_page()`):
```python
import smtplib
# Sende Email an mmittelbach@gmail.com
# Siehe: https://docs.python.org/3/library/smtplib.html
```

### Eigene News-Quellen hinzufügen
Ändere in `daily-news-generator.py` den `system_prompt` um deine Quellen zu spezifizieren.

## 📚 Weitere Ressourcen

- **Notion API:** https://developers.notion.com/reference
- **Anthropic API:** https://docs.anthropic.com
- **Cron Syntax:** https://crontab.guru/
- **systemd Timer:** https://wiki.archlinux.org/title/Systemd/Timers

## 📝 Changelog

### v1.0 (2026-05-04)
- Initial release
- Cron + systemd timer support
- Claude Opus 4.7 integration
- Notion database creation

## 🤝 Support & Feedback

Falls du Issues hast oder Verbesserungen möchtest:
1. Check Logs: `tail -f /tmp/daily-news.log`
2. Test manuell: `python3 daily-news-generator.py`
3. Debugge mit: `export ANTHROPIC_LOG=debug`

---

**Happy automated news reading!** 🎬📰
