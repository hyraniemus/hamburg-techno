#!/usr/bin/env python3
"""
AI-Post-Production Daily News Scraper
Sammelt News von Reddit, Hacker News, Tech-Blogs und speichert in Notion
"""

import os
import json
from datetime import datetime
from typing import List, Dict
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DB_ID = "9d5b29f9-e74c-4075-bb09-f2600a77677e"

# News-Quellen nach Kategorie
REDDIT_SUBS = [
    "davinciresolve",
    "Avid",
    "MachineLearning",
    "VideoEditing",
    "aivideo",
]

KEYWORDS = {
    "Tool Updates": [
        "DaVinci Resolve",
        "Avid Media Composer",
        "Remotion",
        "ComfyUI",
        "Runway",
        "Claude Code",
        "update",
        "release",
    ],
    "AI-Video": [
        "AI video generation",
        "text-to-video",
        "video synthesis",
        "neural rendering",
    ],
    "Musik": ["Suno", "music generation", "audio synthesis"],
}


def fetch_reddit_news() -> List[Dict]:
    """Fetch top posts from target subreddits"""
    news = []
    try:
        for sub in REDDIT_SUBS:
            url = f"https://www.reddit.com/r/{sub}/top.json?t=day&limit=5"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                posts = response.json()["data"]["children"]
                for post in posts:
                    data = post["data"]
                    if data["score"] > 10:  # Filter low engagement
                        category = categorize_post(data["title"])
                        news.append(
                            {
                                "headline": data["title"][:100],
                                "link": f"https://reddit.com{data['permalink']}",
                                "tool": f"r/{sub}",
                                "category": category,
                                "relevance": f"{data['score']} upvotes",
                            }
                        )
    except Exception as e:
        print(f"❌ Reddit fetch error: {e}")
    return news


def fetch_hackernews() -> List[Dict]:
    """Fetch top stories from Hacker News"""
    news = []
    try:
        # Top stories
        response = requests.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10
        )
        if response.status_code == 200:
            story_ids = response.json()[:20]
            for story_id in story_ids:
                try:
                    story = requests.get(
                        f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
                        timeout=5,
                    ).json()
                    title = story.get("title", "")
                    if any(
                        kw.lower() in title.lower()
                        for kws in KEYWORDS.values()
                        for kw in kws
                    ):
                        category = categorize_text(title)
                        news.append(
                            {
                                "headline": title[:100],
                                "link": story.get("url", ""),
                                "tool": "Hacker News",
                                "category": category,
                                "relevance": f"{story.get('score', 0)} points",
                            }
                        )
                except:
                    pass
    except Exception as e:
        print(f"❌ HN fetch error: {e}")
    return news


def categorize_post(text: str) -> str:
    """Kategorisiere Text basierend auf Keywords"""
    text_lower = text.lower()
    for category, keywords in KEYWORDS.items():
        if any(kw.lower() in text_lower for kw in keywords):
            return category
    return "Tool Updates"


def categorize_text(text: str) -> str:
    """Kategorisiere Text"""
    return categorize_post(text)


def add_to_notion(news_items: List[Dict]):
    """Add news items to Notion database"""
    if not NOTION_TOKEN:
        print("❌ NOTION_TOKEN not set")
        return

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    today = datetime.now().strftime("%Y-%m-%d")

    for item in news_items[:10]:  # Limit to 10 items
        payload = {
            "parent": {"database_id": NOTION_DB_ID},
            "properties": {
                "Date": {"title": [{"text": {"content": today}}]},
                "Headline": {"rich_text": [{"text": {"content": item["headline"]}}]},
                "Tool": {"rich_text": [{"text": {"content": item["tool"]}}]},
                "Link": {"url": item["link"]},
                "Category": {"select": {"name": item["category"]}},
                "Relevance": {"rich_text": [{"text": {"content": item["relevance"]}}]},
                "Status": {"select": {"name": "Review"}},
                "Action": {
                    "rich_text": [{"text": {"content": "Geplant - Details folgen"}}]
                },
            },
        }

        try:
            response = requests.post(
                "https://api.notion.com/v1/pages",
                headers=headers,
                json=payload,
                timeout=10,
            )
            if response.status_code == 200:
                print(f"✅ Added: {item['headline'][:50]}")
            else:
                print(f"⚠️ Notion error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Error adding to Notion: {e}")


def main():
    print("🔍 Fetching AI-Post-Prod News...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S CEST')}")

    all_news = []
    all_news.extend(fetch_reddit_news())
    all_news.extend(fetch_hackernews())

    # Remove duplicates
    seen = set()
    unique_news = []
    for item in all_news:
        if item["headline"] not in seen:
            seen.add(item["headline"])
            unique_news.append(item)

    print(f"📰 Found {len(unique_news)} unique news items")
    add_to_notion(unique_news)
    print("✅ Scraping complete!")


if __name__ == "__main__":
    main()
