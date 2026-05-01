#!/bin/bash
# Setup daily news generator cron job at 06:30 CEST

# Make Python script executable
chmod +x /home/user/hamburg-techno/scripts/daily-ai-news.py

# Install/update cron entry for 06:30 CEST (04:30 UTC in summer, 05:30 in winter)
# Using 06:30 CEST (which is 04:30 UTC during CEST period)
CRON_TIME="30 4 * * *"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "daily-ai-news.py"; then
    echo "✓ Cron job already exists"
else
    # Add new cron job
    (crontab -l 2>/dev/null; echo "$CRON_TIME /home/user/hamburg-techno/scripts/daily-ai-news.py >> /home/user/hamburg-techno/.news-generator.log 2>&1") | crontab -
    echo "✓ Cron job added: $CRON_TIME"
fi

echo ""
echo "📅 Cron Configuration:"
echo "   Time: 06:30 CEST (30 4 * * *)"
echo "   Script: /home/user/hamburg-techno/scripts/daily-ai-news.py"
echo "   Log: /home/user/hamburg-techno/.news-generator.log"
echo ""
echo "View cron logs: tail -f /home/user/hamburg-techno/.news-generator.log"
