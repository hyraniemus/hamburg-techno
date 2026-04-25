# 🎬 Tägliche AI-Post-Prod News – Setup-Anleitung

## ✅ Was wurde erstellt

1. **`daily-news-template.md`** – Heute's News-Zusammenfassung (Beispiel)
2. **`generate_daily_news.py`** – Python-Script zur automatischen News-Generierung
3. **`.claude/news_automation.sh`** – Bash-Wrapper für Cron-Automation
4. **Diese Anleitung**

---

## 🔧 Automation einrichten (2 Optionen)

### **Option A: Linux Cron (Einfach & Zuverlässig)**

```bash
# 1. Script ausführbar machen
chmod +x /home/user/hamburg-techno/.claude/news_automation.sh
chmod +x /home/user/hamburg-techno/generate_daily_news.py

# 2. Crontab öffnen
crontab -e

# 3. Diese Zeile hinzufügen (täglich 06:30 CEST):
30 6 * * * /home/user/hamburg-techno/.claude/news_automation.sh >> /home/user/hamburg-techno/.logs/news_cron.log 2>&1

# 4. Speichern & testen
# Logs: tail -f /home/user/hamburg-techno/.logs/news_cron.log
```

### **Option B: Systemd Timer (Modern & Robust)**

```bash
# Erstelle: /etc/systemd/system/daily-news.service
sudo nano /etc/systemd/system/daily-news.service
```

**Inhalt:**
```ini
[Unit]
Description=Daily AI Post-Production News Generator
After=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/home/user/hamburg-techno
ExecStart=/home/user/hamburg-techno/generate_daily_news.py
StandardOutput=journal
StandardError=journal
```

**Timer (Datei: `/etc/systemd/system/daily-news.timer`):**
```ini
[Unit]
Description=Run Daily News at 06:30 CEST

[Timer]
# 06:30 CEST = 06:30 local (wenn CEST aktiviert)
OnCalendar=*-*-* 06:30:00
Persistent=true

[Install]
WantedBy=timers.target
```

**Aktivieren:**
```bash
sudo systemctl enable daily-news.timer
sudo systemctl start daily-news.timer
sudo systemctl status daily-news.timer

# Logs ansehen:
journalctl -u daily-news.service -f
```

---

## 📨 Optional: E-Mail oder Notion Integration

### **E-Mail einrichten** (Mailgun, SendGrid, oder lokaler SMTP)

Setze diese Umgebungsvariablen in `~/.bashrc`:

```bash
export SMTP_HOST="smtp.gmail.com"      # oder dein Provider
export SMTP_PORT=587
export SMTP_USER="dein-email@gmail.com"
export SMTP_PASS="app-password"        # Nicht dein echtes Passwort!
export SMTP_RECIPIENT="mmittelbach@gmail.com"
```

Dann uncomment in `generate_daily_news.py`:
```python
smtp_config = {
    'smtp_host': os.getenv('SMTP_HOST'),
    'smtp_port': os.getenv('SMTP_PORT', 587),
    'smtp_user': os.getenv('SMTP_USER'),
    'smtp_pass': os.getenv('SMTP_PASS'),
}
if smtp_config.get('smtp_host'):
    send_email(summary, smtp_config=smtp_config)
```

### **Notion Integration** (Optional)

1. Notion API-Token generieren: https://www.notion.so/my-integrations
2. Notion Database erstellen mit Columns: `Date | News-Summary | Top-Links`
3. Setze Umgebungsvariable:
   ```bash
   export NOTION_TOKEN="secret_xxx"
   export NOTION_PAGE_ID="abc123"
   ```
4. Uncomment in `generate_daily_news.py`:
   ```python
   if os.getenv('NOTION_TOKEN'):
       update_notion(summary, os.getenv('NOTION_TOKEN'))
   ```

---

## 📂 Output-Struktur

```
hamburg-techno/
├── news/
│   ├── news_2026-04-25.md
│   ├── news_2026-04-26.md
│   └── ...
├── .logs/
│   └── news_cron.log
├── generate_daily_news.py
├── .claude/
│   └── news_automation.sh
└── DAILY_NEWS_SETUP.md (diese Datei)
```

---

## 🧪 Test-Ausführung

```bash
# Script direkt ausführen (heute's News):
python3 /home/user/hamburg-techno/generate_daily_news.py

# Output sollte in: /home/user/hamburg-techno/news/news_YYYY-MM-DD.md
# Und im Terminal angezeigt werden
```

---

## 🚀 Troubleshooting

| Problem | Lösung |
|---------|--------|
| Cron läuft nicht | `crontab -e` → Check Zeile → Speichern → `sudo systemctl restart cron` |
| Python nicht gefunden | Nutze vollständigen Path: `/usr/bin/python3` statt `python3` |
| Anthropic API Error | Check `export ANTHROPIC_API_KEY` |
| Timezone falsch | Cron nutzt lokale Timezone – check `timedatectl` |
| Script hat keine Rechte | `chmod +x generate_daily_news.py` |

---

## 📧 Manuelle Versendung

Wenn du die News manuell versenden möchtest:

```bash
# Als E-Mail-Draft exportieren:
python3 generate_daily_news.py | mail -s "Deine AI-Post-Prod News – $(date +%d.%m.%Y)" mmittelbach@gmail.com

# Oder in Notion kopieren:
python3 generate_daily_news.py | pbcopy  # macOS
# Dann manuell in Notion einfügen
```

---

## 🔄 Regelmäßig testen

Empfehlung: **Wöchentlich** die neuesten News checken:
```bash
# Jeden Sonntag um 10:00 auch manuell ausführen:
python3 generate_daily_news.py
```

---

**Nächster Schritt:** Wähle Option A (Cron) oder B (Systemd) und lass mich wissen, wenn du Hilfe brauchst! 🚀
