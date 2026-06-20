# 📺 Daily AI Post-Prod News Digest – Setup Guide

Automatische täglich News-Zusammenfassung für Video-Editing & Post-Production mit AI-Fokus.

## ✅ Schnellstart (5 Min)

### 1. Notion API Token beschaffen
1. Gehe zu https://www.notion.so/profile/integrations
2. Erstelle eine neue "Internal Integration"
3. Gib ihr Permissions: `read`, `update`, `create`
4. Kopiere den Secret (API Token)

### 2. GitHub Secret konfigurieren
1. Gehe zu `hamburg-techno` Repository → **Settings → Secrets and variables → Actions**
2. Klick **New repository secret**
3. Name: `NOTION_TOKEN`
4. Value: Dein Notion API Token (von Schritt 1)
5. Klick **Add secret**

### 3. Notion Page ID in GitHub Actions updaten
1. Öffne `.github/workflows/daily-news-digest.yml`
2. Ersetze `NOTION_PAGE_ID: 38548a587506812e9934f5fc738ab160` mit deiner Page ID (siehe Notion URL)
3. Commit & Push

### 4. Notion-Page für Zugriff erlauben
1. Öffne deine [Notion News-Seite](https://app.notion.so/p/38548a587506812e9934f5fc738ab160)
2. Top-Right: **...** → **Add Connections**
3. Suche nach deiner Integration (Name von Schritt 1)
4. Klick **Add connection**

### 5. Test aktivieren
```bash
# Lokal testen:
export NOTION_TOKEN=your_token_here
export NOTION_PAGE_ID=38548a587506812e9934f5fc738ab160
node scripts/daily-news-digest.js
```

---

## 🕐 Zeitplan

Die News-Zusammenfassung läuft **täglich um 06:30 CEST**:

| Zeitzone | Zeit |
|----------|------|
| CEST (Sommerzeit) | 06:30 |
| CET (Winterzeit) | 07:30 |
| UTC | 04:30 / 05:30 |

Der Cron Job (`30 5 * * *`) nutzt UTC und passt sich automatisch an.

---

## 📊 Was wird gesammelt?

### News-Quellen
- **Reddit:** r/Avid, r/davinciresolve, r/MachineLearning
- **Tech News:** Hacker News, Product Hunt
- **Blogs:** Blackmagic Design, Anthropic, Runway, Suno
- **Social:** Twitter #AIVideo #PostProduction #VideoEditing

### Fokus-Bereiche
✅ Avid Media Composer Updates & Bug Fixes  
✅ DaVinci Resolve AI-Features & Color-Grading  
✅ Remotion, ComfyUI, Runway Gen-4 Updates  
✅ Claude Code Workflow-Integration  
✅ AI-Video-Generierung & Post-Prod-Automatisierung  
✅ Suno & Musik-Produktion  
✅ Freelance-Chancen & Karriere in AI-Post-Prod  
✅ Film/Dokumentar-Produktion News  

---

## 📝 Digest-Struktur (Max 400 Wörter)

Jede tägliche News-Seite hat diese Struktur:

```
# 📺 Deine AI-Post-Prod News – [DATE]

## 🔥 Top 3 News-Highlights
1. Headline mit Link + Relevanz + Action
2. ...
3. ...

## 🛠️ Tool-Updates & Tipps
- Praktische Insights & Ressourcen

## 💼 Karriere & Trends
- Freelance-Chancen & Markttrends

## ✅ Aktion für heute
- Personalisierte Next-Steps

---
*Zuletzt aktualisiert: [DATE] | Nächste Update: [TOMORROW 06:30]*
```

---

## 🔧 Erweiterte Konfiguration

### News-API Integration (Optional)
Für bessere Quellen-Abdeckung:

```bash
npm install newsapi
# Dann in daily-news-digest.js NewsAPI integrieren
```

**Setup:**
1. Registriere dich bei https://newsapi.org (kostenlos)
2. Kopiere deinen API Key
3. Füge `NEWS_API_KEY=...` in GitHub Secrets ein

### E-Mail-Benachrichtigung (Optional)
Um auch E-Mail-Updates zu bekommen:

```bash
npm install nodemailer
# Setup in daily-news-digest.js:
# const transporter = nodemailer.createTransport({...})
```

---

## 📱 Manueller Trigger

Du kannst den Digest jederzeit manuell auslösen:

1. Gehe zu **hamburg-techno** → **Actions**
2. Wähle **Daily AI Post-Prod News Digest** Workflow
3. Klick **Run workflow** → **Branch: main** → **Run workflow**

Ergebnis: News-Update in ~2 Minuten

---

## ✅ Troubleshooting

### ❌ "NOTION_TOKEN is not set"
- Prüfe: GitHub Secrets → `NOTION_TOKEN` existiert?
- Prüfe: Richtige Repo (hamburg-techno)?
- Prüfe: Token ist aktiv & nicht abgelaufen?

### ❌ "Error updating Notion"
- Stelle sicher: Integration hat Permissions auf der Page
- Prüfe: Page ID ist korrekt
- Test lokal: `NOTION_TOKEN=xyz node scripts/daily-news-digest.js`

### ❌ "GitHub Actions won't run"
- Gehe zu **Settings → Actions → General**
- Stelle sicher: **Actions permissions** = "Allow all actions and reusable workflows"
- Stelle sicher: Workflow-Datei ist in `.github/workflows/`

---

## 📚 Weitere Ressourcen

- [Notion API Docs](https://developers.notion.com/)
- [GitHub Actions Scheduling](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)
- [News API](https://newsapi.org/)
- [Notion Integration Guide](https://www.notion.so/help/guides/creating-and-managing-integrations-with-the-notion-api)

---

**Setup abgeschlossen?** 🎉  
Dein tägliches News-Digest läuft jetzt jeden Tag um 06:30 CEST!

Weitere Fragen? Schreib an mmittelbach@gmail.com oder öffne ein Issue im Repo.
