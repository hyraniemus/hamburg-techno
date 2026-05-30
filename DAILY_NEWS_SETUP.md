# 📰 Tägliche AI-Post-Prod News Automation

Deine persönliche News-Zusammenfassung wird täglich um **06:30 CEST** generiert und in Notion gespeichert.

## Setup-Schritte

### 1️⃣ **GitHub Repository Secrets einrichten**

Gehe zu: `https://github.com/hyraniemus/hamburg-techno/settings/secrets/actions`

Erstelle folgende Secrets:

| Secret Name | Wert | Wie man es bekommt |
|---|---|---|
| `NOTION_TOKEN` | Dein Notion Integration Token | 1. Gehe zu https://www.notion.so/my-integrations 2. Create new integration 3. Kopiere Secrets Key |
| `NOTION_DATABASE_ID` | Die ID deiner News-Datenbank | Öffne deine Notion-Datenbank, kopiere die UUID aus der URL |
| `ANTHROPIC_API_KEY` | Claude API Key | https://console.anthropic.com/account/keys |
| `SLACK_WEBHOOK` | (Optional) Slack Notification | https://api.slack.com/apps/ → Incoming Webhooks |

### 2️⃣ **Notion Integration Setup**

1. **Notion Integration erstellen:**
   ```
   https://www.notion.so/my-integrations → Create new integration
   ```

2. **News-Datenbank in Notion erstellen:**
   - Neue Datenbank: `AI-Post-Prod News`
   - Properties:
     - `Title` (Titel)
     - `Date` (Datum)
     - `Category` (Type: Select - "Highlights", "Tools", "Jobs", "Action")
     - `Source` (URL)

3. **Integration mit Datenbank verbinden:**
   - Öffne Datenbank
   - `Share` → Wähle deine Integration → `Connect`

4. **Database ID kopieren:**
   - URL: `https://www.notion.so/{database_id}?...`
   - Kopiere `{database_id}` (ohne Dashes)

### 3️⃣ **Workflow testen**

Manuell triggern (ohne warten):
```bash
gh workflow run daily-news-summary.yml
```

Oder im GitHub UI: Actions → "Daily AI-Post-Prod News Summary" → "Run workflow"

---

## Tägliche Automatisierung

| Uhrzeit | Action |
|---------|--------|
| **06:30 CEST** | ⚙️ Workflow startet |
|  | 🔍 Web-Recherche (Avid, Resolve, ComfyUI, etc.) |
|  | 🤖 Claude generiert Zusammenfassung (Deutsch) |
|  | 📝 Neue Notion-Seite erstellt |
|  | 🔔 (Optional) Slack-Notification |

---

## Anpassungen

### News-Quellen ändern
Bearbeite `.github/workflows/daily-news-summary.yml`:
```yaml
queries = [
    "Dein neues Topic 1",
    "Dein neues Topic 2",
    ...
]
```

### Uhrzeit ändern
In `.github/workflows/daily-news-summary.yml`:
```yaml
cron: '30 4 * * *'  # 04:30 UTC = 06:30 CEST
```

**Beispiele:**
- `0 5 * * *` = 07:00 CEST
- `0 7 * * *` = 09:00 CEST

### Notion-Format anpassen
Das Skript erstellt pro Tag eine neue Seite. Um mehrere pro Woche zu gruppieren:
1. Erstelle eine Parent-Seite "2026 - Mai"
2. Ändere `parent` in `.github/workflows/daily-news-summary.yml`:
```yaml
"parent": {"page_id": "parent_page_id"}
```

---

## Troubleshooting

**Workflow läuft nicht?**
- ✅ Check: Actions sind im Repo aktiviert
- ✅ Check: `daily-news-summary.yml` ist in `.github/workflows/`
- ✅ Check: Alle Secrets sind korrekt eingetragen

**Notion-Fehler?**
```bash
# Test Notion Integration
curl https://api.notion.com/v1/databases/YOUR_ID \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

---

## Status

- ✅ Workflow erstellt: `.github/workflows/daily-news-summary.yml`
- ⏳ Secrets: Noch einzurichten
- ⏳ Erste Automatisierung: Wird morgen um 06:30 CEST ausgeführt
- ✅ Proof-of-Concept: [Notion-Seite vom 30.05.2026](https://www.notion.so/37048a587506813bbb60e58ab2999c13)

---

**Noch Fragen?** Poste ein Issue oder check die [GitHub Actions Docs](https://docs.github.com/en/actions).
