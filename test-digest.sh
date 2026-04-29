#!/bin/bash

# Test-Skript für News-Digest System
# Nutze: bash test-digest.sh

echo "🧪 News-Digest System Test"
echo "=========================="
echo ""

# Check dependencies
echo "✅ Checking dependencies..."
npm list anthropic dotenv node-cron nodemailer > /dev/null 2>&1 && echo "   ✓ All dependencies installed" || echo "   ✗ Missing dependencies!"

# Check .env
echo ""
echo "✅ Checking .env configuration..."
if [ -f .env ]; then
    echo "   ✓ .env file exists"
    if grep -q "ANTHROPIC_API_KEY=" .env; then
        if grep "ANTHROPIC_API_KEY=" .env | grep -q "sk-"; then
            echo "   ✓ ANTHROPIC_API_KEY configured"
        else
            echo "   ⚠️  ANTHROPIC_API_KEY not set properly"
        fi
    fi
else
    echo "   ✗ .env file missing - run: cp .env.example .env"
fi

# Check TypeScript
echo ""
echo "✅ Checking TypeScript..."
npx tsc --noEmit news-digest.ts > /dev/null 2>&1 && echo "   ✓ TypeScript syntax valid" || echo "   ✗ TypeScript errors found"

# Show commands
echo ""
echo "📝 Available commands:"
echo "   npm run digest:now      - Generate digest now"
echo "   npm run digest:schedule - Start daily scheduler (06:30 CEST)"
echo "   npm run digest -- --now - Direct execution"
echo ""

# Optionally run
echo "Would you like to generate a test digest now? (requires valid ANTHROPIC_API_KEY)"
echo "Run: npm run digest:now"
echo ""
