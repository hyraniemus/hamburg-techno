#!/usr/bin/env python3
"""
Notion Integration für AI-News-Digest
Benötigt: NOTION_TOKEN Environment Variable
"""

import os
import requests
from datetime import datetime
from typing import Optional

class NotionNewsIntegration:
    def __init__(self, token: Optional[str] = None, database_id: Optional[str] = None):
        """
        Initialize Notion integration.

        Args:
            token: Notion API token (oder NOTION_TOKEN env var)
            database_id: Notion Database ID für News (oder NOTION_NEWS_DB_ID env var)
        """
        self.token = token or os.getenv("NOTION_TOKEN")
        self.database_id = database_id or os.getenv("NOTION_NEWS_DB_ID")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def create_news_page(self, digest: str) -> str:
        """Create a new Notion page with the news digest."""
        today = datetime.now()
        date_str = today.strftime("%d.%m.%Y")

        # Parse digest sections
        sections = self._parse_digest(digest)

        # Build page payload
        payload = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Titel": {
                    "title": [{"text": {"content": f"AI-News – {date_str}"}}]
                },
                "Datum": {
                    "date": {"start": today.strftime("%Y-%m-%d")}
                },
                "Status": {
                    "select": {"name": "Aktuell"}
                },
            },
            "children": self._build_page_blocks(sections),
        }

        response = requests.post(
            "https://api.notion.com/v1/pages",
            headers=self.headers,
            json=payload,
        )

        if response.status_code == 200:
            page_id = response.json()["id"]
            print(f"✓ Notion-Seite erstellt: {page_id}")
            return page_id
        else:
            print(f"✗ Notion-Fehler: {response.status_code} - {response.text}")
            return None

    def _parse_digest(self, digest: str) -> dict:
        """Parse digest into sections."""
        sections = {
            "highlights": "",
            "tools": "",
            "career": "",
            "action": "",
        }

        # Simple parsing logic
        if "Top 3 News-Highlights" in digest:
            parts = digest.split("##")
            for part in parts:
                if "Highlights" in part:
                    sections["highlights"] = part.strip()
                elif "Tool" in part:
                    sections["tools"] = part.strip()
                elif "Karriere" in part:
                    sections["career"] = part.strip()
                elif "Aktion" in part:
                    sections["action"] = part.strip()

        return sections

    def _build_page_blocks(self, sections: dict) -> list:
        """Build Notion page blocks from sections."""
        blocks = []

        for key, content in sections.items():
            if content:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": content}}]
                    },
                })

        return blocks


def setup_notion_database() -> str:
    """
    Create a new Notion database for news if it doesn't exist.
    Returns database_id.
    """
    token = os.getenv("NOTION_TOKEN")
    parent_page_id = os.getenv("NOTION_PARENT_PAGE_ID")

    if not token or not parent_page_id:
        print("⚠️  NOTION_TOKEN und NOTION_PARENT_PAGE_ID erforderlich")
        return None

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    # Create database
    payload = {
        "parent": {"page_id": parent_page_id},
        "title": [{"text": {"content": "AI-Post-Production News Digest"}}],
        "properties": {
            "Titel": {"title": {}},
            "Datum": {"date": {}},
            "Status": {"select": {"options": [
                {"name": "Aktuell", "color": "green"},
                {"name": "Archiv", "color": "gray"},
            ]}},
            "Links": {"url": {}},
        },
    }

    response = requests.post(
        "https://api.notion.com/v1/databases",
        headers=headers,
        json=payload,
    )

    if response.status_code == 200:
        db_id = response.json()["id"]
        print(f"✓ Notion-Datenbank erstellt: {db_id}")
        print(f"  Speichere dies als NOTION_NEWS_DB_ID")
        return db_id
    else:
        print(f"✗ Datenbank-Fehler: {response.status_code}")
        return None


if __name__ == "__main__":
    # Test integration
    token = os.getenv("NOTION_TOKEN")
    db_id = os.getenv("NOTION_NEWS_DB_ID")

    if token and db_id:
        integration = NotionNewsIntegration(token, db_id)
        test_digest = """
## Top 3 News-Highlights
- **DaVinci Resolve 21 Beta**: Neue AI-Features (IntelliSearch, CineFocus)
- **Runway Gen-4.5**: Bestes Text-to-Video-Modell
- **ComfyUI 0.19.3**: LTX Text-Generation + Performance-Fixes

## Tool-Updates & Tipps
- ComfyUI-Workflows mit neuen SVG-Models testen
- DaVinci Resolve 21 beta für Color-Grading testen

## Karriere/Trends
- AI-Video-Freelance-Jobs auf Upwork/Fiverr steigen

## Aktion für heute
- Download DaVinci Resolve 21 beta von Blackmagic
"""
        integration.create_news_page(test_digest)
    else:
        print("ℹ️  Notion-Setup erforderlich:")
        print("   1. Erstelle Notion API Token: https://www.notion.so/my-integrations")
        print("   2. Setze Environment Variables:")
        print("      export NOTION_TOKEN='your-token'")
        print("      export NOTION_PARENT_PAGE_ID='page-id'")
        print("   3. Führe setup aus: python3 notion_integration.py")
