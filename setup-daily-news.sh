#!/bin/bash
# Setup-Skript für tägliche AI Post-Prod News

echo "🚀 Richte tägliche News-Automation auf..."
echo ""

# 1. Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 nicht gefunden. Bitte installieren: sudo apt-get install python3"
    exit 1
fi

# 2. Install dependencies
echo "📦 Installiere Python-Dependencies..."
pip3 install anthropic requests

# 3. API Keys
echo ""
echo "🔑 Konfiguriere API Keys:"
echo ""
read -p "   Notion API Token eingeben: " NOTION_TOKEN
read -p "   Anthropic API Key eingeben: " ANTHROPIC_API_KEY

# 4. Add to environment
echo ""
echo "💾 Speichere API Keys in ~/.bashrc..."
echo "" >> ~/.bashrc
echo "# AI Post-Prod News Generator (Auto-generated)" >> ~/.bashrc
echo "export NOTION_TOKEN='$NOTION_TOKEN'" >> ~/.bashrc
echo "export ANTHROPIC_API_KEY='$ANTHROPIC_API_KEY'" >> ~/.bashrc

source ~/.bashrc

# 5. Make script executable
chmod +x "$(pwd)/daily-news-generator.py"

# 6. Setup Cron Job
echo ""
echo "⏰ Erstelle Cron Job (täglich 06:30 CEST)..."
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/daily-news-generator.py"

# Remove old cron if exists
crontab -l 2>/dev/null | grep -v "daily-news-generator" | crontab - 2>/dev/null

# Add new cron (06:30 CEST = 04:30 UTC im Winter, 05:30 UTC im Sommer)
# Vereinfacht: 06:30 CEST (assuming CEST = UTC+2 = 04:30 UTC)
# NOTE: Für korrekte Handling von Sommerzeit, verwende timezone-aware Cron oder systemd timer
(crontab -l 2>/dev/null; echo "30 6 * * * $SCRIPT_PATH >> /tmp/daily-news.log 2>&1") | crontab -

echo "✅ Cron Job erstellt!"
echo ""
echo "📋 Cron-Konfiguration:"
crontab -l | grep "daily-news-generator"
echo ""

# 7. Test
echo "🧪 Führe Skript einmalig aus zum Testen..."
if python3 "$SCRIPT_PATH"; then
    echo "✅ Test erfolgreich!"
else
    echo "❌ Test fehlgeschlagen - logs in /tmp/daily-news.log"
    tail -20 /tmp/daily-news.log
fi

echo ""
echo "🎉 Setup abgeschlossen!"
echo ""
echo "📝 Nächste Schritte:"
echo "   1. Überprüfe deine Notion-Datenbank: https://www.notion.so/bc10ea5cb7f34869b5ce86d572d7840d"
echo "   2. Logs anschauen: tail -f /tmp/daily-news.log"
echo "   3. Cron anpassen falls nötig: crontab -e"
echo ""
echo "💡 Tipps:"
echo "   - Für systemd timer (besser für Timezones): siehe setup-systemd-timer.sh"
echo "   - Notion Token: https://www.notion.so/profile/integrations"
echo "   - Anthropic API Key: https://console.anthropic.com/account/keys"
