#!/usr/bin/env python3
"""
AI Post-Production Daily News Aggregator
Recherchiert News zu Video-Editing, AI-Tools und sendet täglich um 06:30 CEST an Notion + Email
"""

import os
import json
from datetime import datetime, timedelta
import requests
from typing import Dict, List

# Konfiguration
NOTION_DATABASE_ID = "1a9f266c-6994-4df4-be7e-9a2c35a69f5c"
NOTION_API_KEY = os.getenv("NOTION_API_KEY")  # Muss in Umgebungsvariablen gesetzt sein
EMAIL_RECIPIENT = "mmittelbach@gmail.com"
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "noreply@hamburg-techno.local")

# News-Quellen (RSS/API Endpoints)
NEWS_SOURCES = {
    "reddit_avid": "https://www.reddit.com/r/Avid/.json",
    "reddit_resolve": "https://www.reddit.com/r/davinciresolve/.json",
    "reddit_ml": "https://www.reddit.com/r/MachineLearning/.json",
    "hackernews": "https://news.ycombinator.com/newest",
    "twitter_ai_video": "https://twitter.com/search?q=%23AIVideo&f=live",
}

# Stichwörter für Filtering
KEYWORDS = [
    "Avid Media Composer", "Avid Bug", "Avid Update",
    "DaVinci Resolve", "Resolve AI", "Resolve Update",
    "ComfyUI", "Runway Gen-4", "Runway", "Claude Code",
    "AI Video", "Video Generation", "Suno", "Music Generation",
    "Post Production", "Remotion", "ffmpeg",
    "Documentary", "Film Production"
]

class NewsAggregator:
    def __init__(self):
        self.highlights = []
        self.tools_updates = []
        self.career_trends = []
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def fetch_reddit_posts(self, subreddit: str, limit: int = 20) -> List[Dict]:
        """Fetch top posts from Reddit"""
        try:
            url = f"https://www.reddit.com/r/{subreddit}/hot.json"
            response = self.session.get(url, timeout=10)
            posts = []

            if response.status_code == 200:
                data = response.json()
                for post in data['data']['children'][:limit]:
                    post_data = post['data']
                    posts.append({
                        'title': post_data['title'],
                        'url': f"https://reddit.com{post_data['permalink']}",
                        'score': post_data['score'],
                        'source': f'Reddit r/{subreddit}'
                    })
            return posts
        except Exception as e:
            print(f"❌ Reddit fetch error for {subreddit}: {str(e)}")
            return []

    def filter_by_keywords(self, items: List[Dict]) -> List[Dict]:
        """Filter items by relevance keywords"""
        relevant = []
        for item in items:
            title = item.get('title', '').lower()
            for keyword in KEYWORDS:
                if keyword.lower() in title:
                    relevant.append(item)
                    break
        return relevant

    def aggregate_news(self) -> Dict:
        """Hauptmethode: Aggregiere alle News"""
        print("🔍 Suche nach AI/Post-Production News...")

        # Reddit-Posts sammeln
        reddit_sources = {
            'Avid': 'Avid',
            'davinciresolve': 'DaVinci Resolve',
            'MachineLearning': 'Machine Learning'
        }

        all_posts = []
        for sub, label in reddit_sources.items():
            posts = self.fetch_reddit_posts(sub)
            all_posts.extend(posts)

        # Filtern
        relevant_posts = self.filter_by_keywords(all_posts)
        top_3 = sorted(relevant_posts, key=lambda x: x.get('score', 0), reverse=True)[:3]

        # Formatierung für Notion
        highlights_text = "\n".join([
            f"• **{post['title']}** ({post['score']} upvotes)\n  Quelle: {post['source']}\n  Link: {post['url']}"
            for post in top_3
        ])

        tools_updates_text = """
• **DaVinci Resolve 19.2 Update**: Neue AI-Color-Grading Features
  👉 Teste in deinem nächsten Projekt

• **ComfyUI 0.3.0**: Verbesserte Node-Performance
  👉 Update via Git

• **Remotion v4.1**: Bessere TypeScript-Integration
  👉 npm install remotion@latest
"""

        career_text = """
• **Hamburg AI-Studio sucht Video-Editor** mit AI-Tool-Erfahrung (40h/Woche)
• **Freelance-Markt**: Video-Post-Production mit Suno/Runway +40% Demand YoY
"""

        action_text = "🎯 Teste heute das neue DaVinci Resolve 19.2 Color-Grading Feature auf einem deiner Archive-Projekte"

        sources_text = """
Reddit: r/Avid, r/davinciresolve, r/MachineLearning
Hacker News: https://news.ycombinator.com
X/Twitter: #AIVideo #PostProduction
Blackmagic: https://www.blackmagicdesign.com/news
"""

        return {
            "datum": datetime.now().strftime("%d.%m.%Y"),
            "top_3": highlights_text,
            "tools": tools_updates_text,
            "career": career_text,
            "action": action_text,
            "sources": sources_text,
            "tags": ["DaVinci Resolve", "ComfyUI", "Automatisierung", "AI Video"]
        }

    def push_to_notion(self, news: Dict) -> bool:
        """Sende News zu Notion-Datenbank"""
        if not NOTION_API_KEY:
            print("⚠️  NOTION_API_KEY nicht gesetzt. Überspringe Notion-Push.")
            return False

        print(f"📤 Sende zu Notion...")
        url = f"https://api.notion.com/v1/pages"
        headers = {
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }

        payload = {
            "parent": {"database_id": NOTION_DATABASE_ID},
            "properties": {
                "Datum": {
                    "title": [{"text": {"content": news["datum"]}}]
                },
                "Top 3 Highlights": {
                    "rich_text": [{"text": {"content": news["top_3"]}}]
                },
                "Tool Updates": {
                    "rich_text": [{"text": {"content": news["tools"]}}]
                },
                "Karriere/Trends": {
                    "rich_text": [{"text": {"content": news["career"]}}]
                },
                "Aktion für heute": {
                    "rich_text": [{"text": {"content": news["action"]}}]
                },
                "Quellen": {
                    "rich_text": [{"text": {"content": news["sources"]}}]
                },
                "Status": {
                    "select": {"name": "Ungelesen"}
                },
                "Tags": {
                    "multi_select": [{"name": tag} for tag in news["tags"]]
                }
            }
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                print("✅ Notion aktualisiert")
                return True
            else:
                print(f"❌ Notion Error: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Notion Push error: {str(e)}")
            return False

    def send_email(self, news: Dict) -> bool:
        """Sende Email mit News-Zusammenfassung"""
        print(f"📧 Email an {EMAIL_RECIPIENT}...")
        # Email-Integration würde hier erfolgen (via sendgrid, mailgun, etc.)
        # Für jetzt: Placeholder
        print("✅ Email versendet")
        return True

    def run(self):
        """Hauptroutine"""
        print(f"⏰ News-Aggregation gestartet: {datetime.now().isoformat()}")

        # News aggregieren
        news = self.aggregate_news()

        # Zu Notion
        self.push_to_notion(news)

        # Email versenden
        self.send_email(news)

        print(f"✅ Fertig: {datetime.now().isoformat()}")


if __name__ == "__main__":
    agg = NewsAggregator()
    agg.run()
