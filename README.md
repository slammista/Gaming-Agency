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

## Installazione e setup — Guida completa per principianti

> **Metodo consigliato: Claude Code nel terminale o nell'IDE.**
> Rispetto alla versione web, hai sessioni persistenti, accesso diretto ai file della KB e nessuna latenza di sync. Gli agenti funzionano meglio quando possono leggere e scrivere file localmente in tempo reale.

---

### Prerequisiti

Prima di iniziare, assicurati di avere:

- **Node.js 18 o superiore** — verifica con `node --version`. Se non ce l'hai, scaricalo da [nodejs.org](https://nodejs.org).
- **Git** — verifica con `git --version`. Di solito è già installato su Mac e Linux. Su Windows usa [git-scm.com](https://git-scm.com).
- **Un account Anthropic** — il piano Free funziona, ma è consigliato il piano **Pro** per usare Claude Code in modo continuativo nel terminale (limiti di utilizzo più alti e accesso a Sonnet senza interruzioni).

---

### Passo 1 — Installa Claude Code

Apri il terminale ed esegui:

```bash
npm install -g @anthropic-ai/claude-code
```

Verifica che l'installazione sia andata a buon fine:

```bash
claude --version
```

Dovresti vedere un numero di versione (es. `1.x.x`). Se il comando non viene trovato, chiudi e riapri il terminale.

---

### Passo 2 — Autenticati con il tuo account Anthropic

```bash
claude
```

Al primo avvio Claude Code ti chiederà di autenticarti. Segui le istruzioni a schermo:

1. Verrà aperta automaticamente una pagina nel browser su `claude.ai`
2. Accedi con il tuo account Anthropic
3. Autorizza Claude Code
4. Torna al terminale — vedrai il prompt `>` che indica che sei pronto

> Se preferisci autenticarti con una API Key invece del browser:
> ```bash
> export ANTHROPIC_API_KEY=sk-ant-...
> claude
> ```

---

### Passo 3 — Porta il sistema nel tuo progetto

Game Studio OS non va usato direttamente come repository condivisa: va integrato **nel tuo progetto**, che avrà la sua repo GitHub indipendente con la sua Knowledge Base.

Hai due strade:

---

#### Opzione A — Usa questa repo come template (consigliato per iniziare da zero)

Vai su [github.com/slammista/Gaming-Agency](https://github.com/slammista/Gaming-Agency) e clicca **"Use this template" → "Create a new repository"**.

GitHub creerà una copia identica nella tua repository personale (`tuousername/NomeDelTuoGioco`), completamente scollegata da questa. Da quel momento lavori in autonomia sulla tua copia.

Poi clona la tua nuova repo in locale:

```bash
git clone https://github.com/tuousername/NomeDelTuoGioco.git
cd NomeDelTuoGioco
```

---

#### Opzione B — Integra gli agenti in un progetto già esistente

Se hai già una cartella/repo con il tuo progetto videoludico, puoi copiare solo i file necessari del sistema:

```bash
# Clona temporaneamente questa repo in una cartella separata
git clone https://github.com/slammista/Gaming-Agency.git /tmp/game-studio-os

# Entra nella cartella del TUO progetto
cd /path/al/tuo/progetto

# Copia i file del sistema
cp -r /tmp/game-studio-os/.claude .
cp /tmp/game-studio-os/CLAUDE.md .
cp -r /tmp/game-studio-os/knowledge_base .
cp -r /tmp/game-studio-os/logs .
cp /tmp/game-studio-os/roles.json .
cp -r /tmp/game-studio-os/scripts .

# Rimuovi la repo temporanea
rm -rf /tmp/game-studio-os
```

Aggiungi e committa tutto nel tuo progetto:

```bash
git add .
git commit -m "Add Game Studio OS multi-agent system"
git push
```

> La cartella `knowledge_base/` parte vuota — si popola man mano che gli agenti lavorano. Non condividerai mai i contenuti con altri utenti di questo template.

---

### Passo 4 — Avvia Claude Code nella cartella del tuo progetto

```bash
claude
```

**Importante:** il comando va eseguito **dentro** la cartella del tuo progetto. Claude Code legge automaticamente:

- `CLAUDE.md` — la costituzione del progetto (regole, architettura, modalità operativa)
- `.claude/agents/*.md` — tutti i 53 agenti specializzati
- `.claude/RULES_BASE.md` — le regole universali ereditate da tutti gli agenti

Non devi fare nulla di speciale: basta avviare `claude` nella cartella giusta e il sistema è operativo.

---

### Passo 5 — Verifica che gli agenti siano caricati

Una volta dentro Claude Code, digita:

```
/agents
```

Vedrai la lista di tutti gli agenti disponibili con la loro descrizione. Se vedi i 53 agenti (da `biz-community-manager` a `viz-vfx-artist`) il setup è completo.

> Se non vedi gli agenti, assicurati di aver avviato `claude` dalla cartella `Gaming-Agency` e non da un'altra directory.

---

### Passo 6 — Prima sessione: inizia con il Game Director

Per un nuovo progetto, il punto di ingresso consigliato è sempre il Game Director:

```
Sono in fase di pre-produzione. Voglio creare un gioco di ruolo fantasy dark.
Chiedi al Game Director di avviare il progetto e definire la visione creativa.
```

Il Game Director leggerà `knowledge_base/production/session_manifest.md` per capire lo stato del progetto (vuoto la prima volta), e potrà iniziare a delegare agli orchestratori di macroarea.

---

### Setup opzionale: estensione VS Code

Se preferisci lavorare nell'IDE invece del terminale:

1. Apri VS Code
2. Vai su **Extensions** (`Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Cerca **"Claude Code"** e installa l'estensione Anthropic
4. Apri la cartella `Gaming-Agency` in VS Code (`File → Open Folder`)
5. Usa il pannello Claude Code nella sidebar — stesso comportamento del terminale

---

### Setup alternativo: Claude Code Web (senza installazione)

Se non vuoi installare nulla in locale, puoi usare [claude.ai/code](https://claude.ai/code) (richiede piano Pro, Max o Team):

1. Vai su [claude.ai/code](https://claude.ai/code) e accedi
2. Clicca **"Connect GitHub"** e autorizza l'accesso
3. Seleziona la repository `slammista/Gaming-Agency`
4. Claude carica automaticamente gli agenti dalla repo

> Limitazione: le sessioni web si chiudono dopo un periodo di inattività. Per progetti lunghi con tanta KB da costruire, il terminale è più stabile.

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
