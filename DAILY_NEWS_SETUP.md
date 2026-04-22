# 📺 AI Post-Prod Daily News – Automatisierungs-Setup

Deine personalisierte News-Zusammenfassung zu AI-Video-Production, Avid/Resolve/Remotion, Runway, ComfyUI und Suno – täglich um 06:30 CEST.

---

## 🚀 Quick Start (5 Minuten)

### 1. Setup ausführen
```bash
cd ~/hamburg-techno
bash setup-daily-news-cron.sh
```

### 2. Sofort testen
```bash
bash generate-daily-news.sh
```

Schau in `/hamburg-techno/daily-news/` – dort sollte heute's Zusammenfassung sein.

### 3. Logs überwachen
```bash
tail -f /tmp/daily-news-cron.log
```

---

## 📧 E-Mail-Versand

**Option A: Falls Mailutils installiert (empfohlen)**
```bash
sudo apt-get install mailutils    # Linux
# macOS hat Mail bereits built-in
```
Das Skript versendet News automatisch an `mmittelbach@gmail.com`

**Option B: Falls nicht konfigurierbar**
News werden lokal unter `daily-news/` gespeichert.  
Du kannst sie manuell lesen oder zum Repo committen.

**Option C: Notion-Integration** (alternativ)
Zum manuellen Hochladen:
- Öffne deine Notion-Seite
- Copy-Paste den Inhalt aus `daily-news/news-YYYY-MM-DD.md`

---

## 📁 Dateistruktur

```
hamburg-techno/
├── generate-daily-news.sh          # Hauptskript (täglich ausgeführt)
├── setup-daily-news-cron.sh        # Cron-Automatisierung einrichten
├── DAILY_NEWS_SETUP.md             # Diese Datei
└── daily-news/
    ├── news-2026-04-22.md          # Heute's Zusammenfassung
    ├── news-2026-04-21.md
    └── ...
```

---

## 🔧 Manuelle Cron-Konfiguration

Falls `setup-daily-news-cron.sh` nicht funktioniert, manuell hinzufügen:

```bash
crontab -e
```

Dann diese Zeile anfügen:
```
30 6 * * * TZ=Europe/Berlin /home/user/hamburg-techno/generate-daily-news.sh >> /tmp/daily-news-cron.log 2>&1
```

**Speichern**: `:wq` (in vi)

---

## 📰 Was ist in der Zusammenfassung?

Jeden Tag um 06:30 CEST erhältst du:

### 1️⃣ Top 3 News-Highlights
- Neue Tool-Updates (DaVinci Resolve, Runway, ComfyUI, Remotion, etc.)
- Quelle & Link
- Praktischer Tipp für deinen Workflow
- Aktion: Was du heute testen solltest

### 2️⃣ Tool-Updates & Tipps
- 2-3 praktische Insights
- Integration zwischen Tools
- Performance-Tipps

### 3️⃣ Karriere & Trends
- Freelance-Chancen für AI Post-Production
- Markttrends
- Hamburg/Europe-fokussierte Chancen

### 4️⃣ Aktion für Heute
- 1 personalisierter Next-Step
- Zeitaufwand
- Konkretes Ziel

---

## ⚙️ Konfiguration (Optional)

Bearbeite `generate-daily-news.sh` um anzupassen:

```bash
# Zeile 9-10: E-Mail-Adresse ändern
EMAIL="deine-email@example.com"

# Zeile 12: Speicherort für News ändern
NEWS_DIR="$HOME/deine-news-ordner"
```

Dann erneut cron installieren:
```bash
bash setup-daily-news-cron.sh
```

---

## 🐛 Troubleshooting

### E-Mail funktioniert nicht
```bash
# Check Mail-Tool
which mail
which ssmtp
which sendmail

# Falls fehlend: installieren
sudo apt-get install mailutils  # Linux
# macOS: vorinstalliert

# Test E-Mail versenden
echo "Test" | mail -s "Test Email" mmittelbach@gmail.com
```

### Cron läuft nicht
```bash
# Check ob cron aktiv
sudo systemctl status cron  # Linux
launchctl list | grep cron  # macOS

# Check Cron-Logs
grep CRON /var/log/syslog  # Linux
log stream --level debug --predicate 'eventMessage contains[c] "cron"'  # macOS
```

### News-Datei wird nicht erstellt
```bash
# Manuell testen
bash /home/user/hamburg-techno/generate-daily-news.sh

# Berechtigungen prüfen
ls -la /home/user/hamburg-techno/daily-news/

# Log anschauen
cat /tmp/daily-news-cron.log
```

---

## 📚 Quellen für deine News

Das Skript recherchiert täglich:
- 🔴 Reddit (r/davinciresolve, r/Avid, r/MachineLearning)
- 🟠 Hacker News (AI, Video, Tools)
- 🟡 Twitter (Hashtags: #AIVideo, #PostProduction, #ComfyUI, #Remotion)
- 🟢 Tool-Blogs (Blackmagic Design, Anthropic, Runway, ComfyUI)
- 🔵 Developer Docs (Remotion, Claude Code, Suno)

---

## 🎯 Nächste Schritte

1. **Jetzt**: `bash setup-daily-news-cron.sh`
2. **Testen**: `bash generate-daily-news.sh`
3. **Überprüfen**: Logs in `/tmp/daily-news-cron.log`
4. **Morgen um 06:30 CEST**: Erste automatische Zusammenfassung!

---

## 💡 Pro-Tipps

- **Archive**: Alle News unter `daily-news/` bleiben erhalten für später
- **Integration**: News-Markdown mit Claude Code für Video-Automation kombinieren
- **Notion-Sync**: Exportiere monatlich deine Top-News in Notion
- **Git**: News werden zu deinem Repo committed für Versionskontrolle

---

**Fragen? Debugging?** Die Logs sagen dir alles: `tail -f /tmp/daily-news-cron.log`

Happy Learning! 🚀
