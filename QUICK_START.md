# 🚀 Quick Start: Deine tägliche AI-Post-Prod News

## ✅ Was wurde erstellt:

1. ✅ **Notion-Datenbank** "AI Post-Production Daily News"
   - 👉 https://notion.so/6c9bb5511848482aa0521ac18161c4c3
   - Erste Beispiel-News: 20.05.2026

2. ✅ **Python News-Aggregator** (`news_aggregator.py`)
   - Scraped Reddit (r/Avid, r/davinciresolve, r/ML)
   - Filtert nach deinen Keywords
   - Pusht zu Notion

3. ✅ **GitHub Action** (`.github/workflows/daily-news.yml`)
   - Läuft täglich um **06:30 CEST**
   - Automatisch, keine manuelle Intervention nötig

4. ✅ **Setup-Guide** (`DAILY_NEWS_SETUP.md`)
   - Detaillierte Konfiguration

---

## 🎯 Nächste Schritte (5 Minuten)

### 1️⃣ Notion Integration einrichten

```bash
# Gehe zu: https://www.notion.com/my-integrations
# → "New integration" 
# → Name: "Hamburg Techno News"
# → Kopiere "Internal Integration Token"

# Speichere es irgendwo sicher (brauchst du gleich)
```

### 2️⃣ GitHub Secrets hinzufügen

Gehe zu: **GitHub Repo** → **Settings** → **Secrets and variables** → **Actions**

Klicke "+ New repository secret" und füge folgende hinzu:

| Secret Name | Wert |
|------------|------|
| `NOTION_API_KEY` | Dein Token von oben (von my-integrations) |
| `SENDER_EMAIL` | `noreply@hamburg-techno.local` |

**Speichern** → Fertig! ✅

### 3️⃣ Lokal testen (optional, aber empfohlen)

```bash
cd /home/user/hamburg-techno

# API-Key als Env-Var setzen
export NOTION_API_KEY="your-integration-token-from-step-1"

# Dependencies installieren
pip install -r requirements_news.txt

# Script testen
python news_aggregator.py

# Überprüfe Notion: Eine neue News-Seite sollte erscheinen!
```

### 4️⃣ GitHub Action enablen

Gehe zu: **GitHub Repo** → **Actions** Tab
- Die Workflow `daily-news.yml` sollte dort sichtbar sein
- Sie startet automatisch täglich um 06:30 CEST
- Du kannst sie auch manuell testen:
  - Klick auf "📰 Tägliche AI-Post-Prod News Aggregation"
  - Klick "Run workflow" → "Run workflow"

---

## 📋 Überblick: Wie es funktioniert

```
06:30 CEST (täglich)
    ↓
GitHub Action startet
    ↓
news_aggregator.py läuft
    ├─ Scraped Reddit (Avid, DaVinci, ML)
    ├─ Filtert Highlights
    └─ Pusht zu Notion
    ↓
Deine Notion-Datenbank aktualisiert
    ↓
Du liest die News morgens beim Kaffee ☕
```

---

## 🎓 Customization (optional)

### Keywords anpassen?
Bearbeite `news_aggregator.py`:
```python
KEYWORDS = [
    "Avid Media Composer", "DaVinci Resolve",
    "ComfyUI", "Runway",  # ← Hier deine Tools
    # ... mehr hinzufügen
]
```

### Email-Versand hinzufügen?
Siehe `DAILY_NEWS_SETUP.md` → "Email-Versand konfigurieren"

### Andere Reddit-Subs?
Bearbeite in `news_aggregator.py`:
```python
reddit_sources = {
    'Avid': 'Avid',
    'davinciresolve': 'DaVinci Resolve',
    'MachineLearning': 'Machine Learning',
    # Weitere Subs hier hinzufügen
}
```

---

## 🆘 Troubleshooting

| Problem | Lösung |
|---------|--------|
| GitHub Action startet nicht | Überprüfe Secrets sind gesetzt (Settings → Secrets) |
| "NOTION_API_KEY not found" | Speichere das Geheimnis neu in GitHub |
| Keine News in Notion | Warte 30 Sekunden nach manueller Ausführung |
| Reddit-Verbindung blockiert | VPN nutzen oder Reddit-Fetch in Script anpassen |

---

## 📞 Support-Links

- **Notion API Docs**: https://developers.notion.com
- **GitHub Actions Docs**: https://docs.github.com/en/actions
- **Reddit-Scraping**: https://www.reddit.com/.json (Dateiformat)

---

## 🎉 Fertig!

Deine tägliche News-Aggregation läuft jetzt automatisch.

**Morgen um 06:30 CEST** erhältst du deine erste automatische News-Zusammenfassung in Notion! 

Viel Erfolg beim Aufbau deines AI-Video-Workflows! 🚀

---

Fragen? → Gehe zu `DAILY_NEWS_SETUP.md` für detaillierte Anleitung
