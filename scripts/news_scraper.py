#!/usr/bin/env python3
"""
AI-Post-Production Daily News Scraper
Sammelt News von Reddit, Hacker News, Tech-Blogs und speichert in Notion
"""

import os
import json
import feedparser
from datetime import datetime, timedelta
from typing import List, Dict
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DB_ID = "9d5b29f9-e74c-4075-bb09-f2600a77677e"
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")

# News-Quellen nach Kategorie
REDDIT_SUBS = [
    "davinciresolve",
    "Avid",
    "MachineLearning",
    "VideoEditing",
    "aivideo",
]

# RSS Feed-Quellen (Tech & Video Production)
RSS_FEEDS = {
    "Blackmagic Design": "https://www.blackmagicdesign.com/feeds/blog.xml",
    "Anthropic Blog": "https://www.anthropic.com/feed.xml",
    "Runway": "https://blog.runwayml.com/feed/",
    "OpenAI": "https://openai.com/feed.rss",
    "Adobe Blog": "https://blog.adobe.com/feed",
    "NVIDIA AI": "https://blogs.nvidia.com/feed/",
    "Cogito": "https://www.cogito.ai/blog/feed.xml",
}

# Twitter Hashtags & Keywords zu tracken
TWITTER_SEARCHES = [
    "#AIVideo",
    "#VideoGeneration",
    "#DaVinciResolve",
    "#Remotion",
    "#ComfyUI",
    "#RunwayML",
    "#Suno",
    "#PostProduction",
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
        "new feature",
    ],
    "AI-Video": [
        "AI video generation",
        "text-to-video",
        "video synthesis",
        "neural rendering",
        "generative video",
    ],
    "Musik": ["Suno", "music generation", "audio synthesis", "AI music"],
    "Film/TV": [
        "documentary",
        "filmmaking",
        "cinematography",
        "production",
    ],
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


def fetch_rss_feeds() -> List[Dict]:
    """Fetch latest articles from RSS feeds"""
    news = []
    for feed_name, feed_url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(feed_url)
            if not feed.entries:
                continue

            # Nur neue Einträge (letzte 24h)
            cutoff_time = datetime.now() - timedelta(days=1)

            for entry in feed.entries[:5]:  # Top 5 pro Feed
                pub_date = entry.get("published_parsed")
                if pub_date:
                    entry_date = datetime(*pub_date[:6])
                    if entry_date < cutoff_time:
                        continue

                title = entry.get("title", "No title")
                summary = entry.get("summary", "")
                link = entry.get("link", "")

                # Filtere nach Keywords
                full_text = f"{title} {summary}".lower()
                category = categorize_text(full_text)

                if any(
                    kw.lower() in full_text
                    for kws in KEYWORDS.values()
                    for kw in kws
                ):
                    news.append(
                        {
                            "headline": title[:100],
                            "link": link,
                            "tool": feed_name,
                            "category": category,
                            "relevance": "Blog Post",
                        }
                    )
        except Exception as e:
            print(f"⚠️ RSS Feed error ({feed_name}): {e}")

    return news


def fetch_twitter_search() -> List[Dict]:
    """
    Fetch recent tweets via Twitter API v2 (requires bearer token)
    Falls kein API Key: Fallback zu alternative method
    """
    news = []

    if not TWITTER_API_KEY:
        print("⚠️ No TWITTER_API_KEY set - skipping Twitter search")
        return news

    headers = {
        "Authorization": f"Bearer {TWITTER_API_KEY}",
    }

    for search_term in TWITTER_SEARCHES:
        try:
            # Twitter API v2 recent search endpoint
            url = "https://api.twitter.com/2/tweets/search/recent"
            params = {
                "query": search_term,
                "max_results": 10,
                "tweet.fields": "author_id,created_at,public_metrics",
                "expansions": "author_id",
                "user.fields": "username",
            }

            response = requests.get(url, headers=headers, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if "data" in data:
                    for tweet in data["data"]:
                        # Filter nach Engagement (min 5 retweets/likes)
                        engagement = (
                            tweet.get("public_metrics", {}).get("like_count", 0)
                            + tweet.get("public_metrics", {}).get("retweet_count", 0)
                        )
                        if engagement >= 5:
                            category = categorize_text(tweet["text"])
                            news.append(
                                {
                                    "headline": tweet["text"][:100],
                                    "link": f"https://twitter.com/i/web/status/{tweet['id']}",
                                    "tool": "Twitter",
                                    "category": category,
                                    "relevance": f"{engagement} engagements",
                                }
                            )
            else:
                print(
                    f"⚠️ Twitter API error: {response.status_code} - {response.text[:200]}"
                )
        except Exception as e:
            print(f"⚠️ Twitter search error ({search_term}): {e}")

    return news


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
    print("  📍 Reddit...", end=" ", flush=True)
    all_news.extend(fetch_reddit_news())
    print("✓")

    print("  📍 Hacker News...", end=" ", flush=True)
    all_news.extend(fetch_hackernews())
    print("✓")

    print("  📍 RSS Feeds...", end=" ", flush=True)
    all_news.extend(fetch_rss_feeds())
    print("✓")

    print("  📍 Twitter...", end=" ", flush=True)
    all_news.extend(fetch_twitter_search())
    print("✓")

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
