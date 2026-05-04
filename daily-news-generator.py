#!/usr/bin/env python3
"""
Tägliche AI Post-Prod News Generator für Notion
Generiert personalisierte News-Zusammenfassungen und postet sie in Notion
"""

import os
import json
from datetime import datetime
from anthropic import Anthropic
import requests

# API Keys (aus Environment Variables)
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = "d15c4ffa-fa29-4608-919d-37bfc1766392"  # AI Post-Prod Daily News
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Notion API Headers
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2024-08-06",
}

def generate_news_with_claude():
    """Generiert News-Zusammenfassung mit Claude API"""
    client = Anthropic()

    system_prompt = """Du bist ein spezialisierter News-Kurator für einen Video-Editor und Post-Production-Spezialist aus Hamburg, der zu AI-gestützter Video-Produktion wechselt.

Deine Aufgabe: Recherchiere aktuelle News (letzte 24h) zu seinen Kerninteressen und erstelle eine strukturierte tägliche Zusammenfassung.

KERNINTERESSEN:
- Tools: Avid Media Composer, DaVinci Resolve, Remotion, ComfyUI, Runway Gen-4, Claude Code-Integration
- AI: Video-Generierung, Post-Production-Automatisierung, Musik mit Suno
- Karriere: Freelance-Chancen in AI-Editing (Hamburg/Europa)
- Content: Film/TV-News, Dokumentar-Produktion
- IGNORIERE: Politik/Wirtschaft (nur wenn Tech/Film-relevant)

OUTPUT-FORMAT (JSON):
{
  "top_3_highlights": [
    {
      "title": "Headline",
      "source": "Source Name",
      "url": "https://...",
      "relevance": "Kurze Beschreibung für Workflow",
      "action": "Konkrete Aktion für den Editor"
    }
  ],
  "tool_updates": [
    {
      "tool": "Tool Name",
      "update": "Was ist neu/wichtig",
      "practical_tip": "Wie nutzt der Editor das?",
      "link": "https://..."
    }
  ],
  "career_trends": [
    {
      "trend": "Trend-Name",
      "context": "Warum relevant?",
      "opportunity": "Konkrete Chance für AI-Post-Prod-Freelancer"
    }
  ],
  "action_today": "1-2 konkrete Aufgaben für heute (max 100 Wörter)",
  "sources_used": ["Source 1", "Source 2", ...]
}

DEUTSCH, maximal 400 Wörter gesamt. Fokus auf HANDLUNGSORIENTIERTE Insights mit konkreten Links."""

    user_prompt = f"""Generiere die tägliche News-Zusammenfassung für {datetime.now().strftime('%d. %B %Y')}.

Recherchiere aktuelle Quellen (letzte 24h):
- Reddit: r/Avid, r/davinciresolve, r/MachineLearning
- Hacker News
- Tool-Blogs: Blackmagic Design, Anthropic, Runway, ComfyUI
- X/Twitter: #AIVideo #PostProduction #VideoEditing
- GitHub Trends

Fokus auf NEWS mit konkreten Links und Workflow-Relevanz."""

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2000,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.content[0].text

def parse_news_content(content: str) -> dict:
    """Parsed die Claude-Response in strukturierte News"""
    try:
        # Versuche JSON zu extrahieren
        json_start = content.find("{")
        json_end = content.rfind("}") + 1
        if json_start >= 0 and json_end > json_start:
            json_str = content[json_start:json_end]
            return json.loads(json_str)
    except json.JSONDecodeError:
        pass

    # Fallback: Strukturiere aus Text
    return {
        "raw_content": content,
        "top_3_highlights": [],
        "tool_updates": [],
        "career_trends": [],
        "action_today": "Siehe rohes Content"
    }

def format_notion_content(news: dict) -> str:
    """Formatiert News für Notion (Markdown)"""
    content = ""

    if news.get("top_3_highlights"):
        content += "## 🔥 Top 3 News-Highlights\n\n"
        for i, hl in enumerate(news["top_3_highlights"], 1):
            content += f"**{i}. {hl.get('title', 'Update')}**\n"
            if hl.get('source'):
                content += f"[{hl['source']}]({hl.get('url', '#')})\n"
            if hl.get('relevance'):
                content += f"- ✅ {hl['relevance']}\n"
            if hl.get('action'):
                content += f"- 🎯 {hl['action']}\n"
            content += "\n"

    if news.get("tool_updates"):
        content += "## 🛠️ Tool-Updates & Praktische Tipps\n\n"
        for update in news["tool_updates"]:
            content += f"**{update.get('tool', 'Update')}**\n"
            content += f"- {update.get('update', '')}\n"
            content += f"- 💡 {update.get('practical_tip', '')}\n"
            if update.get('link'):
                content += f"- [Link]({update['link']})\n"
            content += "\n"

    if news.get("career_trends"):
        content += "## 💼 Karriere & Trends\n\n"
        for trend in news["career_trends"]:
            content += f"**{trend.get('trend', 'Trend')}**\n"
            content += f"- {trend.get('context', '')}\n"
            content += f"- 🎯 {trend.get('opportunity', '')}\n"
            content += "\n"

    if news.get("action_today"):
        content += "## ⚡ Aktion für Heute\n\n"
        content += news["action_today"]

    if news.get("sources_used"):
        content += "\n\n## 📖 Quellen\n\n"
        for source in news["sources_used"]:
            content += f"- {source}\n"

    if news.get("raw_content") and not news.get("top_3_highlights"):
        content = news["raw_content"]

    return content

def create_notion_page(news_content: str, formatted_content: str) -> bool:
    """Erstellt neue Seite in Notion-Datenbank"""
    today = datetime.now().strftime("%d. %B %Y")

    page_data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "Datum": {
                "title": [
                    {
                        "text": {
                            "content": f"{today} – AI Video Edition"
                        }
                    }
                ]
            },
            "Status": {
                "select": {
                    "name": "Wichtig"
                }
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": formatted_content
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers=NOTION_HEADERS,
        json=page_data
    )

    if response.status_code == 200:
        print(f"✅ News-Seite erstellt: {today}")
        return True
    else:
        print(f"❌ Fehler beim Erstellen der Notion-Seite: {response.status_code}")
        print(response.text)
        return False

def main():
    """Hauptfunktion"""
    print(f"🚀 Generiere tägliche News für {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}...")

    # Check API Keys
    if not NOTION_TOKEN or not ANTHROPIC_API_KEY:
        print("❌ Fehler: NOTION_TOKEN oder ANTHROPIC_API_KEY nicht gesetzt")
        print("Setze Environment Variables:")
        print("  export NOTION_TOKEN='your-token'")
        print("  export ANTHROPIC_API_KEY='your-key'")
        return False

    # Generate news
    try:
        news_content = generate_news_with_claude()
        parsed_news = parse_news_content(news_content)
        formatted_content = format_notion_content(parsed_news)

        # Create Notion page
        success = create_notion_page(news_content, formatted_content)
        return success
    except Exception as e:
        print(f"❌ Fehler: {e}")
        return False

if __name__ == "__main__":
    main()
