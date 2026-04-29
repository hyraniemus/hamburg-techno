# 📰 Dein tägliches AI-Post-Production News Digest

Automatisiertes System für deine persönliche News-Zusammenfassung – speziell kuratiert für dein Profil als Video-Editor/Post-Production-Spezialist in Hamburg mit Fokus auf AI-gestützte Produktion.

## 🎯 Was du bekommst

- **Täglich um 06:30 CEST**: Personalisierte News-Zusammenfassung (max. 400 Wörter)
- **4 Sektionen**:
  1. Top 3 News-Highlights (mit Quellen/Links)
  2. Tool-Updates & praktische Tipps
  3. Karriere/Freelance-Chancen
  4. Konkrete Aktion für heute

- **Fokus auf**:
  - Avid Media Composer, DaVinci Resolve, Remotion
  - ComfyUI, Runway Gen-4, Claude Code-Integration
  - AI-Video-Generierung, Post-Production-Automatisierung
  - Musikproduktion mit Suno
  - Film/TV-News, Dokumentar-Produktion

## 🚀 Schnellstart

### 1. Umgebungsvariablen einrichten

```bash
cp .env.example .env
```

Dann `.env` mit deinen Daten füllen:

```env
ANTHROPIC_API_KEY=sk-ant-... # Dein Anthropic API Key
SMTP_USER=deine_email@gmail.com
SMTP_PASS=dein_app_passwort  # Gmail: App Password generieren
EMAIL_TO=mmittelbach@gmail.com
TIMEZONE=Europe/Berlin
SCHEDULE_TIME=06:30
```

### 2. Sofort testen

```bash
npm run digest:now
```

Dies generiert einen Digest und speichert ihn lokal in `news-digests/`.

### 3. Tägliche Planung starten

```bash
npm run digest:schedule
```

Dies startet einen Scheduler, der täglich um 06:30 CEST läuft.

## 📧 Versandoptionen

### Option A: Email (Gmail)
1. Gmail-Konto öffnen
2. App-Password generieren: https://myaccount.google.com/apppasswords
3. In `.env` eintragen:
   ```env
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=deine_email@gmail.com
   SMTP_PASS=dein_app_passwort
   EMAIL_TO=mmittelbach@gmail.com
   ```

### Option B: Notion
1. Notion-Workspace öffnen
2. API-Key generieren: https://www.notion.so/my-integrations
3. Eine Datenbank für News-Digests erstellen
4. Database ID kopieren (aus der URL: `https://notion.so/{DATABASE_ID}?...`)
5. In `.env` eintragen:
   ```env
   NOTION_API_KEY=secret_...
   NOTION_DATABASE_ID=abc123def...
   ```

### Option C: Lokal (Standard)
Wenn E-Mail/Notion nicht konfiguriert: Digests werden in `news-digests/` als JSON gespeichert.

## 🛠️ Verfügbare Befehle

```bash
# Sofort einen Digest generieren
npm run digest:now

# Täglich um 06:30 CEST planen
npm run digest:schedule

# Manuell ausführen (mit ts-node)
npm run digest -- --now
npm run digest -- --schedule
```

## 📂 Dateistruktur

```
hamburg-techno/
├── news-digest.ts              # Hauptskript
├── news-digests/               # Lokal gespeicherte Digests
│   └── news-digest-2026-04-29.json
├── .env                        # Konfiguration (nicht committen!)
├── .env.example                # Template
└── NEWS-DIGEST-SETUP.md        # Diese Datei
```

## 🔧 Erweiterte Konfiguration

### Zeitzone ändern
In `.env`:
```env
TIMEZONE=Europe/Amsterdam    # oder andere Zeitzone
SCHEDULE_TIME=08:00          # Andere Uhrzeit
```

Verfügbare Zeitzonen: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

### API-Modell anpassen
In `news-digest.ts`, Zeile ~70:
```typescript
model: "claude-opus-4-7",  // Oder: claude-sonnet-4-6, claude-haiku-4-5
```

### News-Fokus-Themen ändern
In `news-digest.ts`, Zeile ~50 im Prompt anpassen:
```typescript
FOKUSGEBIETE:
- Deine Custom-Tools hier...
```

## 🐛 Troubleshooting

### Fehler: "ANTHROPIC_API_KEY not set"
→ `.env` anlegen und Anthropic API Key eintragen

### Fehler: "Email not sent"
→ Gmail: App Password statt normales Passwort nutzen
→ SMTP-Settings überprüfen

### Fehler: "Notion unauthorized"
→ API-Key in der Notion Integration Settings überprüfen
→ Bot-Zugriff auf die Datenbank erlauben

### Digest wird nicht täglich generiert
→ Prozess muss im Hintergrund laufen:
```bash
# Mit pm2 (empfohlen für Produktion):
npm install -g pm2
pm2 start "npm run digest:schedule"
pm2 save
```

## 📊 Monitoring

Digests werden lokal in `news-digests/` gespeichert mit ISO-Datum als Dateiname:
```
news-digest-2026-04-29.json
news-digest-2026-04-30.json
```

Öffne die Datei im Editor oder lese mit:
```bash
cat news-digests/news-digest-*.json | jq .
```

## 🔄 Pipeline-Integration

Wenn du dein News-Digest in dein Video-Produktions-Workflow integrieren willst:

1. **Automatische Benachrichtigungen in Slack**:
   ```bash
   # In news-digest.ts nach generateDigest() hinzufügen:
   await fetch(process.env.SLACK_WEBHOOK_URL, {
     method: "POST",
     body: JSON.stringify({ text: `📰 Daily News: ${digest.date}` })
   });
   ```

2. **Automatisches Backup in Google Drive/Dropbox**:
   ```typescript
   // Google Drive API integrieren für automatische Archivierung
   ```

3. **RSS-Feed generieren** (für News-Reader):
   ```typescript
   // JSON zu RSS konvertieren
   ```

## 📝 Notizen

- Digests werden basierend auf **aktuellem Web-Wissen von Claude** generiert
- Quellen sind im Digest mit Links angegeben
- Ändere den Prompt in `news-digest.ts` für andere Themen/Zielgruppen
- Das System arbeitet offline (Recherche via Claude)

## 🎓 Nächste Schritte

1. ✅ `.env` einrichten
2. ✅ `npm run digest:now` testen
3. ✅ E-Mail oder Notion konfigurieren (optional)
4. ✅ `npm run digest:schedule` für tägliche Ausführung starten
5. 📖 Customize den Prompt für deine spezifischen Interessen

---

**Fragen?** Check die Docs oder optimier den Prompt in `news-digest.ts` für deine Needs!
