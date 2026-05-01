#!/bin/bash
# Initialize AI Post-Production Daily News Automation

set -e

echo "🎥 Setting up Daily AI Post-Production News Automation..."
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}📂 Project Root: $PROJECT_ROOT${NC}"
echo -e "${BLUE}📂 Scripts Dir: $SCRIPT_DIR${NC}"
echo ""

# 1. Create scripts directory if needed
mkdir -p "$SCRIPT_DIR"
echo -e "${GREEN}✓ Scripts directory ready${NC}"

# 2. Make scripts executable
chmod +x "$SCRIPT_DIR/daily-ai-news.py"
chmod +x "$SCRIPT_DIR/setup-cron.sh"
echo -e "${GREEN}✓ Scripts made executable${NC}"

# 3. Setup cron job (if available)
echo ""
echo -e "${YELLOW}⚙️  Configuring Cron Job...${NC}"

CRON_TIME="30 4 * * *"  # 06:30 CEST (04:30 UTC)
CRON_CMD="$SCRIPT_DIR/daily-ai-news.py >> $PROJECT_ROOT/.news-generator.log 2>&1"

if command -v crontab &> /dev/null; then
    # Check if already installed
    if crontab -l 2>/dev/null | grep -q "daily-ai-news.py"; then
        echo -e "${YELLOW}⚠️  Cron job already exists, skipping...${NC}"
    else
        # Add cron job
        (crontab -l 2>/dev/null || true; echo "$CRON_TIME $CRON_CMD") | crontab -
        echo -e "${GREEN}✓ Cron job installed${NC}"
        echo -e "   Time: Daily @ 06:30 CEST (04:30 UTC)"
        echo -e "   Job: $CRON_CMD"
    fi
else
    echo -e "${YELLOW}⚠️  crontab not available on this system${NC}"
    echo "   You can use Claude Code /loop command instead:"
    echo "   /loop 24h python3 $SCRIPT_DIR/daily-ai-news.py"
fi

# 4. Create initial log file
touch "$PROJECT_ROOT/.news-generator.log"
echo -e "${GREEN}✓ Log file created${NC}"

# 5. Display summary
echo ""
echo -e "${GREEN}════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BLUE}📋 Next Steps:${NC}"
echo "   1. View setup README:"
echo "      cat $PROJECT_ROOT/NEWS-AUTOMATION.md"
echo ""
echo "   2. Test manually:"
echo "      python3 $SCRIPT_DIR/daily-ai-news.py"
echo ""
echo "   3. Check scheduled runs:"
echo "      crontab -l"
echo ""
echo "   4. Monitor logs:"
echo "      tail -f $PROJECT_ROOT/.news-generator.log"
echo ""
echo -e "${BLUE}🌐 Notion Database:${NC}"
echo "   https://app.notion.com/p/2aa41b373890430d967c92d32f8f20dc"
echo ""
echo -e "${BLUE}📅 Schedule:${NC}"
echo "   Runs daily @ 06:30 CEST (04:30 UTC during CEST)"
echo "   Next run will be tomorrow morning"
echo ""
