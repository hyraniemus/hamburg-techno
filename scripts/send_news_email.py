#!/usr/bin/env python3
"""
Versende die tägliche News per E-Mail via SendGrid
"""

import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "mmittelbach@gmail.com")


def send_news_email():
    """Versende die News-Zusammenfassung per E-Mail"""

    today = datetime.now().strftime("%d. %B %Y")
    notion_url = "https://www.notion.so/AI-Post-Prod-News-1ed331909c264ff190633f0c65d3cbb1"

    message = Mail(
        from_email=Email("claude@hamburg-techno.local", "Claude AI News"),
        to_emails=To(RECIPIENT_EMAIL),
        subject=f"Deine AI-Post-Prod News – {today}",
        html_content=f"""
        <html>
            <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
                <h1>🎬 Deine tägliche AI-Video-News</h1>

                <p><strong>{today}</strong> | 06:30 CEST</p>

                <p>Hallo Marcus,</p>

                <p>Deine persönliche AI-Post-Production News ist aktualisiert!
                Du findest die vollständige Zusammenfassung hier:</p>

                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <a href="{notion_url}" style="color: white; text-decoration: none; font-size: 16px; font-weight: bold;">
                        ➜ Öffne die News in Notion
                    </a>
                </div>

                <h3>Was ist neu?</h3>
                <ul>
                    <li><strong>Top 3 Highlights:</strong> Aktuelle Updates zu deinen Tools</li>
                    <li><strong>Tool-Updates:</strong> Praktische Tipps & Workflows</li>
                    <li><strong>Karriere:</strong> Freelance-Chancen & Trends</li>
                    <li><strong>Aktion für heute:</strong> Dein personalisierter Next-Step</li>
                </ul>

                <p style="color: #666; font-size: 12px; margin-top: 40px; border-top: 1px solid #ddd; padding-top: 20px;">
                    Diese News werden täglich um 06:30 CEST aktualisiert.<br>
                    Quellen: Reddit, Hacker News, Blackmagic Blog, Runway, Suno, Claude Code Docs
                </p>
            </body>
        </html>
        """
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"✅ E-Mail versendet! Status: {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ E-Mail-Fehler: {str(e)}")
        return False


if __name__ == "__main__":
    send_news_email()
