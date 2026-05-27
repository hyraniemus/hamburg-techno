#!/bin/bash
# Setup für Notion-Integration der Daily News

echo "🔧 Notion-Integration Setup"
echo "======================================"
echo ""

echo "📋 Schritt 1: Notion Integration Token erstellen"
echo "1. Gehe zu: https://www.notion.com/my-integrations"
echo "2. Klicke 'New Integration'"
echo "3. Name: 'Hamburg-Techno News Bot'"
echo "4. Bestätige die Bedingungen und klicke 'Create Integration'"
echo "5. Kopiere den 'Internal Integration Token'"
echo ""
read -p "Füge deinen Notion Token ein: " NOTION_TOKEN

echo ""
echo "📋 Schritt 2: Notion-Datenbank erstellen"
echo "1. Erstelle eine neue Seite in Notion"
echo "2. Füge eine neue Datenbank (Table) ein"
echo "3. Name: 'AI-Post-Prod News'"
echo "4. Eigenschaften:"
echo "   - Name (Text/Title)"
echo "   - Date (Date)"
echo "   - Category (Select) -> 'Daily News'"
echo "5. Klicke auf die 3 Punkte -> 'Add connection'"
echo "6. Wähle 'Hamburg-Techno News Bot'"
echo ""
read -p "Füge deine Notion Database ID ein (siehe URL nach 'p='): " NOTION_DB_ID

echo ""
echo "🔐 GitHub Secrets konfigurieren"
echo "1. Gehe zu: https://github.com/hyraniemus/hamburg-techno/settings/secrets/actions"
echo "2. Klicke 'New repository secret'"
echo "3. Erstelle:"
echo "   - Name: NOTION_TOKEN"
echo "   - Value: $NOTION_TOKEN"
echo "4. Wiederhole für NOTION_DATABASE_ID"
echo ""

# Lokale Konfiguration speichern (nicht committen!)
CONFIG_FILE=".env.local"
cat > "$CONFIG_FILE" << EOF
# Notion-Konfiguration (nicht committen!)
NOTION_TOKEN=$NOTION_TOKEN
NOTION_DATABASE_ID=$NOTION_DB_ID
EOF

echo "✅ Setup abgeschlossen!"
echo "📝 Lokale Konfiguration gespeichert in: $CONFIG_FILE"
echo ""
echo "🚀 Test: python scripts/daily_news_summary.py"
