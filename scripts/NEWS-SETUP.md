# 📰 Daily AI Post-Production News Setup Guide

Automatische tägliche News-Zusammenfassung um 06:30 CEST für deine Video-Editing & AI-Produktion Workflows.

## ⚙️ Übersicht

Das System besteht aus:
- **daily-news.ts**: TypeScript Script zur Recherche und Formatierung
- **.github/workflows/daily-news.yml**: GitHub Actions für tägliches Scheduling
- **news-config.json**: Deine persönlichen Präferenzen und Quellen

## 🚀 Setup in 3 Schritten

### 1. GitHub Secrets konfigurieren

Die folgenden Secrets werden für die Automatisierung benötigt. Gehe zu:
**Repo Settings → Secrets and variables → Actions → New repository secret**

#### Notion Integration (empfohlen)

Wenn du die News-Zusammenfassung täglich in Notion aktualisieren möchtest:

```
Secret Name: NOTION_TOKEN
Value: [Dein Notion Integration Token]

Secret Name: NOTION_PAGE_ID
Value: [Deine Notion Seiten-ID]
```

**Wie bekommst du diese?**

1. Gehe zu https://www.notion.so/my-integrations
2. Erstelle eine neue Integration: "Hamburg Techno Daily News"
3. Kopiere den "Internal Integration Token"
4. Teile eine Notion-Seite mit dieser Integration
5. Kopiere die Seiten-ID aus der URL: `notion.so/[WORKSPACE]/[PAGE-ID]`

#### Email Integration (alternativ)

Wenn du lieber E-Mails möchtest (z.B. mit SendGrid):

```
Secret Name: EMAIL_SERVICE
Value: sendgrid (or mailgun, gmail, etc.)

Secret Name: EMAIL_API_KEY
Value: [Dein API Key]

Secret Name: EMAIL_RECIPIENT
Value: mmittelbach@gmail.com
```

### 2. GitHub Actions aktivieren

Stelle sicher, dass GitHub Actions in deinem Repo aktiviert ist:
- **Settings → Actions → General → Allow all actions and reusable workflows**

### 3. Test durchführen

Zum Testen des Workflows manuell:

```bash
# Option 1: GitHub UI
# Repo → Actions → Daily AI News Summary → Run workflow

# Option 2: GitHub CLI (lokal)
gh workflow run daily-news.yml
```

## 📅 Schedule anpassen

Der aktuelle Schedule ist **06:30 CEST**:

```yaml
cron: '30 4 * * *'  # 04:30 UTC (06:30 CEST im Sommer, 05:30 UTC im Winter)
```

**Möchtest du eine andere Uhrzeit?** Ändere die `cron` Expression in `.github/workflows/daily-news.yml`:

- **07:00 CEST**: `cron: '0 5 * * *'`
- **08:00 CEST**: `cron: '0 6 * * *'`
- **22:00 CEST**: `cron: '0 20 * * *'`

[Cron Expression Generator](https://crontab.guru/)

## 🎯 Anpassen der News-Quellen

Bearbeite `scripts/news-config.json`:

```json
{
  "coreInterests": [
    "Deine Top Interessen hier"
  ],
  "sources": {
    "reddit": ["r/dein-subreddit"],
    "twitter": ["#deinHashtag"],
    "blogs": ["https://dein-blog.com"]
  }
}
```

## 🔄 Wie die Automatisierung funktioniert

1. **Täglich um 06:30 CEST**:
   - GitHub Actions startet automatisch
   - `daily-news.ts` wird ausgeführt
   
2. **News recherchieren**:
   - Monitort deine konfigurierten Quellen
   - Filtert nach relevanten Themen
   - Formatiert die Zusammenfassung
   
3. **Versand**:
   - Schreibt zu Notion-Seite (wenn konfiguriert)
   - ODER sendet E-Mail
   - Optional: Committed zu Git

## 🚨 Troubleshooting

### "Secrets not found" Error
- Stelle sicher, dass die Secrets in den GitHub Settings hinzugefügt wurden
- Warte ~30 Sekunden nach dem Hinzufügen

### Notion API Error
- Überprüfe, dass der Notion Integration Token korrekt kopiert wurde
- Stelle sicher, dass die Integration die Seite hat ("Share" Button)
- Notion Seite muss eine Datenbank oder ein Page sein

### Email nicht angekommen
- Überprüfe dein Spam-Ordner
- Verifiziere den API Key des Email-Services
- Teste mit `workflow_dispatch` manuell

## 📊 Beispiel-Output

Deine tägliche News-Zusammenfassung wird so aussehen:

```
# 📰 Deine AI-Post-Prod News – 11.06.2026

## 🔝 Top 3 News-Highlights
- **Avid Media Composer 2026.6 Update** (Reddit/r/Avid) → Neue AI-Color-Grading Features
- **DaVinci Resolve GPU Acceleration** (Blackmagic Blog) → 40% schnellere Timelines
- **Claude Code 1.5 Release** (Anthropic News) → Neue Integration für Video-Workflows

## 🛠️ Tool-Updates & Tipps
- Neue ComfyUI Node für Remotion-Integration
- Runway Gen-4 API jetzt in Beta
- Suno 3.0 mit besseren Musik-Qualitätsoptionen

## 💼 Karriere & Trends
- Hamburg Startup sucht AI-Video-Editor (Freelance)
- Cape Town Post-Production Company hiring Remote

## ✅ Aktion für heute
Teste das neue Resolve AI Color-Grading Feature in deinem nächsten Projekt
```

## 🤝 Support

Bei Fragen oder Problemen:
- Überprüfe die GitHub Actions Logs: **Repo → Actions → Daily AI News Summary → Latest Run**
- Bearbeite `daily-news.ts` für Custom-Logik
- Aktualisiere `news-config.json` für deine Präferenzen

---

**Letzte Aktualisierung**: 11.06.2026
