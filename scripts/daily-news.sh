#!/bin/bash
# Daily AI Post-Production News Fetcher
# Runs at 06:30 CEST via cron

set -e

NOTION_TOKEN="${NOTION_TOKEN}"
DATABASE_ID="e59e916c-60a2-4123-817d-2838ca955c4d"
WEBHOOK_URL="${DISCORD_WEBHOOK_URL}"  # Optional: Discord notification

# Fetch latest news from key sources
get_davinci_news() {
  curl -s "https://www.blackmagicdesign.com/products/davinciresolve/whatsnew" | \
    grep -oP '(?<=<h2>)[^<]+' | head -3
}

get_runway_news() {
  curl -s "https://runwayml.com/changelog" | \
    grep -oP '(?<=<li>)[^<]+' | head -2
}

get_remotion_news() {
  curl -s "https://www.remotion.dev/" | \
    grep -i "ai\|claude\|update" | head -2
}

# Format for Notion
TIMESTAMP=$(date +"%Y-%m-%d")
TITLE="${TIMESTAMP} - AI Post-Production Daily"

# Create Notion page
curl -X POST \
  "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer ${NOTION_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "parent": { "database_id": "${DATABASE_ID}" },
  "properties": {
    "Name": { "title": [{ "text": { "content": "${TITLE}" } }] },
    "date:Datum:start": { "date": { "start": "${TIMESTAMP}" } },
    "Status": { "select": { "name": "Veröffentlicht" } },
    "Top 3 Highlights": { "rich_text": [{ "text": { "content": "$(get_davinci_news)\\n$(get_runway_news)" } }] },
    "Action for Today": { "rich_text": [{ "text": { "content": "✅ Teste DaVinci 21 AI IntelliSearch\\n✅ Erkunde ComfyUI LTX Video\\n✅ Remotion + Claude Demo-Video" } }] }
  }
}
EOF

echo "✅ News für $(date +%d.%m.%Y) erstellt"
