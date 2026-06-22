#!/usr/bin/env python3
"""
Notion Database Setup Helper
Creates a new Notion database for AI News summaries if it doesn't exist.
Requires: NOTION_API_KEY environment variable
"""

import os
import sys
import json

def main():
    """Setup Notion database for daily news"""

    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        print("❌ Error: NOTION_API_KEY not set")
        print("\nTo set it up:")
        print("1. Go to notion.so")
        print("2. Settings & Members → Integrations → Create integration")
        print("3. Name it 'Daily News Generator'")
        print("4. Copy the token")
        print("5. Set environment variable: export NOTION_API_KEY='your-token'")
        sys.exit(1)

    print("=" * 60)
    print("🗄️  Notion Database Setup Guide")
    print("=" * 60)
    print()

    print("Step 1: Create Notion Database")
    print("-" * 60)
    print("1.1 Go to https://notion.so")
    print("1.2 Create new page or database titled 'AI News Daily'")
    print("1.3 Use template or create manual with these properties:")
    print()
    print("    Property Name       | Type           | Required")
    print("    ────────────────────┼────────────────┼──────────")
    print("    Title               | Title          | Yes")
    print("    Date                | Date           | Yes")
    print("    Category            | Select         | Yes")
    print("                        | Options:")
    print("                        |  • Avid")
    print("                        |  • Resolve")
    print("                        |  • ComfyUI")
    print("                        |  • Runway")
    print("                        |  • Remotion")
    print("                        |  • Suno")
    print("                        |  • Claude Code")
    print("                        |  • Careers")
    print("    Content             | Text (Long)    | Yes")
    print("    Sources             | URL            | No")
    print("    Tags                | Multi-select   | No")
    print()

    print("Step 2: Create Integration")
    print("-" * 60)
    print("2.1 Go to Notion settings (gear icon)")
    print("2.2 Select 'Integrations' from left sidebar")
    print("2.3 Click 'Create new integration'")
    print("2.4 Name: 'Daily News Generator'")
    print("2.5 Click 'Show API token' and copy it")
    print()

    print("Step 3: Share Database with Integration")
    print("-" * 60)
    print("3.1 Open your 'AI News Daily' database")
    print("3.2 Click the share button (top right)")
    print("3.3 Search for 'Daily News Generator' integration")
    print("3.4 Give it 'Editor' access")
    print()

    print("Step 4: Get Database URL")
    print("-" * 60)
    print("4.1 Open the database")
    print("4.2 Copy the URL from your browser (it looks like):")
    print("    https://www.notion.so/workspace/AI-News-Daily-abc123def456")
    print()

    print("Step 5: Set Environment Variables")
    print("-" * 60)
    print("5.1 Add to ~/.bashrc or ~/.zshrc:")
    print()
    print("    export NOTION_API_KEY='your-integration-token'")
    print("    export NOTION_NEWS_DB_URL='https://www.notion.so/workspace/your-db-url'")
    print()
    print("5.2 Then reload: source ~/.bashrc")
    print()

    print("Step 6: Configure GitHub (Optional)")
    print("-" * 60)
    print("6.1 Go to GitHub: Your Repo → Settings → Secrets and variables → Actions")
    print("6.2 Add new secret: NOTION_API_KEY")
    print("6.3 Add new secret: NOTION_NEWS_DB_URL")
    print()

    print("Step 7: Test the Setup")
    print("-" * 60)
    print("7.1 Run: python3 ai-news-generator.py")
    print("7.2 Check if markdown file is created in news-archive/")
    print("7.3 Manually post one summary to Notion to test")
    print()

    print("=" * 60)
    print("✅ When complete, your daily news will be posted to Notion at 06:30 CEST")
    print("=" * 60)

if __name__ == "__main__":
    main()
