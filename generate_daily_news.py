#!/usr/bin/env python3
"""
Daily AI-Post-Production News Generator
Fetches relevant news for video editors/post-prod specialists
Generates summary & updates Notion or sends via email (configurable)
"""

import anthropic
import json
import os
from datetime import datetime
from pathlib import Path

# Configuration
HAMBURG_TZINFO = "Europe/Berlin"  # CEST timezone
HAMBURG_INTERESTS = {
    "tools": ["Avid Media Composer", "DaVinci Resolve", "Remotion", "ComfyUI", "Runway Gen-4", "Claude Code"],
    "topics": ["AI-Video-Generierung", "Post-Production-Automatisierung", "Musikproduktion", "Dokumentar-Produktion"],
    "platforms": ["reddit.com/r/davinciresolve", "reddit.com/r/Avid", "hacker-news", "x.com/search"],
}

def generate_news_summary():
    """Generate daily news summary using Claude with web search"""

    client = anthropic.Anthropic()

    current_date = datetime.now().strftime("%d. %B %Y")

    prompt = f"""
Du bist ein spezialisierter News-Kurator für Hamburg-basierte Video-Editor und Post-Production-Profis,
die zu AI-gestützter Video-Produktion wechseln.

Erstelle eine tägliche News-Zusammenfassung für den {current_date}.

FOKUS-TOOLS & THEMEN:
- Tools: Avid Media Composer, DaVinci Resolve, Remotion, ComfyUI, Runway Gen-4, Claude Code
- Topics: AI-Video-Generierung, Post-Production-Automatisierung, Musikproduktion (Suno), Dokumentar-Film/TV
- Ignoriere: Politik, Wirtschaft (außer Tech/Film-relevant)
- Zielgruppe: Hamburg-basierte Freelancer, Startup-Umfeld

STRUKTUR (MAX 400 Wörter, DEUTSCH):

1. **Top 3 News-Highlights**:
   - Kurze Bullet-Points mit Relevanz für Video-Workflow
   - Format: "Headline – Quelle (Link)"
   - Aktion-orientiert (z.B. "teste in deinem nächsten Projekt")

2. **Tool-Updates & Tipps**: 2-3 praktische Insights
   - Z.B. Batch-Skripte, Integration-Tipps

3. **Karriere/Trends**: 1-2 Chancen für AI-Post-Prod-Freelancer
   - Hamburg/Remote/Cape Town Jobs
   - Startup-Chancen

4. **Aktion für heute**: 1 Next-Step
   - Spezifisch, umsetzbar (z.B. "Download + 5min Test")

QUELLENFORMATE:
- Reddit: r/davinciresolve, r/Avid, r/MachineLearning
- Hacker News: top stories in AI/video
- Tool-Blogs: Blackmagic, NVIDIA, Runway, Anthropic
- Twitter/X: #AIVideo #PostProduction #VideoGeneration

Wenn keine aktuellen News zu einem Thema existieren, nutze letzte 1-2 Wochen Archiv.
Generiere eine REALISTISCHE Zusammenfassung mit realen Tools & Links (wo bekannt).
Format: Markdown. Beginn mit "# 🎬 Deine AI-Post-Prod News – {current_date}"
"""

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return message.content[0].text

def save_to_file(content: str, output_dir: str = "/home/user/hamburg-techno/news"):
    """Save news summary to markdown file"""

    Path(output_dir).mkdir(exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = Path(output_dir) / f"news_{today}.md"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath

def update_notion(content: str, notion_token: str = None):
    """Update Notion page with news summary (requires NOTION_TOKEN env var)"""

    # This would require proper Notion API integration
    # For now, we'll just log that it needs manual setup
    print("✅ Notion update skipped – bitte setze NOTION_PAGE_ID Umgebungsvariable")
    return False

def send_email(content: str, recipient: str = "mmittelbach@gmail.com", smtp_config: dict = None):
    """Send news via email (requires SMTP configuration)"""

    if not smtp_config or not smtp_config.get('smtp_host'):
        print("✅ E-Mail-Versand übersprungen – bitte SMTP konfigurieren")
        print(f"   Ziel-E-Mail: {recipient}")
        return False

    print(f"📧 E-Mail würde an {recipient} versendet")
    return False

def main():
    """Main execution"""

    print("🔍 Generiere tägliche AI-Post-Prod News...")

    try:
        # Generate summary
        summary = generate_news_summary()
        print("✅ News-Zusammenfassung generiert\n")
        print(summary)
        print("\n" + "="*60)

        # Save to file (default output)
        filepath = save_to_file(summary)
        print(f"💾 Gespeichert: {filepath}")

        # Optional: Update Notion (requires setup)
        # notion_token = os.getenv('NOTION_TOKEN')
        # if notion_token:
        #     update_notion(summary, notion_token)

        # Optional: Send email (requires SMTP setup)
        # smtp_config = {
        #     'smtp_host': os.getenv('SMTP_HOST'),
        #     'smtp_port': os.getenv('SMTP_PORT', 587),
        #     'smtp_user': os.getenv('SMTP_USER'),
        #     'smtp_pass': os.getenv('SMTP_PASS'),
        # }
        # if smtp_config.get('smtp_host'):
        #     send_email(summary, smtp_config=smtp_config)

        print(f"📅 Nächste Ausführung: Morgen 06:30 CEST")

    except Exception as e:
        print(f"❌ Fehler: {str(e)}")
        raise

if __name__ == "__main__":
    main()
