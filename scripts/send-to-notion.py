#!/usr/bin/env python3
"""
Send daily news summary to Notion database
Requires NOTION_API_TOKEN and NOTION_PAGE_ID as environment variables
"""

import os
import json
import sys
import requests
from datetime import datetime

def load_news_output():
    """Load generated news from daily-news.py output"""
    try:
        with open("/tmp/daily-news-output.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ News output file not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print("❌ Failed to parse news output")
        sys.exit(1)

def send_to_notion(title: str, content: str):
    """Send news summary to Notion as new page"""
    api_token = os.getenv("NOTION_API_TOKEN")
    parent_page_id = os.getenv("NOTION_NEWS_PAGE_ID")

    if not api_token:
        print("⚠️  NOTION_API_TOKEN not configured - skipping Notion update")
        print("   To enable: Set NOTION_API_TOKEN & NOTION_NEWS_PAGE_ID in GitHub Secrets")
        return True

    if not parent_page_id:
        print("⚠️  NOTION_NEWS_PAGE_ID not configured")
        return False

    # Notion API endpoint for creating a page
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    # Parse content into Notion blocks
    blocks = parse_markdown_to_blocks(content)

    payload = {
        "parent": {
            "page_id": parent_page_id
        },
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        },
        "children": blocks
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        page_id = response.json()["id"]
        print(f"✅ News page created in Notion: {page_id}")
        return True

    except requests.exceptions.HTTPError as e:
        print(f"❌ Notion API error: {e.response.status_code}")
        print(f"   Response: {e.response.text}")
        return False
    except Exception as e:
        print(f"❌ Error sending to Notion: {str(e)}")
        return False

def parse_markdown_to_blocks(content: str) -> list:
    """Convert markdown content to Notion blocks"""
    blocks = []
    lines = content.split("\n")

    for line in lines:
        if line.startswith("# "):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:].strip()}}]
                }
            })
        elif line.startswith("## "):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": line[3:].strip()}}]
                }
            })
        elif line.startswith("### "):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": line[4:].strip()}}]
                }
            })
        elif line.startswith("- "):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:].strip()}}]
                }
            })
        elif line.strip():
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": line}}]
                }
            })

    return blocks

def main():
    """Main function"""
    print("📤 Sending news to Notion...")

    # Load generated news
    news_data = load_news_output()
    title = news_data.get("title")
    content = news_data.get("content")

    if not title or not content:
        print("❌ Invalid news data structure")
        return 1

    # Send to Notion
    if send_to_notion(title, content):
        print("✅ News update completed successfully")
        return 0
    else:
        print("⚠️  News generated but not sent to Notion (API error)")
        return 1

if __name__ == "__main__":
    sys.exit(main())
