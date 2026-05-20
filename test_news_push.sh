#!/bin/bash
# Test-Script: Erste News-Beispiel zu Notion pushen

echo "🧪 Teste News-Aggregation..."

# 1. Notion API-Key prüfen
if [ -z "$NOTION_API_KEY" ]; then
    echo "⚠️  NOTION_API_KEY nicht gesetzt!"
    echo "Setze die Variable: export NOTION_API_KEY='your-token'"
    exit 1
fi

echo "✅ NOTION_API_KEY gefunden"

# 2. Python-Dependencies installieren
echo "📦 Installiere Dependencies..."
pip install -q -r requirements_news.txt

# 3. Script ausführen
echo "🚀 Starte News-Aggregation..."
python news_aggregator.py

echo ""
echo "✅ Test komplett!"
echo "👉 Gehe zu Notion und überprüfe deine 'AI Post-Production Daily News' Datenbank"
