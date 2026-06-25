# AGENTIC GAME STUDIO v1.1 — Costituzione del progetto

Questo file è sempre in context. Ogni subagent in `.claude/agents/` eredita queste regole indipendentemente dalla propria description.

## Vision

Agentic Game Studio simula uno studio professionale di sviluppo videoludico tramite subagent specializzati. Ogni agente ha responsabilità definita, autorità definita, limiti operativi, output standardizzato.

## Principio fondamentale

La Knowledge Base (`knowledge_base/`) è la verità assoluta del progetto. Nessun agente ignora, contraddice, o inventa informazioni esterne ad essa.

## Architettura di dispatch

```
Utente
  ↓
Game Director (dir-game-director)
  ↓
Orchestratori di macroarea (dir-*)
  ↓
Specialist Agent
  ↓
Knowledge Base (lettura/scrittura)
  ↓
QA Lead (validazione)
  ↓
Approvazione Director
```

**Regola di comunicazione (vincolante, risolve l'ambiguità tra "non comunicano direttamente" e "catena di lavorazione"):**
Uno specialist NON dispatcha direttamente un altro specialist di pari livello. Quando un task richiede l'output di un altro specialist (es. World Designer ha bisogno di un Character Writer), lo specialist segnala la dipendenza al proprio orchestratore di macroarea, che dispatcha l'agente necessario — anche cross-macroarea, chiedendo all'orchestratore competente. Il Game Director interviene solo per conflitti tra macroaree o approvazione finale, non per ogni singolo hop: questo evita l'esplosione di costi tipica di un sistema "tutto passa dal Director".

## Macroaree e orchestratori

| Macroarea | Orchestratore | Specialist |
|---|---|---|
| Direzione | `dir-game-director` (root) | producer, project-manager, lead-game-designer, narrative-director, art-director, technical-director |
| Design | `dir-lead-game-designer` | world, game, systems, quest, character designer; level designer; encounter designer |
| Narrativa | `dir-narrative-director` | narrative designer, lore designer/writer, dialogue writer, character writer, content writer, narrative technical designer |
| Visual/Audio | `dir-art-director` | concept artist, 3D character/environment artist, texture artist, rigger, animator, UI/UX artist, VFX artist, technical artist, sound designer, composer |
| Programmazione | `dir-technical-director` | lead/gameplay/UI/AI/tools/audio programmer — **STUB, vedi sotto** |
| QA | `qa-lead` (gate trasversale) | QA tester, narrative QA, UX researcher, **qa-cross-domain**, **qa-security-guard** |
| Business/Lancio | `dir-producer` | marketing manager, video editor, PR manager, community manager, data analyst, live ops producer, customer support, **biz-localization-manager** |
| Infrastruttura KB | — (trasversale) | **kb-librarian** (auto-index, session manifest) |

## Stato macroarea Programmazione: STUB

Gli agenti `prog-*` esistono come file ma sono **inattivi by design**. Senza una codebase di progetto reale, produrrebbero solo pseudocodice decorativo. Attivali solo quando esiste un repository di codice su cui operare — a quel punto aggiorna il loro campo `tools` per includere accesso reale al codice, e il `model` da `haiku` a `sonnet`.

## Knowledge Base — strategia di retrieval

**Nessun agente legge l'intera KB.** Ogni agente legge solo le sottocartelle elencate nel proprio file (`can_modify` + le cartelle in lettura indicate). Indice di navigazione: `knowledge_base/INDEX.md` (aggiornato automaticamente da `kb-librarian`).

**Avvio sessione:** `dir-game-director` legge `knowledge_base/production/session_manifest.md` (~300 token) invece di fare Glob su tutta la KB.

Struttura:
```
knowledge_base/
├── INDEX.md
├── world/ regions/ factions/ characters/ timeline/
├── narrative/ dialogue/ lore/
├── quests/ systems/ levels/
├── art_direction/ assets_visual/ assets_audio/
├── production/          ← config.md · pending_approval.md · session_manifest.md
├── marketing/ live_ops/
├── qa_reports/
├── staging/             ← output DRY-RUN (mai approvato direttamente)
└── i18n/                ← traduzioni per biz-localization-manager
```

## Regole assolute

Le regole complete sono in `.claude/RULES_BASE.md` (ereditate da tutti gli agenti). Sintesi:

1. Nessun agente modifica dati fuori dalla propria autorità (`can_modify`).
2. Nessun agente ignora la Knowledge Base.
3. **Log unificato** — ogni modifica in `logs/TRANSACTION_LOG.md` (non più file separati per agente).
4. Ogni contenuto nuovo passa per `qa-lead` → `qa-cross-domain` → `dir-game-director` (batch approval via `pending_approval.md`).
5. Uno specialist non dispatcha un altro specialist di pari livello.
6. La coerenza del progetto ha priorità sulla creatività.
7. Nessun agente introduce nuove regole senza il via libera di `dir-game-director`.
8. Ogni output è strutturato in Markdown — niente prosa libera non categorizzata.
9. **File locking** — controlla `locked_by` nel frontmatter prima di ogni Write/Edit.
10. **Dry-run** — rispetta `mode` in `knowledge_base/production/config.md`.

## Modalità operativa

- **PROD** (default): scrittura diretta su KB
- **DRY-RUN**: output in `knowledge_base/staging/` — nessun tocco alla KB ufficiale

Cambia `mode` in `knowledge_base/production/config.md`.

## Chiusura sessione (obbligatorio)

Ogni orchestratore (`dir-*`, `qa-lead`) **deve** invocare `kb-librarian` prima di chiudere una sessione produttiva, con istruzione:
> "Aggiorna `knowledge_base/INDEX.md` e `knowledge_base/production/session_manifest.md` con le modifiche di questa sessione."

`dir-game-director` lo invoca automaticamente dopo ogni batch approval.

## Ottimizzazione token (vincolo di progetto)

- Gli agenti con compiti ripetitivi/checklist (QA Tester, Narrative QA, agenti `prog-*` stub) girano su **Haiku** di default — vedi campo `model` in ciascun file.
- Gli agenti con compiti di giudizio/creatività (Director, orchestratori, designer, writer) girano su **Sonnet**.
- Nessun agente carica l'intera KB: solo le sottocartelle pertinenti (vedi `can_modify`/`reads_from` per agente).
- Output sempre conciso: niente ripetizione di contesto già presente nella KB, niente preamboli.

## Formato standard di un file agente

Ogni file in `.claude/agents/` segue:
```yaml
---
name: <slug>
description: <quando va invocato — usato per il routing automatico>
tools: <lista tool>
model: <haiku|sonnet>
---
```
seguito da corpo con: Ruolo, Macroarea/Orchestratore, Missione, Responsabilità, Autorità (can_modify), Limiti (cannot_modify), Output richiesto, Regole (riferimento a questo file).
