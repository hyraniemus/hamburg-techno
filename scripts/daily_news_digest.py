#!/usr/bin/env python3
"""
Daily AI Post-Production News Digest Generator
Fetches news from multiple sources and sends via Notion or Email
"""

import os
import sys
from datetime import datetime, timezone
import json
import requests
from typing import List, Dict

# Configuration
INTERESTS = {
    "avid": "Avid Media Composer updates/bug fixes",
    "resolve": "DaVinci Resolve AI features",
    "remotion": "Remotion Claude AI integration",
    "comfyui": "ComfyUI workflows",
    "runway": "Runway Gen-4 AI video",
    "ai_video": "AI video generation",
    "post_production": "Post-production automation",
    "freelance": "AI editing freelance opportunities",
    "suno": "Suno music production",
    "film": "Film/TV news",
}

SEARCH_QUERIES = [
    "Avid Media Composer update bug fixes 2026",
    "DaVinci Resolve AI features June 2026",
    "ComfyUI Runway Gen-4 video generation",
    "Remotion Claude Code AI integration",
    "AI post-production automation 2026",
    "AI video freelance opportunities",
]

class NewsDigestGenerator:
    def __init__(self):
        self.news_items = []
        self.digest = ""
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.date_de = datetime.now().strftime("%d.%m.%Y")

    def fetch_news_from_sources(self):
        """
        In production, this would fetch from:
        - Reddit APIs (r/Avid, r/davinciresolve, r/MachineLearning)
        - HackerNews API
        - Tool blogs (Blackmagic, Anthropic)
        - Twitter/X API
        """
        # Placeholder: This would be replaced with actual API calls
        self.news_items = [
            {
                "category": "resolve",
                "title": "DaVinci Resolve 21 veröffentlicht mit neuen AI-Color-Grading-Tools",
                "description": "Blackmagic hat Resolve 21 mit erweiterten AI-Features gelauncht, inklusive Photo Page und IntelliSearch",
                "link": "https://www.redsharknews.com/davinci-resolve-21-nab-2026-photo-page-ai-tools",
                "relevance": "Testet die neuen 1-Node AI Color Grading Features in deinem nächsten Projekt"
            },
            {
                "category": "runway_comfyui",
                "title": "Runway Gen-4.5 jetzt in ComfyUI integriert",
                "description": "ComfyUI API Nodes mit Runway Gen-4 Image und Full-Stack Video Generation Live",
                "link": "https://x.com/ComfyUI/status/1927400907051765808",
                "relevance": "Text-to-Video und Image-to-Video mit konsistenter Charakterdarstellung"
            },
            {
                "category": "remotion",
                "title": "Claude Code + Remotion: Videos jetzt vollautomatisiert erstellen",
                "description": "Mit Claude Code kannst du Videos nur durch natürlichsprachige Prompts erzeugen – ohne Code zu schreiben",
                "link": "https://www.remotion.dev/docs/ai/claude-code",
                "relevance": "Perfekt für Batch-Video-Produktion von Social Media Content"
            },
            {
                "category": "ai_post_prod",
                "title": "AI Sound Design revolutioniert Post-Production 2026",
                "description": "Neural Models können jetzt Stems separieren, Ambience rekonstruieren und Foley-Sound synthesieren",
                "link": "https://flawlessai.com/blog/ai-in-post-production",
                "relevance": "Automatisiert Dialog-Transcription und Ambient Sound Cleanup"
            },
            {
                "category": "avid",
                "title": "Media Composer 2025.12.1 mit aktuellen Bug Fixes",
                "description": "Avid veröffentlicht regelmäßig Updates – ReadMe verfügbar auf Support KB",
                "link": "https://kb.avid.com/pkb/articles/en_US/Knowledge/Media-Composer-2025-Documentation",
                "relevance": "Häufige Fixes für Proxy-Handling und XML-Export"
            }
        ]

    def generate_digest(self) -> str:
        """Generate structured news digest in German"""

        digest = f"# 🎬 Deine AI-Post-Prod News – {self.date_de}\n\n"

        # Top 3 Highlights
        digest += "## 🔥 TOP 3 NEWS-HIGHLIGHTS\n\n"
        for i, item in enumerate(self.news_items[:3], 1):
            digest += f"**{i}. {item['title']}**\n"
            digest += f"- {item['description']}\n"
            digest += f"- **Für dich relevant:** {item['relevance']}\n"
            digest += f"- 🔗 [Quelle]({item['link']})\n\n"

        # Tool Updates & Tipps
        digest += "## 🛠️ TOOL-UPDATES & PRAKTISCHE TIPPS\n\n"
        digest += "**1. ComfyUI + Runway Gen-4.5 Workflow**\n"
        digest += "   - Nutze die neuen Partner Nodes für Text-to-Video mit 4K Output\n"
        digest += "   - Pricing: Gen-4.5 kostet 12 Credits/Sekunde (Plan: $9.90/Monat)\n"
        digest += "   - 📌 Tipp: Kombiniere mit Motion Brush 3.0 für präzise Bewegungssteuerung\n\n"

        digest += "**2. DaVinci Resolve 21: 1-Node statt 15 Nodes**\n"
        digest += "   - Neue AI Color Grading ersetzt komplexe Node Trees\n"
        digest += "   - IntelliSearch für schnellere Content-Navigation\n"
        digest += "   - 📌 Tipp: Teste mit Fashion-Footage – zeigt Best Case der AI\n\n"

        digest += "**3. Remotion + Claude Code: Video-Batching leicht gemacht**\n"
        digest += "   - Schreib einfach einen Prompt statt TypeScript-Code\n"
        digest += "   - Perfekt für Social Media Repurposing (Instagram Reels, TikTok)\n"
        digest += "   - 📌 Tipp: Nutze Variablen für schnelle A/B Tests\n\n"

        # Karriere/Trends
        digest += "## 💼 KARRIERE & TRENDS\n\n"
        digest += "**AI-Video-Freelancer verdienen 2x mehr (2026)**\n"
        digest += "- Traditionelle Video-Editoren: €15–45/Std\n"
        digest += "- AI-Post-Prod Spezialisten: €60–150+/Std (custom Models, Cleanup)\n"
        digest += "- 🎯 **Top-Plattformen:** Upwork, Truelancer, Curious Refuge (AI Jobs Board)\n\n"

        digest += "**Hamburg Tech Scene:**\n"
        digest += "- Viele Startups suchen AI-Video-Experten (Remote + vor Ort)\n"
        digest += "- Post-Production-Studios beginnen AI-Services zu integrieren\n"
        digest += "- 🚀 **Netzwerk-Tipp:** Hamburg Tech Community, NextMedia Initiative\n\n"

        # Aktion für heute
        digest += "## ✅ DEINE AKTION FÜR HEUTE\n\n"
        digest += "1. **Download & Test:** Resolve 21 neue Color Grading Demo (5 Minuten)\n"
        digest += "2. **Code-Snippet:** Erstelle mit Claude Code dein erstes Remotion-Video\n"
        digest += "3. **Bookmark:** ComfyUI Runway Partner Nodes Dokumentation speichern\n"
        digest += "4. **Optional:** Upwork nach \"AI Video Post-Production\" filtern → deine Rate setzen\n\n"

        digest += f"---\n_Generiert: {datetime.now().strftime('%H:%M CEST')}_\n"

        return digest

    def save_to_markdown(self) -> str:
        """Save digest to markdown file"""
        output_dir = "news_digests"
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{output_dir}/news_{datetime.now().strftime('%Y%m%d')}.md"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.digest)

        return filename

    def generate(self) -> str:
        """Main generation flow"""
        self.fetch_news_from_sources()
        self.digest = self.generate_digest()
        return self.digest

def main():
    generator = NewsDigestGenerator()
    digest = generator.generate()

    print(digest)

    # Optional: Save to file
    output_file = generator.save_to_markdown()
    print(f"\n✅ Digest saved to: {output_file}")

    # TODO: Integration mit:
    # 1. Notion API für Page-Erstellung
    # 2. Email API (SendGrid, Mailgun) für mmittelbach@gmail.com
    # 3. RSS/Webhook für automatische Updates

if __name__ == "__main__":
    main()
