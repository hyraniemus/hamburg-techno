# 📰 AI Post-Production Daily News System

**Automatisierte tägliche News-Zusammenfassung (06:30 CEST)** für Video-Editor & AI-Post-Prod-Spezialist aus Hamburg.

---

## 🚀 Quick Start (5 Minuten)

### **1️⃣ Notion Database einrichten** (Choose ONE option)

**Option A: Automatische Anleitung (Empfohlen)**
```bash
python3 setup-notion-db.py
```
Folge den Steps 1-6 in der Anleitung.

**Option B: Manuelle Setup**
- Gehe zu notion.so
- Erstelle Database "AI News Daily" mit Properties: Title, Date, Category (Select), Content, Sources
- Integration → "Daily News Generator" erstellen
- Token + DB-URL notieren

### **2️⃣ Umgebungsvariablen setzen**
```bash
# In ~/.bashrc oder ~/.zshrc hinzufügen:
export ANTHROPIC_API_KEY="sk-ant-..."  # Dein Claude API Key
export NOTION_API_KEY="secret_..."     # Notion Integration Token
export NOTION_NEWS_DB_URL="https://www.notion.so/workspace/..."  # Deine DB URL

# Dann reload:
source ~/.bashrc
```

### **3️⃣ Erste Zusammenfassung generieren**
```bash
cd /home/user/hamburg-techno

# Test lokal
python3 ai-news-generator.py

# Überprüfe:
# ✅ Markdown in news-archive/ai-news-YYYY-MM-DD.md
# ✅ (Optional) Notion Database neue Einträge
```

### **4️⃣ Automatisierung aktivieren (Choose ONE option)**

**Option A: GitHub Actions (Empfohlen – läuft automatisch)**
```bash
git add .github/workflows/daily-ai-news.yml
git commit -m "Add: Daily AI news automation (06:30 CEST)"
git push

# Dann: GitHub → Your Repo → Settings → Secrets and variables → Actions
# Add secrets: NOTION_API_KEY, NOTION_NEWS_DB_URL, ANTHROPIC_API_KEY
```

**Option B: Lokales Cron-Job** (nur wenn dein Rechner läuft)
```bash
crontab -e

# Hinzufügen:
30 6 * * * cd /home/user/hamburg-techno && python3 ai-news-generator.py
```

---

## 📁 System-Dateien

```
hamburg-techno/
├── README-DAILY-NEWS.md              ← Du bist hier
├── DAILY-NEWS-SETUP.md               ← Detaillierte Anleitung
├── ai-news-generator.py              ← Main news generator (Python)
├── setup-notion-db.py                ← Notion-Setup Helper
├── generate-daily-news.sh            ← Bash wrapper (optional)
├── daily-news-summary.md             ← Beispiel-Zusammenfassung (heute)
├── .github/workflows/
│   └── daily-ai-news.yml             ← GitHub Actions Automation
├── news-archive/
│   └── ai-news-YYYY-MM-DD.md         ← Daily generated files
└── .env.example                      ← Kopier nach .env (lokal)
```

---

## 🎯 Was du täglich bekommst

**Struktur (max 400 Wörter, Deutsch):**

```
# 📺 Deine AI-Post-Prod News – DD.MM.YYYY

## 🔥 Top 3 News-Highlights
- Avid/Resolve/Runway Updates
- Mit Quelle + direktem Link
- Workflow-Relevanz erklärt
- Actionable Insight

## 🛠️ Tool-Updates & Tipps
- 2-3 praktische Use-Cases
- Batch-Skripte, API-Integration
- Direkt heute umsetzbar

## 💼 Karriere & Trends
- AI-Post-Prod Freelance-Jobs (Hamburg, Remote)
- Gehalt, Job-Boards, Kontakte
- Startups suchen Editor-Experten

## ✅ Aktion für heute
- 1 konkreter 30-min-Task
- Tool-spezifisch
- Mit Test-Szenario
```

---

## 🔍 News-Quellen (automatisch recherchiert)

Täglich durchsucht:
- **Reddit**: r/Avid, r/davinciresolve, r/VideoEditing, r/MachineLearning
- **Hacker News**: AI, Video, Tools
- **Official Blogs**:
  - Avid Knowledge Base
  - Blackmagic Design (Resolve)
  - ComfyUI Changelog
  - Runway ML Updates
  - Remotion Docs
- **Twitter/X**: #AIVideo, #PostProduction, #AiEditing
- **Job Boards**: Glassdoor, 27km, Curious Refuge

---

## ⚙️ Konfiguration anpassen

### **Tool-Fokus erweitern** (z.B. HoudiniVFX hinzufügen)
```python
# In ai-news-generator.py, SEARCH_QUERIES dict:
SEARCH_QUERIES = {
    ...
    "houdini": "Houdini VFX AI integration 2026",
    "krita": "Krita AI painting tools 2026",
}
```

### **Zeit ändern** (z.B. 08:00 statt 06:30)
**GitHub Actions:**
```yaml
# .github/workflows/daily-ai-news.yml
cron: '0 6 * * *'  # 06:00 UTC = 08:00 CEST (summer)
```

**Cron-Generator:** [crontab.guru](https://crontab.guru/)

### **Format anpassen** (Markdown → HTML, Format ändern)
```python
# In generate_news_summary(), system_prompt anpassen
system_prompt = """... custom format ..."""
```

---

## 🐛 Troubleshooting

| Problem | Ursache | Lösung |
|---------|--------|--------|
| `ANTHROPIC_API_KEY not set` | Fehlende API Key | `export ANTHROPIC_API_KEY="..."` in ~/.bashrc |
| GitHub Actions läuft nicht | Secrets not set | Settings → Secrets → add ANTHROPIC_API_KEY, NOTION_* |
| Notion Integration fails | Token invalid/revoked | Neue Integration erstellen + Token updaten |
| Cron läuft nicht | Falsches Timing | `crontab -l` checken, [crontab.guru](https://crontab.guru/) verifizieren |
| Zu alte News | WebSearch-Quellen veraltet | News-Queries in SEARCH_QUERIES aktualisieren |

---

## 📊 Monitoring & Logs

### **GitHub Actions Logs**
```
Your Repo → Actions → Daily AI Post-Prod News Generator → Latest Run
→ Logs checken
```

### **Lokale Logs (Cron)**
```bash
# MacOS:
log stream --predicate 'process == "cron"' --level debug

# Linux:
grep CRON /var/log/syslog
# oder
sudo journalctl -u cron
```

### **Test-Run lokal**
```bash
python3 ai-news-generator.py 2>&1 | tee test-run.log
cat test-run.log
```

---

## 🎓 Beispiel: So nutzt du deine Daily News

**06:30 CEST:** Deine News-Zusammenfassung kommt rein
↓
**08:00 Uhr:** Du schaust die 3 Highlights durch (2 min)
↓
**9:00 Uhr:** Du testest die "Aktion für heute" (z.B. ComfyUI Wan 2.2)
↓
**Mittags:** Du integrierst Best Practices in deinen Workflow

---

## 💡 Pro-Tipps

1. **Sterne im Notion DB**: Interessante News für später speichern
2. **Tags hinzufügen**: "urgent", "test-today", "freelance" für Filtering
3. **Share mit Kollegen**: Notion-DB Link sharen für Team-News
4. **Archive durchsuchen**: news-archive/ mit `grep` durchsuchen
5. **Feedback-Loop**: Tool-Queries basierend auf echten Bedarf anpassen

---

## 📧 Support & Fragen

- **Issues**: Check [hamburg-techno GitHub Issues](https://github.com/hyraniemus/hamburg-techno/issues)
- **Notion API Docs**: [notion.com/developers](https://developers.notion.com/)
- **Claude API Docs**: [claude.ai/docs](https://claude.ai/docs)
- **Cron Format**: [crontab.guru](https://crontab.guru/)

---

## ✅ Checkliste: Setup Complete?

- [ ] Notion Database erstellt
- [ ] Integration Token generiert
- [ ] Umgebungsvariablen gesetzt (.bashrc/.zshrc)
- [ ] Test-Run: `python3 ai-news-generator.py` ✓
- [ ] GitHub Actions OR Cron konfiguriert
- [ ] GitHub Secrets gesetzt (falls GitHub Actions)
- [ ] Erste News-Zusammenfassung manuell geprüft
- [ ] Format/Tools nach Bedarf angepasst
- [ ] **✨ Live ab morgen 06:30 CEST! ✨**

---

**Viel Erfolg mit deinem AI News System! 🚀**

*Deine tägliche Dosis AI-Post-Production-News*
*Hamburg 🎬 | June 2026*
