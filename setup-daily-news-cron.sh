#!/bin/bash

# Setup-Script für tägliche News-Automatisierung
# Installiert Cron-Job für 06:30 CEST täglich

echo "🚀 AI Post-Prod Daily News – Cron Setup"
echo "========================================="
echo ""

# Check ob crontab verfügbar
if ! command -v crontab &> /dev/null; then
    echo "❌ crontab nicht gefunden. Bitte installieren:"
    echo "   Ubuntu/Debian: sudo apt-get install cron"
    echo "   macOS: cron ist vorinstalliert"
    exit 1
fi

# Skript-Pfad
SCRIPT_PATH="$HOME/hamburg-techno/generate-daily-news.sh"

if [ ! -f "$SCRIPT_PATH" ]; then
    echo "❌ Skript nicht gefunden: $SCRIPT_PATH"
    exit 1
fi

# Cron-Eintrag: 06:30 CEST (= 04:30 UTC oder 05:30 UTC+1 je nach Sommerzeit)
# Deutschland nutzt CEST (UTC+2) von März bis Oktober
# Daher: 04:30 UTC = 06:30 CEST Sommer / 05:30 UTC = 06:30 CET Winter
# Vereinfacht: 30 6 (lokale Zeit, falls TZ=Europe/Berlin gesetzt)

# Backup des aktuellen Crontabs
BACKUP_CRON="/tmp/crontab.backup.$(date +%s)"
crontab -l > "$BACKUP_CRON" 2>/dev/null || true
echo "✅ Backup erstellt: $BACKUP_CRON"

# Neuen Cron-Eintrag hinzufügen (nur wenn nicht vorhanden)
if crontab -l 2>/dev/null | grep -q "generate-daily-news.sh"; then
    echo "⏭️  Cron-Eintrag existiert bereits."
else
    # Cron-Eintrag erstellen
    # Format: Minute Stunde Tag Monat Wochentag Befehl
    # 30 6 * * * = jeden Tag um 06:30 Uhr lokale Zeit

    (crontab -l 2>/dev/null; echo "30 6 * * * TZ=Europe/Berlin $SCRIPT_PATH >> /tmp/daily-news-cron.log 2>&1") | crontab -
    echo "✅ Cron-Eintrag hinzugefügt!"
    echo "   Zeitpunkt: Täglich 06:30 Uhr CEST"
    echo "   Log-Datei: /tmp/daily-news-cron.log"
fi

# Verifyze Setup
echo ""
echo "📋 Aktuelle Cron-Einträge:"
crontab -l | grep -i "news" || echo "   (Keine News-Einträge gefunden)"

echo ""
echo "✅ Setup abgeschlossen!"
echo ""
echo "Nächste Schritte:"
echo "1. Prüfe die Logs: tail -f /tmp/daily-news-cron.log"
echo "2. Test jetzt: $SCRIPT_PATH"
echo "3. Überprüfe: $HOME/hamburg-techno/daily-news/"
echo ""
echo "Falls E-Mail nicht funktioniert:"
echo "- Richte lokales Mail-Relay ein: sudo apt-get install ssmtp"
echo "- Oder: News-Dateien werden lokal unter daily-news/ gespeichert"
