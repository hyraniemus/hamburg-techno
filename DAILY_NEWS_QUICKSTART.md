# 📰 AI-Post-Prod Daily News – Quick Start

**Automatische tägliche Zusammenfassung für deine AI-Video-Produktion – täglich 06:30 CEST**

---

## 🚀 Start in 3 Schritten

### 1️⃣ Notion Setup (5 Minuten)
```bash
bash scripts/setup_notion.sh
```
Folge den Anweisungen, um deine Notion-Datenbank zu verbinden.

### 2️⃣ GitHub Secrets konfigurieren
1. Gehe zu: `Settings → Secrets and variables → Actions`
2. Klicke `New repository secret`
3. Füge ein:
   - **Name**: `NOTION_TOKEN`
   - **Value**: (dein Token aus Schritt 1)
4. Wiederhole für `NOTION_DATABASE_ID`

### 3️⃣ Test
```bash
python scripts/daily_news_summary.py
```
→ Prüfe: `news_summaries/news_YYYY-MM-DD.md`

---

## 📅 Automatische Tägliche Ausführung

**Startet automatisch um 06:30 CEST** über GitHub Actions

Oder manuell triggern:
- **GitHub UI**: Actions → "Daily News" → "Run workflow"
- **CLI**: `gh workflow run daily-news.yml`

---

## 📍 Was du bekommst

Täglich um 06:30 CEST:
- ✨ **Top 3 News** (Avid, DaVinci, Remotion, ComfyUI, Runway, Claude, Suno)
- 🛠️ **Tool-Updates & Tipps** (praktische Integration)
- 💼 **Freelance-Chancen** (Hamburg + weltweit)
- 🎯 **Action-Items** (was du heute testen solltest)

Beispiel heute:
- [news_2026-05-27.md](./news_summaries/news_2026-05-27.md)

---

## 🔗 Links & Dokumentation

| Link | Beschreibung |
|------|-------------|
| [NEWS_AUTOMATION.md](./NEWS_AUTOMATION.md) | Vollständige Dokumentation |
| [scripts/daily_news_summary.py](./scripts/daily_news_summary.py) | Hauptscript |
| [news_summaries/](./news_summaries/) | Archiv alle Ausgaben |

---

## 🤔 Häufige Fragen

**Q: Kann ich ohne Notion nutzen?**  
A: Ja! Das Skript speichert automatisch lokal als Markdown in `news_summaries/`

**Q: Wie ändere ich die Uhrzeit?**  
A: Bearbeite `.github/workflows/daily-news.yml`, Cron: `30 4 * * *` (04:30 UTC = 06:30 CEST)

**Q: Kann ich eigene News-Quellen hinzufügen?**  
A: Ja! Bearbeite `NEWS_SOURCES` in `scripts/daily_news_summary.py`

**Q: Funktioniert es auch offline?**  
A: Nur mit Notion – lokal geht immer

---

## ✅ Status

- ✅ News-Automation läuft
- ✅ GitHub Actions aktiviert
- ⏳ Notion-Integration: du musst noch Token hinzufügen
- ✅ Erste Ausgabe: 2026-05-27

---

**Nächste Schritte:**
1. `bash scripts/setup_notion.sh` ausführen
2. GitHub Secrets konfigurieren
3. Morgen 06:30 CEST erste automatische News 🎉

📧 Fragen? → mmittelbach@gmail.com
