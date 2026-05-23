#!/usr/bin/env python3
"""
Daily AI-Post-Production News Summary Generator
Researches current news and updates Notion database with daily digest
Scheduled: Daily at 06:30 CEST via GitHub Actions
"""

import os
import sys
import json
from datetime import datetime
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

NEWS_SOURCES = {
    "davinci_resolve": "DaVinci Resolve AI update 2026",
    "avid_media": "Avid Media Composer bug fixes updates May 2026",
    "comfyui": "ComfyUI AI video generation May 2026",
    "runway": "Runway Gen-4 video AI updates",
    "freelance": "AI video post production freelance opportunities 2026",
    "claude_api": "Claude API video production automation integration",
}

def generate_news_summary():
    """Generate daily news summary using Claude API with multi-turn conversation"""

    conversation_history = []

    # Step 1: Ask Claude to research and organize news
    research_prompt = """Du bist ein Spezialist für AI-Video-Produktion und Post-Production News.

Recherchiere und erstelle eine tägliche News-Zusammenfassung für einen Video-Editor in Hamburg, der zu AI-gestützter Post-Production wechselt.

Fokusiere auf:
- Avid Media Composer Updates/Bug Fixes
- DaVinci Resolve AI-Tools
- ComfyUI & Runway Gen-4 Updates
- Claude Code Integration in Video-Workflows
- AI-Video-Generierung & Post-Production-Automatisierung
- Freelance-Chancen in AI-Editing
- Suno für Musikproduktion
- Film/TV-News relevant für Tech/AI

Strukturiere die Antwort in folgendem Format (max. 400 Wörter):
1. **Top 3 News-Highlights** (mit Links/Quellen)
2. **Tool-Updates & Tipps** (2-3 praktische Insights)
3. **Karriere/Trends** (1-2 Chancen für AI-Post-Prod-Freelancer)
4. **Aktion für heute** (1 personalisierter Next-Step)

Antworte auf Deutsch. Sei konkret und handlungsorientiert.

Heute ist: {today}""".format(today=datetime.now().strftime("%d. %B %Y"))

    conversation_history.append({
        "role": "user",
        "content": research_prompt
    })

    # Get initial response
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2000,
        messages=conversation_history
    )

    news_summary = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": news_summary
    })

    # Step 2: Ask Claude to add links and citations
    refinement_prompt = """Perfekt! Jetzt bitte:
1. Füge konkrete URLs/Links zu allen Tools und Quellen hinzu (Reddit, Hacker News, Tool-Blogs, Twitter-Hashtags)
2. Formatiere als Markdown mit Überschriften, Bullets und Links
3. Füge am Ende eine "Quellen & Weiterführende Links" Sektion ein

Antworte mit der kompletten, verfeinerten Version."""

    conversation_history.append({
        "role": "user",
        "content": refinement_prompt
    })

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2500,
        messages=conversation_history
    )

    refined_summary = response.content[0].text

    return refined_summary

def format_notion_content(summary: str) -> tuple:
    """Format summary for Notion page"""
    today = datetime.now().strftime("%d. %B %Y")
    title = f"📺 AI-Post-Prod News – {today}"

    return title, summary

def create_notion_page(title: str, content: str) -> dict:
    """Create new Notion page (integration with Notion API via environment variables)"""
    # This would be implemented with Notion API
    # For now, return metadata for manual creation or GitHub workflow

    return {
        "title": title,
        "content": content,
        "date": datetime.now().isoformat(),
        "status": "ready_for_notion"
    }

def main():
    """Main function"""
    print("🚀 Starting Daily AI-Post-Prod News Generation...")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S CEST')}")

    try:
        # Generate news summary
        print("📰 Generating news summary with Claude...")
        summary = generate_news_summary()

        # Format for Notion
        title, content = format_notion_content(summary)

        # Prepare page data
        page_data = create_notion_page(title, content)

        # Save to output file for GitHub Actions / manual processing
        output_path = "/tmp/daily-news-output.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(page_data, f, ensure_ascii=False, indent=2)

        print(f"✅ News summary generated successfully!")
        print(f"📄 Output saved to: {output_path}")
        print(f"\n📌 Title: {title}")
        print(f"📊 Content length: {len(content)} characters")

        return 0

    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
