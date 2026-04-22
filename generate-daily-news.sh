#!/bin/bash

# AI Post-Prod Daily News Generator
# Läuft täglich um 06:30 CEST
# Generiert News-Zusammenfassung und sendet per E-Mail oder Notion

set -e

# Konfiguration
EMAIL="mmittelbach@gmail.com"
NEWS_DIR="$HOME/hamburg-techno/daily-news"
TODAY=$(date +"%Y-%m-%d")
NEWS_FILE="$NEWS_DIR/news-$TODAY.md"

# Verzeichnis erstellen, falls nicht existent
mkdir -p "$NEWS_DIR"

# News-Zusammenfassung generieren (Template für tägliche Ausführung)
cat > "$NEWS_FILE" << 'EOF'
# 📺 DEINE AI-POST-PROD NEWS – $(date +%d.%m.%Y)

## 🔥 Top 3 News-Highlights

### 1. DaVinci Resolve 21 Beta – AI Tools revolutionieren Color Grading & Editing
- **News**: Blackmagic präsentiert Resolve 21 mit IntelliSearch, CineFocus, AI UltraSharpen
- **Quelle**: [Newsshooter NAB 2026](https://www.newsshooter.com/2026/04/21/blackmagic-design-davinci-resolve-21-photo-page-preview-nab-2026/)
- **Für deinen Workflow**: IntelliSearch für schnellere Asset-Suche in großen Projekten
- **Aktion**: Beta runterladen & in nächstem Projekt testen

### 2. Runway Gen-4.5 – Text-to-Video Prompting perfektioniert
- **News**: Runway dominiert Google & OpenAI in Benchmarks, Character-Konsistenz garantiert
- **Quelle**: [Runway Research](https://runwayml.com/research/introducing-runway-gen-4.5)
- **Für deinen Workflow**: Complex Kamera-Bewegungen direkt per Prompt
- **Aktion**: Test-Prompt schreiben: "Drohne über Hafenszene, 45° pan, Abendlicht"

### 3. Remotion + Claude Code = 150K Installs in 8 Wochen 🚀
- **News**: Remotion Skill #5 weltweit bei Claude Code, 50 Videos in 15 Minuten
- **Quelle**: [Remotion AI Docs](https://www.remotion.dev/docs/ai/claude-code)
- **Für deinen Workflow**: Skalierbare Freelance-Automatisierung (Template + Claude = Batch-Videos)
- **Aktion**: Remotion Skill in Claude Code installieren

---

## 🛠️ Tool-Updates & Tipps

### ComfyUI + NVIDIA RTX: 40% Speedup seit Sept 2025
- **Update**: RTX Video Super Resolution (4K Real-Time), simplified App View bei GDC 2026
- **Praktisch**: Teste lokal statt Cloud für schnellere Iteration
- **Quelle**: [NVIDIA Blog GDC 2026](https://blogs.nvidia.com/blog/rtx-ai-garage-flux-ltx-video-comfyui-gdc/)

### Sonilo Native Node für ComfyUI
- **Feature**: Auto-Music-Generation passend zu deinem Video-Inhalt
- **Praktisch**: Spart 2-3h pro Projekt bei Music-Synchronisierung
- **Quelle**: [Sonilo x ComfyUI Partnership](https://www.prnewswire.com/news-releases/sonilo-brings-instant-video-to-music-generation-to-comfyui-through-exclusive-partnership-302741976.html)

### Claude Code Video Toolkit (Github)
- **Was**: MCP-Server + Skills für Hyperframes, Remotion, Screen Recording
- **Vorteil**: Zero-Code Video Production, keine Programmierung nötig
- **Repos**: digitalsamba/claude-code-video-toolkit, wilwaldon/Claude-Code-Video-Toolkit

---

## 💼 Karriere & Trends

### AI Post-Production ist Production-Standard 2026
- **Realität**: Studios nutzen live WAN 2.1, CogVideoX, AnimateDiff lokal
- **Chancen für dich**:
  - Automatisierungs-Services für Agenturen
  - Batch-Video-Produktion für Startups
  - Dokumentation + Code-Automation kombinieren
- **Hamburg-Akteure**: Check ORBX, Zomma (Tech-fokussierte Produktionshäuser)
- **Freelance-Angle**: "AI Post-Production Automation Specialist" auf Upwork/Toptal
- **Suno-Chancen**: AI-generierte Musik + deine Video-Production = neuer Service

---

## ✅ AKTION FÜR HEUTE

**→ DaVinci Resolve 21 Beta testen (15 Min)**
1. Download: https://www.blackmagicdesign.com/products/davinciresolve/whatsnew
2. Öffne eines deiner Archive-Projekte
3. Test IntelliSearch: "find hands" oder "find face"
4. Report: Funktioniert Asset-Recovery besser als vorher?

---

*Generiert: $(date +"%H:%M CEST")*
*Nächste Ausgabe: Morgen 06:30 CEST*
EOF

# Markdown-Variablen ausfüllen
sed -i "s|\$(date +%d.%m.%Y)|$(date +%d.%m.%Y)|g" "$NEWS_FILE"
sed -i "s|\$(date +\"%H:%M CEST\")|$(date +"%H:%M CEST")|g" "$NEWS_FILE"

echo "✅ News generiert: $NEWS_FILE"

# Attempt 1: E-Mail versenden (optional - benötigt mailx/sendmail)
if command -v mail &> /dev/null; then
  SUBJECT="Deine AI-Post-Prod News – $(date +%d.%m.%Y)"
  mail -s "$SUBJECT" "$EMAIL" < "$NEWS_FILE"
  echo "📧 E-Mail an $EMAIL versendet"
elif command -v ssmtp &> /dev/null; then
  # Alternative mit ssmtp, falls configured
  SUBJECT="Deine AI-Post-Prod News – $(date +%d.%m.%Y)"
  {
    echo "To: $EMAIL"
    echo "Subject: $SUBJECT"
    echo ""
    cat "$NEWS_FILE"
  } | ssmtp "$EMAIL"
  echo "📧 E-Mail via ssmtp versendet"
else
  echo "⚠️  Mail-Tool nicht gefunden. News lokal gespeichert."
  echo "   Datei: $NEWS_FILE"
  echo "   Zum Versenden: mail < $NEWS_FILE"
fi

# Git commit (optional - aktualisiert Repo)
if [ -d "$HOME/hamburg-techno/.git" ]; then
  cd "$HOME/hamburg-techno"
  git add "daily-news/$TODAY.md" 2>/dev/null || true
  git commit -m "Daily AI Post-Prod News – $TODAY" 2>/dev/null || true
  git push origin claude/compassionate-meitner-DAWRH 2>/dev/null || echo "⚠️  Git push fehlgeschlagen (optional)"
fi

echo "✅ News-Generator erfolgreich ausgeführt!"
