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

### 3️⃣ GitHub Secrets hinzufügen

#### Secret 1: NOTION_TOKEN (ERFORDERLICH)
1. Gehe zu deinem Repo: https://github.com/hyraniemus/hamburg-techno
2. **Settings** → **Secrets and variables** → **Actions**
3. Neue Secret: `NOTION_TOKEN`
4. Wert: Dein Notion Integration Token
5. **Add secret**

#### Secret 2: TWITTER_API_KEY (OPTIONAL)
Für X/Twitter Integration (kostenpflichtig):
1. Gehe zu https://developer.twitter.com/en/portal/dashboard
2. Erstelle ein Projekt und generiere einen **Bearer Token**
3. Neuer Secret: `TWITTER_API_KEY`
4. Wert: Dein Twitter API Bearer Token
5. Speichern

*Hinweis: Ohne Twitter API Key wird das Script diese Quelle einfach überspringen.*

## 🎯 Was passiert dann?

**Täglich um 06:30 CEST:**

### News-Quellen (kostenlos):
- 🔴 **Reddit** (5 Subreddits): r/davinciresolve, r/Avid, r/MachineLearning, r/VideoEditing, r/aivideo
- 🟠 **Hacker News**: Top Stories zu AI/Video
- 📰 **RSS Feeds** (7 Quellen):
  - Blackmagic Design (DaVinci Resolve)
  - Anthropic (Claude & AI)
  - Runway (AI Video)
  - OpenAI (GPT updates)
  - Adobe (Premiere Pro)
  - NVIDIA AI Blog
  - Cogito (Post-Production AI)
- 🐦 **X/Twitter** (optional, kostenpflichtig): #AIVideo, #DaVinciResolve, #ComfyUI, #RunwayML, #Suno, etc.

### Keywords für Filterung:
- Tool Updates: Resolve, Avid, Remotion, ComfyUI, Runway, Claude Code, etc.
- AI-Video: Text-to-video, Video Synthesis, Generative Video
- Musik: Suno, AI Music Generation
- Film/TV: Dokumentation, Filmproduktion, Cinematography

**Ergebnis:**
- Bis zu 10 neue, gefilterte Stories zu Notion hinzu
- Status: "Review" (du kannst sie dann in "Done" setzen)
- Automatische Kategorisierung nach deinen Interessen

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

**Q: Kostet die Twitter-Integration was?**
A: Ja, aber minimal. Twitter API v2:
- Kostenlos: Tweets von verwalteten Accounts + 2 Millionen Tweets/Monat (Hobbyplan)
- ~$100/Monat: Unlimited Search (Pro Plan)
- Alternative: Nur RSS-Feeds und Reddit nutzen (völlig kostenlos!)

**Q: Welche RSS-Feeds werden gerade abonniert?**
A:
1. Blackmagic Design Blog (DaVinci Resolve Updates)
2. Anthropic Blog (Claude & AI News)
3. Runway Blog (AI Video Generation)
4. OpenAI Blog (GPT Updates)
5. Adobe Blog (Premiere Pro & Post-Prod)
6. NVIDIA AI Blog (GPU & AI Updates)
7. Cogito (Post-Production Automation)

Du kannst weitere hinzufügen: Einfach RSS_FEEDS in news_scraper.py erweitern!

**Q: Kann ich RSS-Feeds hinzufügen?**
A: Ja! Editiere `scripts/news_scraper.py` und füge deine Feeds zu `RSS_FEEDS` hinzu:
```python
RSS_FEEDS = {
    "Name": "https://example.com/feed.rss",
    "Dein Blog": "https://deintool.com/blog/feed",
}
```

---

**Status**: ✅ Ready to deploy  
**Getestet**: 2026-04-27  
**Nächster Schritt**: Setup die GitHub Secrets und der Automation startet!
