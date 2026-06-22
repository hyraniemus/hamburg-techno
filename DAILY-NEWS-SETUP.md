# 📰 AI Post-Production Daily News System – Setup Guide

Automatisierte tägliche News-Zusammenfassung (06:30 CEST) für deine Kerninteressen: Avid, Resolve, ComfyUI, Runway, Remotion, Suno, Claude Code, Freelance-Chancen.

---

## 🎯 System-Komponenten

```
Claude Code (dein Agent)
    ↓
WebSearch API (aktuelle News alle 24h)
    ↓
Daily News Generator (Deutsch, max 400 Wörter)
    ↓
Notion Database (Public/Private)
    ↓
Email Notification (mmittelbach@gmail.com)
```

---

## 📋 Setup-Schritte

### **Option 1: Notion Database (Empfohlen)**

1. **Notion-Seite erstellen** (falls nicht existent)
   - Gehe zu notion.so
   - Erstelle neue Seite/Database: "AI News Daily"
   - Properties: Title (Name), Date (Datum), Category (Tool/News), Content (Text), Source (Link)

2. **Notion API Key generieren**
   - → Settings & Members → Integrations → Create integration
   - Name: "Daily News Generator"
   - Copy Integration Token

3. **GitHub Secrets konfigurieren** (falls GitHub Actions nutzen)
   ```
   Repository → Settings → Secrets and variables → Actions
   
   Secret Name: NOTION_API_KEY
   Secret Value: [your-integration-token]
   
   Secret Name: NOTION_NEWS_DB_URL
   Secret Value: https://notion.so/workspace/your-database-id
   ```

4. **Test-Run ausführen**
   ```bash
   cd /home/user/hamburg-techno
   bash generate-daily-news.sh
   ```

---

### **Option 2: Email-Versand (Alternative)**

Wenn Notion nicht verfügbar:

```bash
# Installiere mail-utility
sudo apt-get install mailutils

# Konfiguriere Postfix oder SendGrid
# Email wird um 06:30 CEST automatisch versendet an: mmittelbach@gmail.com
```

---

## 🔧 Konfiguration

### **Anpassen der Suchbegriffe** (`generate-daily-news.sh`)

```bash
# Beispiel: Neue Tool hinzufügen
fetch_news "HoudiniVFX AI integration updates 2026" "Houdini"

# Oder: Spezifische Hamburg-Jobbörsen
fetch_news "AI video jobs Hamburg freelance 2026 Cape Town" "Jobs"
```

### **Scheduling ändern**

Wenn nicht 06:30 CEST, sondern andere Zeit:

**GitHub Actions** (`.github/workflows/daily-ai-news.yml`):
```yaml
on:
  schedule:
    - cron: '30 5 * * *'  # 05:30 UTC = 06:30 CEST (summer)
                          # 04:30 UTC = 05:30 CET (winter)
```

**Cron-Format Anleitung:**
```
Minute (0-59) | Stunde (0-23) | Tag (1-31) | Monat (1-12) | Wochentag (0-7)
    30        |      5        |    *      |      *      |       *
```

---

## 📊 Inhalt: Jeden Tag neu generiert

### **Top 3 News-Highlights**
- Mit Quelle + Link
- Relevanz für deinen Workflow
- Actionable insight

### **Tool-Updates & Tipps**
- 2-3 praktische Insights
- Batch-Skripte, Integration-Tipps
- Direkt umsetzbar

### **Karriere & Trends**
- Freelance-Chancen (Hamburg, Cape Town, Remote)
- Gehalt/Budget-Info falls verfügbar
- Job-Boards + Kontakte

### **Aktion für heute**
- 1 personalisierter Next-Step
- 30-min-Tasks
- Konkrete Test-Szenarien

---

## 🚀 Start-Optionen

### **Option A: Manueller Test**
```bash
cd /home/user/hamburg-techno
bash generate-daily-news.sh
```
→ Generiert erste Zusammenfassung

### **Option B: GitHub Actions aktivieren**
```bash
git add .github/workflows/daily-ai-news.yml
git commit -m "Add daily AI news automation"
git push
```
→ Läuft täglich um 06:30 CEST automatisch

### **Option C: Lokales Cron-Job (Nur wenn Session läuft)**
```bash
# Edit crontab
crontab -e

# Add line:
30 6 * * * cd /home/user/hamburg-techno && bash generate-daily-news.sh
```
⚠️ Funktioniert nur wenn dein Rechner/Session ständig läuft

---

## 🔍 News-Quellen (täglich aktualisiert)

Die Recherche sucht automatisch in:

- **Reddit**: r/Avid, r/davinciresolve, r/MachineLearning, r/VideoEditing
- **Hacker News**: AI, Video, Tool Updates
- **Offiziell**: 
  - Avid Knowledge Base (kb.avid.com)
  - Blackmagic Design Blog (DaVinci Resolve)
  - ComfyUI Changelog & Forum
  - Runway ML Updates (runwayml.com/changelog)
  - Remotion Docs + GitHub
- **Twitter/X**: #AIVideo, #PostProduction, #VideoAI
- **Job Boards**:
  - Glassdoor (Hamburg)
  - 27km.com (Freelance)
  - Curious Refuge (AI Jobs)
  - ZipRecruiter (Freelance-Raten)

---

## 📧 Email-Integration (Optional)

Falls du nur Email willst (ohne Notion):

```bash
# Erstelle ~/.env
cat > ~/.env << EOF
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
RECIPIENT=mmittelbach@gmail.com
EOF

# Exportiere in Script
source ~/.env

# Im Script:
echo "$SUMMARY_CONTENT" | mail -s "Deine AI-Post-Prod News – $(date +%d.%m.%Y)" $RECIPIENT
```

---

## ⚙️ Troubleshooting

| Problem | Lösung |
|---------|--------|
| GitHub Actions läuft nicht | Check: Secrets gesetzt? Workflow-Syntax ok? → Actions-Tab prüfen |
| Notion-Integration fehlt | API-Key ungültig? DB-URL korrekt? → Notion Settings prüfen |
| Email kommt nicht an | SMTP-Credentials ok? Firewall? → Test mit `mail` command |
| News-Inhalte zu alt | WebSearch-Quellen aktualisieren? Reddit-Subs subscribed? |

---

## 📞 Feedback & Anpassungen

Wenn du:
- **Neue Tools hinzufügen** willst → Suchbegriffe in `generate-daily-news.sh` erweitern
- **Zeit ändern** möchtest → Cron-Expression anpassen
- **Format umgestalten** willst → Markdown-Template editieren
- **Email + Notion** kombinieren möchtest → Beide Schritte im Workflow

---

## ✅ Nächste Schritte

1. ✅ **Notion Database einrichten** (oder Email-Setup)
2. ✅ **GitHub Secrets konfigurieren**
3. ✅ **Workflow testen**: `.github/workflows/daily-ai-news.yml` manual trigger
4. ✅ **Erste Zusammenfassung prüfen** (Qualität, Format, Relevanz)
5. ✅ **Feedback-Runde**: Anpassungen an Suchbegriffe/Format?

**Fertig! Ab morgen um 06:30 CEST läuft es automatisch.** 🚀
