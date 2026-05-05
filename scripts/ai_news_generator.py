#!/usr/bin/env python3
"""
Daily AI Post-Production News Generator
Generates personalized news summaries for video editors specializing in AI post-production.
Publishes to Notion database daily at 06:30 CEST.
"""

import os
import json
from datetime import datetime
import anthropic
from notion_client import Client

# Configuration
NOTION_DATABASE_ID = os.getenv("NOTION_NEWS_DB_ID", "fa4ec63b-5c1b-443a-9dbd-fe8fe07fa330")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Initialize clients
notion = Client(auth=NOTION_TOKEN)
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

TOPICS = """
Kerninteressen für tägliche News:
- Avid Media Composer Updates & Bug Fixes
- DaVinci Resolve Features & AI-Grading
- Remotion neue Funktionen
- ComfyUI Improvements & Models
- Runway Gen-4 Updates
- Claude Code Integration in Workflows
- AI-Video-Generierung Tools
- Post-Production-Automatisierung
- Freelance-Chancen in AI-Editing
- Suno & Musikproduktion mit AI
- Film/TV-News & Dokumentar-Produktion

Ignorieren: Politik/Wirtschaft (außer Tech/Film-relevant)
"""

def generate_news_with_claude():
    """Generate daily news summary using Claude with web search."""

    prompt = f"""Du bist ein News-Kurator für Video-Editor und Post-Production-Spezialisten in Hamburg.

Heute ist der {datetime.now().strftime('%d. %B %Y')}.

KERNINTERESSEN:
{TOPICS}

Generiere eine personalisierte Tagesübersicht (max. 400 Wörter, auf Deutsch):

1. **Top 3 News-Highlights** (mit Links/Quellen)
   - Kurze Bullet-Points mit Relevanz für AI-Video-Workflows

2. **Tool-Updates & Tipps** (2-3 praktische Insights)
   - Konkrete Actionables für heute

3. **Karriere & Trends** (1-2 Chancen für AI-Post-Prod-Freelancer)
   - Hamburg/deutschsprachiger Markt fokussiert

4. **Aktion für heute** (1 personalierter Next-Step)
   - Was sollte der Editor heute testen/machen?

Recherchiere aktuelle Informationen:
- Reddit (r/Avid, r/davinciresolve, r/MachineLearning)
- Hacker News
- Tool-Blogs (Blackmagic, Anthropic, Runway, ComfyUI)
- X/Twitter (#AIVideo #PostProduction)

Formatiere als JSON mit keys: top_highlights, tool_updates, career_trends, action_today, sources
"""

    print("📡 Searching for latest AI Post-Production news...")

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    try:
        content = message.content[0].text
        # Try to extract JSON if wrapped in markdown
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()

        news_data = json.loads(content)
        return news_data
    except (json.JSONDecodeError, IndexError) as e:
        print(f"⚠️  Could not parse Claude response as JSON: {e}")
        # Fallback: return structured text
        return {
            "top_highlights": message.content[0].text,
            "tool_updates": "Siehe oben",
            "career_trends": "Siehe oben",
            "action_today": "Siehe oben",
            "sources": "Claude-Research"
        }

def publish_to_notion(news_data):
    """Publish news summary to Notion database."""

    today = datetime.now().strftime("%Y-%m-%d")

    properties = {
        "Datum": {
            "title": [
                {
                    "text": {
                        "content": f"🗞️ AI Post-Prod News – {today}"
                    }
                }
            ]
        },
        "Top 3 Highlights": {
            "rich_text": [
                {
                    "text": {
                        "content": news_data.get("top_highlights", "")
                    }
                }
            ]
        },
        "Tool-Updates & Tipps": {
            "rich_text": [
                {
                    "text": {
                        "content": news_data.get("tool_updates", "")
                    }
                }
            ]
        },
        "Karriere & Trends": {
            "rich_text": [
                {
                    "text": {
                        "content": news_data.get("career_trends", "")
                    }
                }
            ]
        },
        "Aktion für heute": {
            "rich_text": [
                {
                    "text": {
                        "content": news_data.get("action_today", "")
                    }
                }
            ]
        },
        "Quellen": {
            "rich_text": [
                {
                    "text": {
                        "content": news_data.get("sources", "Claude Research")
                    }
                }
            ]
        },
        "Status": {
            "select": {
                "name": "Veröffentlicht"
            }
        }
    }

    page = notion.pages.create(
        parent={"database_id": NOTION_DATABASE_ID},
        properties=properties
    )

    print(f"✅ News veröffentlicht: {page['url']}")
    return page

if __name__ == "__main__":
    try:
        news = generate_news_with_claude()
        publish_to_notion(news)
        print("🎉 Tägliche News-Zusammenfassung erstellt!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        raise
