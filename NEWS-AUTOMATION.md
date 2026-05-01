# 🎥 Daily AI Post-Production News – Automation Setup

Tägliche persönliche News-Zusammenfassung für Video-Editing & AI-Produktion (06:30 CEST)

---

## 📍 Notion Database
- **Link**: [AI Post-Production News Hub – Hamburg Techno](https://app.notion.com/p/2aa41b373890430d967c92d32f8f20dc)
- **Data Source ID**: `3d115aff-0975-431a-83f7-d344357c917c`

---

## 🚀 Quick Start

### 1. **Cron Job aktivieren** (Linux/Mac)
```bash
bash /home/user/hamburg-techno/scripts/setup-cron.sh
```

Dies erstellt einen täglichen Job um **06:30 CEST** (04:30 UTC in CEST)

### 2. **Manuell testen**
```bash
python3 /home/user/hamburg-techno/scripts/daily-ai-news.py
```

### 3. **Status checken**
```bash
tail -f /home/user/hamburg-techno/.news-generator.log
```

---

## 📋 Was ist in jeder Daily News?

### **Top 3 News-Highlights**
- AI Video Production Tools Updates (Resolve, Runway, ComfyUI)
- Integration News (Claude Code, Adobe, Remotion)
- Market/Industry Trends
- Mit Links zu Quellen

### **Tool-Updates & Tipps** (2-3 praktische Insights)
- Feature Releases & How-tos
- Workflow Optimisierungen
- Integration Tipps

### **Karriere/Trends** (1-2 Chancen)
- Hamburg Startup Opportunities
- Freelance Jobs für AI Post-Prod
- Markt-Projections

### **Aktion für heute**
- 1-2 konkrete Nächste Schritte
- Personalisierte Tasks basierend auf News

---

## 🔧 Architecture

```
hamburg-techno/
├── scripts/
│   ├── daily-ai-news.py          # Main generator script
│   └── setup-cron.sh              # Cron configuration
├── .news-generator.log            # Daily run logs
└── NEWS-AUTOMATION.md             # This file
```

### **Workflow**
1. **06:30 CEST**: Cron triggert `daily-ai-news.py`
2. **WebSearch**: Recherchiert aktuelle News (Resolve, Runway, etc.)
3. **Notion Integration**: Erstellt/Updated News-Seite
4. **Logging**: Status + Fehler in `.log`

---

## 🔌 Integration mit Claude Code

Die News können auch manuell in Claude Code generiert werden:

```bash
# Im Claude Code Terminal:
/loop 24h python3 /home/user/hamburg-techno/scripts/daily-ai-news.py
```

Dies würde täglich um die gleiche Zeit (relativ) ausführen.

---

## 📧 E-Mail-Versand (Optional)

Falls du E-Mail-Benachrichtigungen willst, kannst du das Script mit SMTP erweitern:

```python
import smtplib

# Nach News-Erstellung:
subject = f"Deine AI-Post-Prod News – {datetime.now().strftime('%d.%m.%Y')}"
body = format_email(entry_data)
send_email("mmittelbach@gmail.com", subject, body)
```

**Required**: `.env` mit:
```
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

---

## 🗂️ Kategorien

Jede News wird mit Tags versehen:
- 🟣 **DaVinci Resolve** – Editing, Color Grading
- 🔵 **ComfyUI** – Local AI Video Generation
- 🌸 **Runway** – Gen-4/Gen-4.5 News
- 🟠 **Claude Code** – AI Automation Integration
- 🟢 **Remotion** – Programmatic Video
- 🟡 **Suno** – AI Music Generation
- 🔴 **Film/TV** – Industry News

---

## ⚙️ Customization

### News Sources hinzufügen
Edit `daily-ai-news.py`:
```python
search_queries = [
    "Avid Media Composer AI updates",  # Add Avid tracking
    # ... more queries
]
```

### Zeitplan ändern
Edit `setup-cron.sh`:
```bash
CRON_TIME="0 7 * * *"  # Change to 07:00
```

### Template anpassen
Modify `format_notion_entry()` in `daily-ai-news.py`

---

## 🐛 Troubleshooting

### Cron läuft nicht?
```bash
# Check cron daemon
ps aux | grep cron

# View all cron jobs
crontab -l

# Manual test
python3 /home/user/hamburg-techno/scripts/daily-ai-news.py
```

### Notion-Verbindung fehlgeschlagen?
- Verify `NOTION_DB_ID` correct
- Check Notion API Token in environment
- See logs: `tail -100 .news-generator.log`

### Logs leeren
```bash
> /home/user/hamburg-techno/.news-generator.log
```

---

## 📚 References

- [Notion API Docs](https://developers.notion.com/)
- [DaVinci Resolve Updates](https://www.blackmagicdesign.com/products/davinciresolve/whatsnew)
- [Runway Research](https://runwayml.com/research/)
- [ComfyUI Docs](https://docs.comfy.org/)

---

**Last Updated**: 2026-05-01  
**Maintained by**: hamburg-techno automation  
**Next Run**: Daily @ 06:30 CEST
