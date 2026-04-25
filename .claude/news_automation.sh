#!/bin/bash
# Daily News Summary Automation (06:30 CEST)
# Add to crontab: 30 6 * * * /home/user/hamburg-techno/.claude/news_automation.sh
# Or use systemd timer for more control

cd /home/user/hamburg-techno

# Generate today's news
echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting daily news generation..."
python3 generate_daily_news.py

# Optional: Sync to Notion/Email (not implemented yet)
# python3 sync_to_notion.py
# python3 send_email.py

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Daily news generation complete."
