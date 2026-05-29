#!/usr/bin/env python3
"""
Tägliche AI-Post-Prod News für Notion
Recherchiert aktuelle News und aktualisiert Notion-Datenbank
"""

import os
import json
from datetime import datetime
import requests
from anthropic import Anthropic

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

NOTION_API_URL = "https://api.notion.com/v1"

def search_news():
    """Recherchiere aktuelle News zu deinen Interessen"""
    client = Anthropic()

    # News-Quellen-Recherche
    sources = [
        "Avid Media Composer AI updates May 2026",
        "DaVinci Resolve 21 AI tools color grading",
        "Runway Gen-4 ComfyUI integration",
        "Claude Code post production workflows",
        "AI video editing freelance opportunities",
        "Suno music generation May 2026",
        "Remotion web video framework updates",
        "ComfyUI latest features"
    ]

    # Prompt für Claude, der die strukturierte Zusammenfassung erstellt
    research_prompt = f"""
Du recherchierst tägliche News für einen Hamburg-basierten Video-Editor, der zu AI-gestützter Video-Produktion wechselt.

Interessen:
- Avid Media Composer (Bug Fixes, neue Tools, AI-Integration)
- DaVinci Resolve (AI-Features, Color Grading, Updates)
- ComfyUI, Runway Gen-4, Remotion
- Claude Code-Integration in Video-Workflows
- AI-Video-Generierung & Automatisierung
- Freelance-Chancen in AI-Editing
- Suno für Musikproduktion

Erstelle eine strukturierte Zusammenfassung (max. 350 Wörter, auf Deutsch):

1. **Top 3 News-Highlights** (kurze Bullet-Points mit Quelle/Link)
2. **Tool-Updates & Tipps** (2-3 praktische Insights)
3. **Karriere & Trends** (1-2 Chancen für Freelancer)
4. **Aktion für heute** (1 personalisierter Next-Step)

Format: JSON mit den Keys: highlights, tools, career, action_today

Heute ist: {datetime.now().strftime('%d. %B %Y')}
"""

    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1500,
        messages=[
            {"role": "user", "content": research_prompt}
        ]
    )

    return message.content[0].text


def create_notion_page(news_content):
    """Erstelle eine neue Seite in der Notion-Datenbank"""

    today = datetime.now().strftime("%d. %B %Y")

    # Parse die News (vereinfacht - in Produktion robuster parsen)
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Datum": {
                "title": [
                    {
                        "text": {
                            "content": f"{today} – AI Video Production News"
                        }
                    }
                ]
            },
            "Status": {
                "select": {
                    "name": "Veröffentlicht"
                }
            },
            "Top 3 Highlights": {
                "rich_text": [
                    {
                        "text": {
                            "content": news_content[:200]  # Preview
                        }
                    }
                ]
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
                                "content": news_content
                            }
                        }
                    ]
                }
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    response = requests.post(
        f"{NOTION_API_URL}/pages",
        json=payload,
        headers=headers
    )

    if response.status_code == 200:
        print(f"✅ News-Seite erstellt: {response.json().get('id')}")
        return response.json()
    else:
        print(f"❌ Fehler beim Erstellen der Seite: {response.text}")
        return None


if __name__ == "__main__":
    print("🔄 Recherchiere tägliche AI-Post-Prod News...")

    news = search_news()
    print(f"📝 News generiert ({len(news)} Zeichen)")

    result = create_notion_page(news)

    if result:
        print("✅ Tägliche News aktualisiert!")
    else:
        print("❌ News-Update fehlgeschlagen")
        exit(1)
