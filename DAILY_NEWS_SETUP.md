# 🎬 Daily AI Post-Production News Digest – Setup Guide

Automatisierte tägliche News-Zusammenfassung speziell für Video-Editor und AI-Enthusiasten in Hamburg.

## 📋 Übersicht

- **Automatisches Scheduling:** GitHub Actions, täglich 06:30 CEST
- **Datenquellen:** Reddit, HackerNews, Tool Blogs, Twitter
- **Fokusthemen:** Avid, DaVinci Resolve, Remotion, ComfyUI, Runway Gen-4, AI-Video, Post-Prod Automation
- **Ausgabeformate:** Notion-Seite + Email (optonal)
- **Max. 400 Wörter:** Kurz, präzise, handlungsorientiert

---

## 🚀 SCHNELLSTART (5 Minuten)

### 1. **Notion Integration einrichten** (für Digest-Speicherung)

1. Gehe zu https://www.notion.so/my-integrations
2. Klick "Create new integration"
3. Name: `AI-News-Bot`
4. Speichere den **Internal Integration Token** (kopiert in Schritt 4)

**Notion Database vorbereiten:**
1. Erstelle eine neue Notion-Datenbank oder nutze eine vorhandene
2. Teile sie mit deiner Integration:
   - Öffne die Database
   - Klick auf "Share" → Integrationen → Wähle deine Integration
3. Kopiere die **Database ID** aus der URL:
   ```
   https://www.notion.so/[WORKSPACE_ID]?v=[VIEW_ID]
   Database ID = der lange String nach ".so/"
   ```

### 2. **SendGrid einrichten** (für Email-Versand, optional)

1. Registriere dich kostenlos bei https://sendgrid.com
2. Gehe zu "Email API" → "Integration Guide"
3. Erstelle einen **API Key** (Settings → API Keys → Create API Key)
4. Speichere den Key

### 3. **GitHub Secrets hinzufügen**

1. Öffne dein Repository auf GitHub
2. Gehe zu **Settings → Secrets and variables → Actions**
3. Füge diese Secrets hinzu:

```
NOTION_TOKEN         = [dein Internal Integration Token]
NOTION_DATABASE_ID   = [deine Database ID]
SENDGRID_API_KEY     = [dein SendGrid API Key]
RECIPIENT_EMAIL      = mmittelbach@gmail.com
```

### 4. **Workflow testen**

1. Gehe zu **Actions → Daily AI Post-Prod News Digest**
2. Klick "Run workflow" (manual trigger)
3. Beobachte die Logs → sollte erfolgreich sein

---

## 📝 WORKFLOW DETAILS

### GitHub Actions Schedule
```yaml
# Runs at 04:30 UTC = 06:30 CEST (Sommerzeit)
- cron: '30 4 * * *'
```

**Anpassung für Winterzeit (Oktober–März):**
```yaml
- cron: '30 5 * * *'  # 05:30 UTC = 06:30 CET
```

### Was der Workflow macht

1. **Triggert täglich** um 06:30 CEST
2. **Führt Python-Script aus:**
   - Sucht nach News aus konfigurierten Quellen
   - Formatiert in Markdown (max 400 Wörter)
   - Speichert in `news_digests/` Ordner
3. **Speichert in Notion** (via Notion API)
4. **Sendet Email** (via SendGrid, optional)
5. **Committed in Git** automatisch

---

## 🔧 ERWEITERTE KONFIGURATION

### News-Quellen hinzufügen

Bearbeite `scripts/daily_news_digest.py`:

```python
SEARCH_QUERIES = [
    "Avid Media Composer update bug fixes",
    "DaVinci Resolve AI features",
    # Füg deine eigenen Queries hinzu
]
```

### Email-Template anpassen

In `daily_news_digest.py` die `generate_digest()` Methode anpassen für Custom HTML, Styling, etc.

### Notion-Template

Erstelle in Notion diese Spalten für die Auto-Sync:
- `Date` (Datums-Property)
- `Title` (Text - wird auto-gefüllt mit Datum)
- `Digest` (Rich Text - kompletter Inhalt)
- `Top 3 News` (Text - extrahierte Highlights)
- `Action Item` (Checkbox - für Tracking)

---

## 🐛 TROUBLESHOOTING

### Workflow läuft nicht um 06:30?
- GitHub Actions kann **5-10 Minuten Verzögerung** haben
- Timezone ist immer UTC – berechne: `CEST = UTC+2`
- Testen mit `workflow_dispatch` manuell

### Notion-Fehler: "Invalid token"
- Token muss "Internal Integration Token" sein (nicht API-Secret)
- Database muss mit der Integration geteilt sein
- Prüfe: Settings → Connections → deine Integration

### SendGrid-Email kommt nicht an
- API Key in den Secrets korrekt hinterlegt?
- Spam-Folder checken
- Free-Plan: max 100 Emails/Tag

### Script produziert leere Digests
- Prüfe deine News-Quellen (sind APIs erreichbar?)
- Logs in GitHub Actions anschauen
- Bei API-Rate-Limits: Retry-Logic hinzufügen

---

## 📊 BEISPIEL-DIGEST

Siehe `news_digests/sample_digest_2026_06_10.md` für aktuelles Format.

**Struktur:**
1. **🔥 TOP 3 NEWS** (kurz, mit Links + Relevanz)
2. **🛠️ TOOL-UPDATES** (2-3 praktische Tipps)
3. **💼 KARRIERE & TRENDS** (Freelance-Chancen)
4. **✅ AKTION FÜR HEUTE** (1 personalisierter Next-Step)

---

## 💡 PRO-TIPPS

### 1. Eigene News-Quellen via Webhook
Falls du eigene Datenquellen (z.B. Slack, Discord) einbauen willst:
```python
# In daily_news_digest.py
def fetch_custom_sources(self):
    # Custom API calls hier
    pass
```

### 2. Notion-Filter für "Unread"
In Notion: Erstelle Filter `Status = "Unread"` um neue Digests zu sehen

### 3. Newsletter-Version
Exportiere Notion-Seite als HTML → sende via Email-Service mit Template

### 4. Lokales Testing
```bash
python scripts/daily_news_digest.py
# Erzeugt lokale Markdown-Datei in news_digests/
```

---

## 🔐 SICHERHEIT

- **Secrets sind GitHub-verschlüsselt** – niemals ins Repo committen
- **API Keys in `.env` lokal?** → Nutze `.env.local` und `.gitignore`
- **Rate-Limits beachten** bei News-APIs

---

## 📞 SUPPORT & WEITERFÜHRUNG

### Weitere Automatisierungen
- [ ] Slack-Bot Integration (Post täglich in #news-feed)
- [ ] RSS-Feed für deine Website
- [ ] Video-Thumbnail Vorschau (AI-generiert)
- [ ] Discord Webhook für Community

### Feedback zur Relevanz
Tracke in Notion, welche News du aktiv nutzt:
- [ ] Resolve-Updates: Wie oft getestet?
- [ ] Freelance-Chancen: Wie viele Bewerbungen?
- [ ] Tool-Tips: Welche funktionieren best?

---

**Fragen? Schreib einen Issue oder öffne ein Discussion in diesem Repo!**

Generated: 2026-06-10 | Next Digest: 2026-06-11 06:30 CEST
