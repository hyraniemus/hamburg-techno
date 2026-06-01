#!/usr/bin/env python3
"""
AI Post-Prod Daily News Generator
Erstellt täglich um 06:30 CEST eine personalisierte News-Zusammenfassung
für Video-Editor mit AI-Fokus in Notion.
"""

import os
import json
import datetime
from typing import Optional
import requests
from anthropic import Anthropic

# Environment variables
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID", "941d6c5a-b60d-44c1-a39e-8f947bfa0845")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Initialize Anthropic client
client = Anthropic()

SEARCH_QUERIES = [
    "Avid Media Composer updates bug fixes 2025 2026 latest news",
    "DaVinci Resolve AI features color grading updates 2026",
    "Runway Gen-4 AI video generation latest features",
    "ComfyUI Remotion video AI tools automation 2026",
    "Claude Code video workflow automation integration AI",
    "Post-production AI automation freelance opportunities 2026",
    "Suno AI music generation latest features 2026",
]

NEWS_STRUCTURE_PROMPT = """Du bist ein spezialisierter News-Kurator für einen Video-Editor & Post-Production-Spezialist aus Hamburg,
der zu AI-gestützter Video-Produktion übergeht.

Erstelle basierend auf den recherchierten News eine tägliche Zusammenfassung mit dieser EXAKTEN Struktur (max. 400 Wörter, auf Deutsch):

## STRUKTUR:

### Top 3 News-Highlights
- Bullet-Points mit Quelle/Link
- Relevanz für den Workflow erklärt
- Format: "**1. 🎬 [Tool]: [News]**\n• Detail1\n• Detail2\n📌 Relevanz: ...\n🔗 [Link](url)"

### Tool-Updates & Tipps
- 2-3 praktische Insights
- Code-Snippets oder Workflow-Tipps wo relevant
- Format: "🛠️ **[Titel]**\n[Erklärung]\n🔗 [Link](url)"

### Karriere & Trends
- 1-2 Chancen für AI-Post-Prod-Freelancer
- Fokus: Hamburg/Remote, Startups, Skill-Positionierung
- Format: "💼 **[Trend]**\n✅ [Chance]\n💡 [Actionable Insight]"

### Action für Heute
- 1 personalisierter Next-Step (z.B. "Teste dieses Runway-Model")
- Zeitplan (Morgens/Mittags/Abends)
- Format: "🎯 **Dein 24h Action-Plan:**\n1. **[Aktion]**\n..."

## INHALTS-FOKUS:

### Hoch Priorität:
- Avid Media Composer Bug Fixes & neue Tools
- DaVinci Resolve AI-Features (Color Grading, Editing)
- Runway Gen-4/4.5 Updates
- ComfyUI, Remotion, Claude Code Integration
- Automation für Post-Production

### Mittel Priorität:
- AI-Video-Generierung News
- Suno & Musikproduktion
- Freelance-Chancen

### Ignorieren:
- Politik/Wirtschaft (außer Tech/Film-relevant)
- Unbekannte Tools
- Generische AI-News ohne praktischen Bezug

## WICHTIG:
- Schreibe HANDLUNGSORIENTIERT (nicht theoretisch)
- Verlink ALLE Quellen
- Deutsche Sprache, aber Tech-Begriffe auf Englisch (z.B. "DaVinci Resolve", nicht "Davinci-Auflöser")
- Emojis für Struktur nutzen, aber sparsam
- Personalisiere: "Für Dich als Post-Producer mit Avid-Hintergrund..."
"""

def search_news() -> str:
    """Recherchiere aktuelle News über Web-APIs."""
    print("[📡] Searching for latest news...")

    news_articles = []

    for query in SEARCH_QUERIES:
        try:
            # Verwende DuckDuckGo oder ähnliche kostenlose API
            # Falls keine API verfügbar, sammeln wir nur relevante Hinweise
            url = f"https://api.duckduckgo.com/?q={query}&format=json"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                for result in data.get("Results", [])[:3]:  # Top 3 pro Query
                    news_articles.append({
                        "query": query,
                        "title": result.get("Title", ""),
                        "url": result.get("FirstURL", ""),
                        "snippet": result.get("Text", "")
                    })
        except Exception as e:
            print(f"[⚠️] Search error for '{query}': {e}")
            continue

    return json.dumps(news_articles[:20], indent=2, ensure_ascii=False)  # Top 20 results

def generate_summary(news_data: str) -> dict:
    """Generiere AI-gestützte News-Zusammenfassung mit Claude."""
    print("[🤖] Generating AI-powered summary with Claude...")

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": f"""{NEWS_STRUCTURE_PROMPT}

## RECHERCHIERTE NEWS (JSON):
{news_data}

Bitte erstelle jetzt die tägliche News-Zusammenfassung basierend auf den Daten oben.
Fokus: Praktisch, handlungsorientiert, für einen Post-Production-Spezialist relevant.

Format: JSON mit Keys:
- "top_headlines": string (mit Markdown)
- "tool_updates": string (mit Markdown)
- "career_trends": string (mit Markdown)
- "action_today": string (mit Markdown)
- "sources": string (mit allen Links)
- "categories": array of strings (Avid, DaVinci Resolve, AI Tools, Automatisierung, Freelance)

Antworte NUR mit gültigem JSON, keine zusätzlichen Erklärungen."""
            }
        ]
    )

    try:
        summary_json = json.loads(response.content[0].text)
        return summary_json
    except json.JSONDecodeError:
        print("[❌] Failed to parse Claude response as JSON")
        print(f"Raw response: {response.content[0].text}")
        return {
            "top_headlines": response.content[0].text,
            "tool_updates": "",
            "career_trends": "",
            "action_today": "",
            "sources": "",
            "categories": ["AI Tools"]
        }

def create_notion_page(summary: dict) -> bool:
    """Erstelle neue Notion-Seite mit der Zusammenfassung."""
    print("[📝] Creating Notion page...")

    today = datetime.datetime.now().strftime("%d. %B %Y")
    page_title = f"📰 {today} – AI-Video News für Post-Producer"

    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # Parse categories
    categories = summary.get("categories", ["AI Tools"])

    payload = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "Datum": {"title": [{"text": {"content": page_title}}]},
            "Top Headlines": {"rich_text": [{"text": {"content": summary.get("top_headlines", "")}}]},
            "Tool Updates": {"rich_text": [{"text": {"content": summary.get("tool_updates", "")}}]},
            "Karriere & Trends": {"rich_text": [{"text": {"content": summary.get("career_trends", "")}}]},
            "Action für Heute": {"rich_text": [{"text": {"content": summary.get("action_today", "")}}]},
            "Quellen": {"rich_text": [{"text": {"content": summary.get("sources", "")}}]},
            "Kategorie": {"multi_select": [{"name": cat} for cat in categories]},
            "Priorität": {"select": {"name": "🔴 High"}}
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)

        if response.status_code == 200:
            page_data = response.json()
            page_url = page_data.get("url", "")
            print(f"[✅] Notion page created: {page_url}")
            return True
        else:
            print(f"[❌] Notion API error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"[❌] Failed to create Notion page: {e}")
        return False

def main():
    """Hauptfunktion."""
    print("[🚀] Starting AI Post-Prod Daily News Generator")
    print(f"[⏰] Generated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S CEST')}")

    if not NOTION_API_KEY:
        print("[❌] NOTION_API_KEY not set in environment variables")
        return False

    if not ANTHROPIC_API_KEY:
        print("[❌] ANTHROPIC_API_KEY not set in environment variables")
        return False

    # Step 1: Search for news
    news_data = search_news()

    # Step 2: Generate summary with Claude
    summary = generate_summary(news_data)

    # Step 3: Create Notion page
    success = create_notion_page(summary)

    if success:
        print("[🎉] Daily news generation completed successfully!")
        return True
    else:
        print("[⚠️] Daily news generation completed with errors")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
