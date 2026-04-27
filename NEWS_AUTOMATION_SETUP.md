# 📰 AI-Post-Prod Daily News Automation

Automatisierte tägliche News-Zusammenfassung um 06:30 CEST direkt in deine Notion-DB.

## ⚙️ Setup in 3 Schritten

### 1️⃣ Notion Integration Token erstellen

1. Gehe zu https://www.notion.com/my-integrations
2. Klicke auf "Create new integration"
3. Name: `AI-News-Scraper`
4. Klicke "Submit"
5. Kopiere den **Internal Integration Token** (beginnt mit `secret_...`)

### 2️⃣ Notion DB mit Integration verbinden

1. Öffne deine News-DB: https://www.notion.so/4280bbdf03ee46ad8df0902a2aae410a
2. Oben rechts: **Share** → **Connections**
3. Suche nach `AI-News-Scraper` und verbinde sie

### 3️⃣ GitHub Secret hinzufügen

1. Gehe zu deinem Repo: https://github.com/hyraniemus/hamburg-techno
2. **Settings** → **Secrets and variables** → **Actions**
3. Neue Secret: `NOTION_TOKEN`
4. Wert: Dein Integration Token
5. Speichern

## 🎯 Was passiert dann?

**Täglich um 06:30 CEST:**
- Script lädt News von:
  - 🔴 **Reddit**: r/davinciresolve, r/Avid, r/MachineLearning, r/VideoEditing, r/aivideo
  - 🟠 **Hacker News**: Top stories zu AI/Video
  - Keywords: Resolve, Avid, Remotion, ComfyUI, Runway, Claude Code, Suno, etc.
- Fügt bis zu 10 neue Stories zu Notion hinzu
- Status: "Review" (du kannst sie dann in "Done" setzen)

## 🧪 Manuell testen

```bash
export NOTION_TOKEN="dein_token_hier"
python scripts/news_scraper.py
```

## 📊 In Notion sehen

- **Category**: Tool Updates | AI-Video | Career/Trends | Musik | Film/TV
- **Link**: Direkt zur Quelle
- **Relevance**: Upvotes/Engagements
- **Action**: Dein personalisierter Next-Step
- **Status**: Review → Done → Archived

## 🔄 Häufig gestellte Fragen

**Q: Warum um 06:30 CEST?**
A: GitHub Actions arbeitet in UTC. 06:30 CEST = 04:30 UTC (Winterzeit) / 05:30 UTC (Sommerzeit). Für exakte Planung benötigst du einen separaten Service.

**Q: Kann ich den Zeitplan ändern?**
A: Ja! In `.github/workflows/daily-news.yml` die `cron` Zeile anpassen: https://crontab.guru/

**Q: Was sind die Grenzen?**
A: GitHub Actions ist kostenlos, aber:
- Max ~10 gleichzeitige Jobs
- Pro privates Repo: 3000 Actions-Minuten/Monat
- News-Script läuft ~1-2 Minuten

**Q: Kann ich E-Mail-Benachrichtigungen hinzufügen?**
A: Ja! Wir können GitHub Actions mit SendGrid / AWS SES / Mailgun verbinden (kostenpflichtig) oder einen Discord/Slack Bot.

---

**Status**: ✅ Ready to deploy  
**Getestet**: 2026-04-27  
**Nächster Schritt**: Setup die GitHub Secrets und der Automation startet!
