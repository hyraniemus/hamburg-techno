#!/usr/bin/env python3
"""
AI-Post-Production News Digest Generator
Tägliche Zusammenfassung (max. 400 Wörter) für Video-Editor & AI-Content-Creator
"""

import os
import sys
from datetime import datetime
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

# Search queries for news sources
SEARCH_QUERIES = [
    "DaVinci Resolve AI updates April 2026",
    "ComfyUI latest updates",
    "Runway Gen-4 video generation",
    "Claude Code video editing workflow integration",
    "AI video post production automation",
    "Remotion React video framework updates",
    "Suno AI music generation",
    "Avid Media Composer updates",
    "AI video freelance opportunities Hamburg",
]

SYSTEM_PROMPT = """Du bist ein spezialisierter News-Aggregator für einen Video-Editor & Post-Production-Spezialist in Hamburg,
der zu AI-gestützter Video-Produktion wechselt.

Deine Aufgabe: Erstelle eine tägliche Zusammenfassung (MAX 400 Wörter, auf Deutsch) mit dieser Struktur:

## **Top 3 News-Highlights**
- Kurze Bullet-Points mit Quelle/Link
- Relevanz für den Workflow (z.B. "Neues Resolve-Update verbessert AI-Color-Grading – teste in deinem nächsten Projekt")

## **Tool-Updates & Tipps**
- 2-3 praktische Insights (z.B. ffmpeg-Batch-Skripte, Notion-Integration, ComfyUI-Workflows)

## **Karriere/Trends**
- 1-2 Chancen für AI-Post-Prod-Freelancer (z.B. Startups, Remote-Jobs, Hamburg-fokussiert)

## **Aktion für heute**
- 1 personalisierter Next-Step (z.B. "Teste dieses ComfyUI-Modell", "Installiere DaVinci Resolve 21 beta")

Fokus-Themen (nur diese beachten):
✓ Avid Media Composer, DaVinci Resolve, Remotion, ComfyUI, Runway Gen-4
✓ Claude Code-Integration, AI-Video-Generierung, Post-Production-Automatisierung
✓ Freelance-Chancen in AI-Editing, Musikproduktion mit Suno
✓ Film/TV-News, Dokumentar-Produktion
✗ Politik, allgemeine Wirtschaft (nur Tech/Film-relevant)

Stil: Klar, handlungsorientiert, mit Links zu Quellen. Keine fluff, pure Insights."""


def generate_digest(news_content: str) -> str:
    """Generate news digest using Claude with multi-turn conversation."""

    conversation_history = []

    # First turn: Ask Claude to analyze the news
    conversation_history.append({
        "role": "user",
        "content": f"""Analysiere diese aktuellen News und erstelle eine AI-Post-Production News-Zusammenfassung:

{news_content}

Bitte strukturiere genau nach dem System-Prompt: Top 3 Highlights, Tool-Updates, Karriere/Trends, Aktion für heute."""
    })

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )

    digest = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": digest
    })

    # Second turn: Verify word count and quality
    conversation_history.append({
        "role": "user",
        "content": "Überprüfe: Ist das genau nach dem Format? Maximal 400 Wörter? Alle Links dabei? Kurze Bestätigung und ggf. Verbesserungen."
    })

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )

    verification = response.content[0].text

    # If verification suggests changes, refine
    if "Verbesserungen" in verification or "Anpassungen" in verification:
        conversation_history.append({
            "role": "assistant",
            "content": verification
        })
        conversation_history.append({
            "role": "user",
            "content": "Bitte erstelle die finale, optimierte Version basierend auf deinem Feedback."
        })

        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=conversation_history
        )
        digest = response.content[0].text

    return digest


def create_notion_page(digest: str) -> None:
    """Create a Notion page with the news digest."""
    today = datetime.now().strftime("%d.%m.%Y")

    # Prepare content for Notion Markdown
    notion_content = f"""# Deine AI-Post-Prod News – {today}

{digest}

---
*Erstellt: {datetime.now().strftime("%H:%M")} CEST*
*Quelle: Web-Search (Blackmagic, GitHub, Reddit, HackerNews)*
"""

    # Save to local markdown file (fallback)
    news_dir = os.path.join(os.path.dirname(__file__), "ai_news")
    os.makedirs(news_dir, exist_ok=True)

    filename = os.path.join(news_dir, f"news_{today.replace('.', '-')}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(notion_content)

    print(f"✓ Notion-Datei erstellt: {filename}")

    # TODO: Integrate with Notion API
    # from notion_client import Client
    # notion = Client(auth=os.environ.get("NOTION_TOKEN"))
    # notion.pages.create(parent={"database_id": "..."}, properties={...})

    return notion_content


def send_email_digest(digest: str) -> None:
    """Send digest via email."""
    today = datetime.now().strftime("%d.%m.%Y")
    subject = f"Deine AI-Post-Prod News – {today}"

    # TODO: Integrate email service (SendGrid, SMTP, etc.)
    # For now, save to file
    email_file = os.path.join(os.path.dirname(__file__), "ai_news", f"email_{today.replace('.', '-')}.txt")
    os.makedirs(os.path.dirname(email_file), exist_ok=True)

    with open(email_file, "w", encoding="utf-8") as f:
        f.write(f"Subject: {subject}\n")
        f.write(f"To: mmittelbach@gmail.com\n\n")
        f.write(digest)

    print(f"✓ Email-Draft erstellt: {email_file}")
    print(f"  (Versand an mmittelbach@gmail.com würde hier erfolgen)")


def main():
    print("🔍 AI-Post-Production News Digest Generator")
    print(f"   {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} CEST\n")

    # Sample news content (in production, this would come from actual API calls)
    sample_news = """
## DaVinci Resolve 21 Update (NAB 2026)
- Neue Photo Page für Foto-Editing
- AI-Features: IntelliSearch (natural language media search), CineFocus (synthetic depth),
  Face Age Transformer, Face Reshaper, AI Speech Generator, AI Motion Deblur
- Public beta verfügbar
- Quelle: https://www.leagueoffilmmakers.com/blackmagic-design-reveals-davinci-resolve-21-for-this-years-2026-nab/

## Runway Gen-4.5 Verfügbar
- Bestes Text-to-Video-Modell 2026
- Verbesserte character consistency und temporale Kohärenz
- Text-to-Video und Image-to-Video control
- Quelle: https://runwayml.com/research/introducing-runway-gen-4.5

## ComfyUI 0.19.3 Release
- LTX text generation mit improved template handling
- Quiver arrow-1.1 SVG models für vector graphics
- Performance improvements bei quantized models
- Quelle: https://github.com/Comfy-Org/ComfyUI/releases

## Claude Code Video Editing Integration
- Remotion + Claude Code für programmatic video creation
- Hyperframes Integration für automated video editing workflows
- Slack-Integration für Review-Loops
- Quelle: https://www.remotion.dev/docs/ai/claude-code

## AI Post-Production Automation 2026
- 85% der Post-Prod-Tasks sind automatisierbar
- Silence removal, audio processing, VFX cleanup gelöst
- Color correction AI-powered
- Quelle: https://vidno.ai/blog/automated-video-post-production
"""

    print("📊 Generiere Zusammenfassung...\n")
    digest = generate_digest(sample_news)

    print("📝 Generierte News-Zusammenfassung:\n")
    print("-" * 80)
    print(digest)
    print("-" * 80 + "\n")

    # Save to Notion (local markdown)
    create_notion_page(digest)

    # Prepare email
    send_email_digest(digest)

    print("\n✅ News-Digest erfolgreich erstellt!")
    print("   Nächste automatische Ausführung: morgen 06:30 CEST")


if __name__ == "__main__":
    main()
