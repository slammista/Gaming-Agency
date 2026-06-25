# Game Studio OS

> Un sistema multi-agente che trasforma Claude Code nel tuo studio di sviluppo videoludico.  
> 53 agenti specializzati. Una Knowledge Base condivisa. Zero overhead manuale.

---

## Cos'è

Game Studio OS replica la struttura organizzativa di uno studio professionale AAA all'interno di Claude Code. Ogni membro del team — dal Game Director al Dialogue Writer, dal Concept Artist al QA Lead — è un agente autonomo con ruolo definito, autorità precisa e accesso limitato alla Knowledge Base.

Non è un chatbot a cui chiedere idee. È un sistema di produzione: i contenuti vengono creati, validati dal QA, approvati dal Director e salvati nella Knowledge Base in formato Markdown pronto all'uso.

```
Utente → Game Director → Orchestratori di macroarea → Specialist → KB → QA → Approvazione
```

---

## Agenti inclusi (53)

| Prefisso | Macroarea | Agenti |
|---|---|---|
| `dir-` | Direzione | Game Director, Producer, Art/Narrative/Technical Director, Lead Designer, PM |
| `design-` | Game Design | World, Game, Systems, Quest, Character, Level, Encounter Designer |
| `narr-` | Narrativa | Narrative Designer, Lore Designer/Writer, Dialogue Writer, Character Writer, Content Writer, Technical Designer |
| `viz-` | Visual & Audio | Concept Artist, 3D Character/Environment Artist, Texture Artist, Rigger, Animator, UI/UX, VFX, Sound Designer, Composer, Technical Artist |
| `qa-` | Quality Assurance | QA Lead, QA Tester, Narrative QA, UX Researcher, Cross-Domain Validator, Security Guard |
| `biz-` | Business & Lancio | Marketing Manager, PR Manager, Community Manager, Data Analyst, Live Ops Producer, Customer Support, Video Editor, Localization Manager |
| `prog-` | Programmazione | Lead, Gameplay, UI, AI, Tools, Audio Programmer *(STUB — attivi solo con codebase reale)* |
| infra | Infrastruttura KB | KB Librarian *(auto-index e session manifest)* |

---

## Setup consigliato: Claude Code IDE o Terminale

> **Raccomandato:** usa Claude Code nel **terminale** o nell'**estensione IDE** (VS Code / JetBrains).  
> Il motivo è semplice: lì hai pieno controllo sul contesto, puoi lavorare nella cartella del progetto e gli agenti accedono direttamente ai file della Knowledge Base senza intermediari.

### 1. Clona il repo

```bash
git clone https://github.com/slammista/Gaming-Agency.git
cd Gaming-Agency
```

### 2. Avvia Claude Code nella cartella

```bash
claude
```

Claude legge automaticamente `CLAUDE.md` (la costituzione del progetto) e scopre tutti i 53 agenti in `.claude/agents/`. Nessuna configurazione aggiuntiva richiesta.

### 3. In alternativa: Claude Code Web

Se non hai Claude Code in locale, puoi usare [claude.ai/code](https://claude.ai/code) (richiede piano Pro, Max o Team):

1. Connetti il tuo account GitHub
2. Seleziona la repository `Gaming-Agency`
3. Claude carica automaticamente gli agenti dalla repo

> L'IDE/terminale rimane la scelta preferita perché garantisce sessioni persistenti, accesso diretto al filesystem e nessuna latenza di sync con GitHub.

---

## Come si usa

Non serve sintassi speciale. Descrivi il task in linguaggio naturale e Claude dispaccia automaticamente l'agente giusto leggendo le `description` in `.claude/agents/`.

**Esempi:**

```
"Crea il world design del continente principale"
→ dispatcha design-world-designer

"Scrivi il dialogo di apertura tra il protagonista e il villain"
→ dispatcha narr-dialogue-writer

"Valida la coerenza tra il lore e le quest create oggi"
→ dispatcha qa-cross-domain

"Approva gli asset in pending"
→ dispatcha dir-game-director (batch approval)
```

**Per forzare un agente specifico:**

```
"Usa l'agente design-quest-designer per progettare la quest del villaggio abbandonato"
```

**Per task multi-agente (consigliato: chiama l'orchestratore):**

```
"Chiedi a dir-lead-game-designer di coordinare world design e narrative per la prima area"
```

L'orchestratore gestisce in autonomia il dispatch agli specialist e la raccolta degli output.

---

## Knowledge Base

Tutti i contenuti prodotti vengono salvati in `knowledge_base/` in formato Markdown strutturato:

```
knowledge_base/
├── world/          characters/     factions/       regions/        timeline/
├── narrative/      dialogue/       lore/
├── quests/         systems/        levels/
├── art_direction/  assets_visual/  assets_audio/
├── production/     marketing/      live_ops/
├── qa_reports/     staging/        i18n/
└── INDEX.md        (aggiornato automaticamente da kb-librarian)
```

Ogni agente legge **solo** le cartelle di sua competenza (`can_modify` + `reads_from` nel proprio file). Nessuno carica l'intera KB.

---

## Modalità operativa

Configurabile in `knowledge_base/production/config.md`:

| Mode | Comportamento |
|---|---|
| `PROD` *(default)* | Scrittura diretta nella KB |
| `DRY-RUN` | Output in `knowledge_base/staging/` — KB ufficiale intatta |

---

## Costi

| Agente | Modello | Perché |
|---|---|---|
| `qa-tester`, `qa-security-guard`, `kb-librarian`, `biz-customer-support-specialist`, `prog-*` | **Haiku** | Compiti ripetitivi/checklist, nessun giudizio creativo |
| Tutti gli altri | **Sonnet** | Giudizio creativo, orchestrazione, scrittura |

Puoi cambiare il modello di qualsiasi agente modificando il campo `model` nel suo file `.claude/agents/<slug>.md`.

---

## File chiave

| File | Ruolo |
|---|---|
| `CLAUDE.md` | Costituzione del progetto — sempre in context, regole assolute |
| `.claude/RULES_BASE.md` | Regole universali ereditate da tutti gli agenti |
| `roles.json` | Sorgente di verità degli agenti (can_modify, reads_from, model) |
| `scripts/generate_agents.py` | Rigenera i file agente da roles.json |
| `knowledge_base/INDEX.md` | Indice navigabile della KB |
| `knowledge_base/production/session_manifest.md` | Checkpointing sessione — il Director lo legge all'avvio |
| `knowledge_base/production/pending_approval.md` | Coda batch approval per il Director |
| `logs/TRANSACTION_LOG.md` | Log unificato di tutte le modifiche alla KB |
