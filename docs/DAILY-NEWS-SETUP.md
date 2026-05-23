# 📰 Tägliche AI-Post-Prod News – Automatisierungs-Setup

Automatische tägliche News-Zusammenfassung um **06:30 CEST**, aktualisiert deine Notion-Seite mit aktuellen Updates zu:
- Avid Media Composer
- DaVinci Resolve
- ComfyUI, Runway Gen-4
- Claude Code Integration
- AI-Video-Generierung & Post-Production
- Freelance-Chancen

## 🔧 Setup-Anleitung

### 1. GitHub Secrets konfigurieren

Gehe zu: **Settings → Secrets and variables → Actions**

Füge folgende Secrets hinzu:

#### `ANTHROPIC_API_KEY`
- **Wert**: Dein Anthropic API Key
- **Bekommst du**: [https://console.anthropic.com/](https://console.anthropic.com/)
- **Kostenlos**: Erste $5 kostenlos, danach pay-as-you-go (~$0.01 pro News-Summary)

#### `NOTION_API_TOKEN` (optional)
- **Wert**: Notion Integration Token
- **Bekommst du**: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
- **Einrichtung**:
  1. "Create new integration" → Name: "Daily News Bot"
  2. Capabilities: "Read, Update, Insert content"
  3. Submit → Copy "Internal Integration Token"

#### `NOTION_NEWS_PAGE_ID` (optional)
- **Wert**: Die Notion Page/Database, wo News landen sollen
- **Bekommst du**: 
  1. Öffne deine Notion-Seite im Browser
  2. Kopiere die ID aus der URL: `notion.so/workspace/**36948a58750681069df0c4e2fac88c34**`
  3. Das fett markierte = deine Page ID

### 2. Notion Integration mit Notion-Seite verbinden

1. Öffne deine Notion-Seite → **...** (More) → **Connections**
2. Suche "Daily News Bot" und verbinde
3. Jetzt kann der Bot neue Sub-Pages erstellen

### 3. Workflow testen

**Manual Trigger:**
```bash
# Über GitHub UI oder CLI:
gh workflow run daily-news.yml
```

**Status überprüfen:**
- Gehe zu: **Actions** Tab
- Suche "Daily AI-Post-Prod News"
- Klick auf den neuesten Run

## 📅 Schedule Details

| Zeit | Zone | Beschreibung |
|------|------|-------------|
| **06:30** | CEST (Hamburg) | ✅ Deine Lokalzeit |
| **04:30** | UTC (Winter) | Server-Zeit (November-März) |
| **05:30** | UTC (Sommer) | Server-Zeit (März-November) |

GitHub Actions rechnet automatisch mit UTC um. Die `cron: '30 4 * * *'` in der Workflow entspricht 06:30 CEST im Winter.

## 📊 Kosten-Übersicht

### Claude API (Anthropic)
- **Kosten pro News-Summary**: ~$0.02-0.05
- **Monatlich (30 Tage)**: ~$0.60-$1.50
- **Kostenlos**: Erste $5 (reicht für ~100-250 Summaries)

### Notion API
- **Kostenlos** – unbegrenzte Anfragen für Integrations

## 🔄 Automatische Ablauf

```
06:30 CEST
    ↓
GitHub Actions startet
    ↓
Python Script researcht mit Claude API
    ↓
Generates Markdown-Zusammenfassung
    ↓
Sendet an Notion API
    ↓
Neue Sub-Page in deiner Notion Database
    ↓
✅ Fertig!
```

## 🛠️ Fehlerbehandlung

### "ANTHROPIC_API_KEY not found"
→ Secret nicht konfiguriert. Gehe zu GitHub Settings → Secrets

### "NOTION_API_TOKEN not found"
→ Optional. News wird generiert, aber nicht zu Notion gesendet.
→ Manuell zu Notion kopieren oder Secret hinzufügen

### Script-Fehler?
→ Gehe zu **Actions** → Klick auf Failed Run → Siehe "Logs"

## 📝 Customization

### Andere Uhrzeit?
Ändere in `.github/workflows/daily-news.yml`:
```yaml
cron: '30 4 * * *'  # Format: minute hour * * day-of-week (UTC)
```

Beispiele:
- `'0 6 * * *'` = 06:00 UTC (08:00 CEST)
- `'0 8 * * *'` = 08:00 UTC (10:00 CEST)
- `'0 22 * * *'` = 22:00 UTC (00:00 CEST nächster Tag)

### Andere Notion-Seite?
1. Kopiere neue Page ID
2. Update `NOTION_NEWS_PAGE_ID` Secret in GitHub

### News-Fokus ändern?
Edit `scripts/daily-news.py` → Sektion `NEWS_SOURCES`:
```python
NEWS_SOURCES = {
    "davinci_resolve": "Dein Such-Query hier",
    # ...
}
```

## ✅ Erfolgreich eingerichtet?

- [ ] ANTHROPIC_API_KEY added
- [ ] NOTION_API_TOKEN added (optional)
- [ ] NOTION_NEWS_PAGE_ID added (optional)
- [ ] Workflow manual triggered & erfolgreich
- [ ] Notion-Page zeigt neue Sub-Pages

## 📞 Support

**Probleme?**
1. Check GitHub Actions Logs
2. Verify API Keys sind korrekt (copy-paste error?)
3. Notion Integration ist mit Seite verbunden?
4. Anthropic API hat genug Credits?

---

**Nächste automatische News:** Morgen 06:30 CEST 🚀
