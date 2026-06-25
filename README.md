# 🎮 Agentic Game Studio

> **Trasforma Claude Code nel tuo studio AAA di sviluppo videoludico.**
> 53 agenti specializzati. Una Knowledge Base condivisa. Pipeline di produzione completa.

[![Claude Code](https://img.shields.io/badge/Claude_Code-Terminal_%2F_IDE-8A2BE2?style=flat-square&logo=anthropic)](https://claude.ai/code)
[![Agents](https://img.shields.io/badge/Agenti-53-blue?style=flat-square)](/.claude/agents)
[![Model](https://img.shields.io/badge/Model-Sonnet_%2F_Haiku-green?style=flat-square)](https://anthropic.com)
[![License](https://img.shields.io/badge/Licenza-MIT-yellow?style=flat-square)](LICENSE)

---

## Cos'è

Agentic Game Studio replica la struttura di uno **studio professionale AAA** direttamente in Claude Code. Ogni membro del team — dal Game Director al Dialogue Writer, dal Concept Artist al QA Lead — è un agente autonomo con ruolo definito, autorità precisa e accesso limitato alla Knowledge Base.

Non è un chatbot a cui chiedere idee. È un **sistema di produzione**: i contenuti vengono creati, validati dal QA, approvati dal Director e salvati nella Knowledge Base in Markdown pronto all'uso.

> ⚠️ **Funziona solo con Claude Code (terminale/IDE).** Claude Desktop non supporta il sistema di agenti con accesso al filesystem. Vedi la [sezione installazione](#installazione-e-setup--guida-completa).

---

## 🏢 L'ecosistema dello studio

```
┌─────────────────────────────────────────────────────────────────┐
│                        🎮 AGENTIC GAME STUDIO                        │
│                                                                 │
│                    👤 UTENTE (tu)                               │
│                         │                                       │
│                         ▼                                       │
│              ┌─────────────────────┐                            │
│              │   🎬 GAME DIRECTOR  │  ← Visione, approvazioni   │
│              │   dir-game-director │    batch, arbitraggio      │
│              └──────────┬──────────┘                            │
│                         │ dispatcha                             │
│         ┌───────────────┼───────────────┐                       │
│         ▼               ▼               ▼                       │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐                   │
│   │ 🎨 ART   │   │ ✍️ NARR  │   │ 🕹️ DESIGN│  + altri...      │
│   │ DIRECTOR │   │ DIRECTOR │   │ LEAD     │                   │
│   └────┬─────┘   └────┬─────┘   └────┬─────┘                   │
│        │              │              │                          │
│        ▼              ▼              ▼                          │
│   Specialist      Specialist     Specialist                     │
│   viz-*           narr-*         design-*                       │
│        │              │              │                          │
│        └──────────────┼──────────────┘                          │
│                       ▼                                         │
│              ┌─────────────────┐                                │
│              │  📚 KNOWLEDGE   │  ← Tutto salvato in            │
│              │     BASE        │    Markdown strutturato        │
│              └────────┬────────┘                                │
│                       │                                         │
│                       ▼                                         │
│              ┌─────────────────┐                                │
│              │  🔍 QA LEAD     │  ← Valida prima               │
│              │  + cross-domain │    dell'approvazione           │
│              └────────┬────────┘                                │
│                       │                                         │
│                       ▼                                         │
│              ✅ APPROVAZIONE DIRECTOR                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ I dipartimenti

```
┌────────────────────┬──────────────────────────────────────────────────────┐
│ 🎬 DIREZIONE       │ Game Director · Producer · Art/Narrative/Technical    │
│ dir-*              │ Director · Lead Designer · Project Manager            │
├────────────────────┼──────────────────────────────────────────────────────┤
│ 🕹️ GAME DESIGN     │ World · Game · Systems · Quest · Character ·          │
│ design-*           │ Level · Encounter Designer                            │
├────────────────────┼──────────────────────────────────────────────────────┤
│ ✍️ NARRATIVA        │ Narrative Designer · Lore Designer/Writer ·           │
│ narr-*             │ Dialogue Writer · Character Writer · Content Writer   │
├────────────────────┼──────────────────────────────────────────────────────┤
│ 🎨 VISUAL & AUDIO  │ Concept Artist · 3D Character/Environment Artist ·    │
│ viz-*              │ Texture · Rigger · Animator · UI/UX · VFX ·           │
│                    │ Sound Designer · Composer · Technical Artist          │
├────────────────────┼──────────────────────────────────────────────────────┤
│ 🔍 QUALITY         │ QA Lead · QA Tester · Narrative QA · UX Researcher ·  │
│ qa-*               │ Cross-Domain Validator · Security Guard               │
├────────────────────┼──────────────────────────────────────────────────────┤
│ 📣 BUSINESS        │ Marketing Manager · PR Manager · Community Manager ·  │
│ biz-*              │ Data Analyst · Live Ops Producer · Customer Support · │
│                    │ Video Editor · Localization Manager                   │
├────────────────────┼──────────────────────────────────────────────────────┤
│ 💻 PROGRAMMAZIONE  │ Lead · Gameplay · UI · AI · Tools · Audio Programmer  │
│ prog-* (STUB)      │ ⚠️ Attivi solo quando esiste una codebase reale        │
├────────────────────┼──────────────────────────────────────────────────────┤
│ 📚 INFRASTRUTTURA  │ KB Librarian (auto-index · session manifest)          │
└────────────────────┴──────────────────────────────────────────────────────┘
```

---

## 📚 La Knowledge Base

Ogni contenuto prodotto viene salvato automaticamente in `knowledge_base/`, organizzato per dominio. Gli agenti leggono **solo** le cartelle di loro competenza — nessuno carica l'intera KB.

```
knowledge_base/
│
├── 🌍 world/           → continenti, geografia
├── 👥 characters/      → schede personaggio
├── ⚔️  factions/        → fazioni e organizzazioni
├── 🗺️  regions/         → regioni e città
├── 📅 timeline/        → cronologia eventi
│
├── 📖 narrative/       → trama, archi, finali
├── 💬 dialogue/        → dialoghi e scene
├── 📜 lore/            → lore, in-world documents
│
├── 🎯 quests/          → missioni principali e secondarie
├── ⚙️  systems/         → meccaniche, economia, bilanciamento
├── 🏰 levels/          → layout, blockout, encounter
│
├── 🎨 art_direction/   → stile visivo e mood board
├── 🖼️  assets_visual/   → concept, 3D, texture, UI, VFX
├── 🎵 assets_audio/    → musica e sound effects
│
├── 📊 production/      → GDD, roadmap, sessioni, approvazioni
├── 📣 marketing/       → strategia, store page, press kit
├── 📈 live_ops/        → eventi, metriche, supporto
│
├── ✅ qa_reports/      → bug, report narrativi, UX
├── 🌐 i18n/            → traduzioni per lingue attive
└── 🧪 staging/         → output DRY-RUN (non approvati)
```

---

## ⚡ Come funziona in pratica

Non serve sintassi speciale. Scrivi in linguaggio naturale e Claude dispaccia l'agente giusto.

```
Tu scrivi:                              Claude attiva:
────────────────────────────────────────────────────────
"Crea il continente principale"     →   design-world-designer
"Scrivi il dialogo col villain"     →   narr-dialogue-writer
"Bilancia il sistema di crafting"   →   design-systems-designer
"Concept art per il protagonista"   →   viz-concept-artist
"Valida la coerenza world/lore"     →   qa-cross-domain
"Approva gli asset in pending"      →   dir-game-director
```

**Per forzare un agente specifico:**
```
"Usa design-quest-designer per la quest del villaggio abbandonato"
```

**Per task complessi (usa l'orchestratore di macroarea):**
```
"Chiedi a dir-lead-game-designer di coordinare world design e
narrative per la prima area di gioco"
```
L'orchestratore gestisce in autonomia il dispatch agli specialist.

---

## 🔄 Pipeline di produzione

```
  CREAZIONE          VALIDAZIONE         APPROVAZIONE
      │                   │                   │
      ▼                   ▼                   ▼
┌──────────┐       ┌──────────┐        ┌──────────────┐
│Specialist│──────▶│ qa-lead  │───────▶│ dir-game-    │
│  agent   │       │    +     │        │   director   │
│          │       │ cross-   │        │ (batch, max  │
│ draft    │       │ domain   │        │  10 asset)   │
└──────────┘       └──────────┘        └──────┬───────┘
                                              │
                                              ▼
                                    knowledge_base/
                                    status: approved ✅
```

---

## 🛠️ Installazione e setup — Guida completa

> **Metodo consigliato: Claude Code nel terminale o nell'IDE.**
> Rispetto alla versione web, hai sessioni persistenti, accesso diretto ai file e nessuna latenza. Gli agenti funzionano meglio quando leggono e scrivono file localmente in tempo reale.

---

### Prerequisiti

| Strumento | Verifica | Link |
|---|---|---|
| **Node.js 18+** | `node --version` | [nodejs.org](https://nodejs.org) |
| **Git** | `git --version` | [git-scm.com](https://git-scm.com) |
| **Account Anthropic** | — | Il piano Free funziona; il piano **Pro** è consigliato per sessioni lunghe e limiti più alti |

---

### Passo 1 — Installa Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Verifica:

```bash
claude --version
# Output atteso: 1.x.x
```

Se il comando non viene trovato, chiudi e riapri il terminale.

---

### Passo 2 — Autenticati

```bash
claude
```

Al primo avvio si apre automaticamente il browser su `claude.ai`. Accedi, autorizza Claude Code, torna al terminale. Vedrai il prompt `>`.

> Alternativa con API Key:
> ```bash
> export ANTHROPIC_API_KEY=sk-ant-...
> claude
> ```

---

### Passo 3 — Porta il sistema nel tuo progetto

> ⚠️ **Non lavorare direttamente su questa repo.** Crea la tua copia indipendente: ogni progetto ha la propria Knowledge Base e i propri contenuti.

#### Opzione A — Template GitHub (consigliato, per chi parte da zero)

Vai su [github.com/slammista/agentic-game-studio](https://github.com/slammista/agentic-game-studio), clicca **"Use this template" → "Create a new repository"** e crea la tua copia personale.

Poi clona la tua repo:

```bash
git clone https://github.com/tuousername/NomeDelTuoGioco.git
cd NomeDelTuoGioco
```

#### Opzione B — Integra in un progetto già esistente

Se hai già una repo con il tuo gioco, copia solo i file del sistema:

```bash
# Clona temporaneamente questa repo
git clone https://github.com/slammista/agentic-game-studio.git /tmp/agentic-game-studio

# Entra nella TUA cartella di progetto
cd /path/al/tuo/progetto

# Copia i file del sistema
cp -r /tmp/agentic-game-studio/.claude .
cp    /tmp/agentic-game-studio/CLAUDE.md .
cp -r /tmp/agentic-game-studio/knowledge_base .
cp -r /tmp/agentic-game-studio/logs .
cp    /tmp/agentic-game-studio/roles.json .
cp -r /tmp/agentic-game-studio/scripts .

# Rimuovi la repo temporanea
rm -rf /tmp/agentic-game-studio

# Committa nel tuo progetto
git add .
git commit -m "Add Agentic Game Studio multi-agent system"
git push
```

> La `knowledge_base/` parte vuota e si popola man mano. I tuoi contenuti non sono mai condivisi con altri utenti del template.

---

### Passo 4 — Avvia Claude Code nella cartella del progetto

```bash
cd NomeDelTuoGioco   # o la cartella del tuo progetto
claude
```

Claude legge automaticamente `CLAUDE.md` e scopre tutti i 53 agenti in `.claude/agents/`. Nessuna configurazione aggiuntiva.

---

### Passo 5 — Verifica che gli agenti siano caricati

```
/agents
```

Dovresti vedere 53 agenti elencati (da `biz-community-manager` a `viz-vfx-artist`). Se non li vedi, assicurati di essere nella cartella giusta.

---

### Passo 6 — Prima sessione

```
Sono in pre-produzione. Voglio creare un gioco di ruolo fantasy dark.
Chiedi al Game Director di avviare il progetto e definire la visione creativa.
```

Il Game Director legge `knowledge_base/production/session_manifest.md` per lo stato del progetto e inizia a delegare agli orchestratori.

---

### Alternativa: estensione VS Code

1. Apri VS Code → **Extensions** (`Ctrl+Shift+X` / `Cmd+Shift+X`)
2. Cerca **"Claude Code"** → installa l'estensione Anthropic
3. Apri la cartella del tuo progetto
4. Usa il pannello Claude Code nella sidebar

---

### Alternativa: Claude Code Web

[claude.ai/code](https://claude.ai/code) — connetti GitHub, seleziona la tua repo, Claude carica gli agenti automaticamente. Richiede piano Pro/Max/Team.

> Limitazione: le sessioni web si chiudono per inattività. Per progetti lunghi usa il terminale.

---

## 💰 Modelli e costi

| Agenti | Modello | Motivo |
|---|---|---|
| `qa-tester` · `qa-security-guard` · `kb-librarian` · `biz-customer-support-specialist` · `prog-*` | **Haiku** *(economico)* | Compiti ripetitivi/checklist |
| Tutti gli altri (director, orchestratori, designer, writer) | **Sonnet** | Giudizio creativo e orchestrazione |

Cambia modello modificando il campo `model` in qualsiasi `.claude/agents/<slug>.md`.

---

## 🗄️ Modalità operativa

Configurabile in `knowledge_base/production/config.md`:

| Modalità | Comportamento |
|---|---|
| `PROD` *(default)* | Scrittura diretta nella Knowledge Base |
| `DRY-RUN` | Output in `knowledge_base/staging/` — KB ufficiale intatta |

---

## 📁 File chiave

| File | Ruolo |
|---|---|
| `CLAUDE.md` | Costituzione del progetto — sempre in context |
| `.claude/RULES_BASE.md` | Regole universali ereditate da tutti gli agenti |
| `roles.json` | Sorgente di verità: can_modify, reads_from, model per ogni agente |
| `scripts/generate_agents.py` | Rigenera i file agente da `roles.json` |
| `knowledge_base/INDEX.md` | Indice navigabile della KB (auto-aggiornato da kb-librarian) |
| `knowledge_base/production/session_manifest.md` | Checkpointing — il Director lo legge all'avvio |
| `knowledge_base/production/pending_approval.md` | Coda batch approval per il Director |
| `logs/TRANSACTION_LOG.md` | Log unificato di tutte le modifiche |

---

## ❓ Claude Desktop è supportato?

No. Gli agenti in `.claude/agents/` richiedono Claude Code (terminale/IDE) perché usano il **Task tool** per leggere e scrivere file nella Knowledge Base. Claude Desktop non supporta questo sistema. Per questo motivo la guida consiglia esclusivamente Claude Code da terminale o IDE.
