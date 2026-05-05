# 🗞️ Tägliche AI Post-Prod News – Setup-Anleitung

## Übersicht

Dein persönliches **Daily News System** für AI-Video-Production:
- **Automatisch** um **06:30 CEST** täglich
- **Notion-Datenbank** als zentrale Hub
- **Claude AI** recherchiert aktuelle News
- **Fokus** auf deine Kerninteressen: Avid, Resolve, AI-Tools, Freelance-Chancen

---

## ✅ Setup in 3 Schritten

### 1. **Anthropic API Key einrichten**

1. Gehe zu [console.anthropic.com](https://console.anthropic.com)
2. Login oder neu registrieren
3. **API Keys** → **Create Key** → Copy
4. In deinem GitHub Repository: **Settings** → **Secrets and Variables** → **Actions**
5. **New repository secret** hinzufügen:
   - Name: `ANTHROPIC_API_KEY`
   - Value: dein API Key

### 2. **Notion Integration einrichten**

1. Gehe zu [notion.com/integrations](https://notion.com/integrations)
2. **Create new integration**:
   - Name: "AI News Generator"
   - Select type: "Internal"
3. **Show API token** → Copy
4. In GitHub Actions Secrets:
   - Name: `NOTION_TOKEN`
   - Value: dein Notion API Token
5. **Notion-Datenbank Zugriff geben**:
   - Öffne deine Datenbank: [https://www.notion.so/8f1896996f7f42059b1a447f64cf27e9](https://www.notion.so/8f1896996f7f42059b1a447f64cf27e9)
   - **...** (oben rechts) → **Add connections**
   - Wähle deine Integration "AI News Generator"
   - Done! ✅

### 3. **GitHub Actions aktivieren**

Der Workflow ist bereits angelegt:
- Datei: `.github/workflows/daily-news.yml`
- **Automatisch**: jeden Tag 06:30 CEST
- **Manuell auslösen** (testen): GitHub → Actions → "Daily AI Post-Production News" → **Run workflow**

---

## 🧪 Sofort testen

```bash
# Installation lokal (optional)
pip install anthropic notion-client

# Manuell starten
python scripts/ai_news_generator.py
```

---

## 📊 Deine Notion-Datenbank

**URL**: [https://www.notion.so/8f1896996f7f42059b1a447f64cf27e9](https://www.notion.so/8f1896996f7f42059b1a447f64cf27e9)

**Struktur**:
| Feld | Inhalt |
|------|--------|
| **Datum** | Titel + Datum (z.B. "🗞️ AI Post-Prod News – 2026-05-05") |
| **Top 3 Highlights** | News mit Relevanz für dein Workflow |
| **Tool-Updates & Tipps** | Praktische Actionables |
| **Karriere & Trends** | Freelance-Chancen & Markt-Insights |
| **Aktion für heute** | Ein konkreter Next-Step |
| **Quellen** | Links zu Reddit, GitHub, Blogs, etc. |
| **Status** | Draft / Veröffentlicht / Geplant |

---

## 🔧 Konfiguration anpassen

### News-Themen ändern

Bearbeite `scripts/ai_news_generator.py`, Zeile ~20:

```python
TOPICS = """
Avid Media Composer Updates
DaVinci Resolve
... (deine Interessen)
"""
```

### Zeitplan ändern

Bearbeite `.github/workflows/daily-news.yml`:

```yaml
- cron: '30 4 * * *'  # 04:30 UTC = 06:30 CEST
```

CRON-Zeiten:
- **30 4 * * *** = täglich 06:30 CEST (Mai-Oktober)
- **30 5 * * *** = täglich 06:30 CET (November-März)
- **30 9 * * 1** = montags 11:30 CEST

---

## 🐛 Troubleshooting

### "NOTION_TOKEN invalid"
→ Check Notion Integration Connection in der Datenbank (siehe Step 2.5)

### "ANTHROPIC_API_KEY not found"
→ Secret in GitHub Actions hinzugefügt? Workflow neu starten!

### Workflow läuft, aber keine News in Notion
→ Manuell testen: `python scripts/ai_news_generator.py`
→ Logs in GitHub Actions ansehen (Actions Tab)

### Workflow läuft garnicht
→ GitHub Actions **aktiviert**? Settings → Actions → "Allow all actions and reusable workflows"

---

## 💡 Next Steps

1. ✅ Setup komplett → First news generated? Check Notion-Datenbank
2. 📊 Daily views erstellen (z.B. "Diese Woche", "Status=Veröffentlicht")
3. 📧 Optional: IFTTT/Make.com integrieren für Email-Digest?
4. 🚀 Portfolio erweitern mit getesteten AI-Tools aus den News

---

## 📞 Support

Bei Fragen:
- GitHub Actions Logs: **Actions Tab** in deinem Repo
- Notion API Docs: [notion.com/developers](https://notion.com/developers)
- Anthropic Claude Docs: [console.anthropic.com/docs](https://console.anthropic.com/docs)

---

**Viel Erfolg mit deinem neuen AI-News-System! 🚀**
