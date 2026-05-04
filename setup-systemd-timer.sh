#!/bin/bash
# Setup systemd timer für tägliche AI Post-Prod News (bessere Timezone-Handling als Cron)

echo "🚀 Richte systemd timer für tägliche News auf..."
echo ""

# 1. Check if systemd is available
if ! command -v systemctl &> /dev/null; then
    echo "❌ systemd nicht verfügbar - verwende stattdessen: bash setup-daily-news.sh"
    exit 1
fi

SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/daily-news-generator.py"
SERVICE_DIR="$HOME/.config/systemd/user"

# 2. Create service file
echo "📝 Erstelle systemd service..."
mkdir -p "$SERVICE_DIR"

cat > "$SERVICE_DIR/daily-news-generator.service" << 'EOF'
[Unit]
Description=Daily AI Post-Prod News Generator
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 %h/hamburg-techno/daily-news-generator.py
Environment="NOTION_TOKEN=${NOTION_TOKEN}"
Environment="ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}"
StandardOutput=journal
StandardError=journal

# Restart on failure
Restart=on-failure
RestartSec=300

[Install]
WantedBy=default.target
EOF

# 3. Create timer file (06:30 CEST with proper timezone)
echo "⏰ Erstelle systemd timer..."

cat > "$SERVICE_DIR/daily-news-generator.timer" << 'EOF'
[Unit]
Description=Run Daily AI Post-Prod News Generator at 06:30 CEST
Requires=daily-news-generator.service

[Timer]
OnCalendar=*-*-* 06:30:00
Persistent=true
Unit=daily-news-generator.service

[Install]
WantedBy=timers.target
EOF

# 4. Load systemd config
echo "🔄 Laden systemd Konfiguration..."
systemctl --user daemon-reload

# 5. Enable and start timer
echo "✅ Aktiviere timer..."
systemctl --user enable daily-news-generator.timer
systemctl --user start daily-news-generator.timer

# 6. Check status
echo ""
echo "📊 Timer Status:"
systemctl --user status daily-news-generator.timer
echo ""

echo "📋 Nächste Ausführungen:"
systemctl --user list-timers daily-news-generator.timer

echo ""
echo "🎉 Setup abgeschlossen!"
echo ""
echo "📝 Useful commands:"
echo "   - Status: systemctl --user status daily-news-generator.timer"
echo "   - Logs: journalctl --user-unit daily-news-generator.service -f"
echo "   - Manuell ausführen: systemctl --user start daily-news-generator.service"
echo "   - Deaktivieren: systemctl --user disable daily-news-generator.timer"
