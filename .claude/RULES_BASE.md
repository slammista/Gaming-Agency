# Regole universali — Game Studio OS v1.0

Ereditate da **tutti** gli agenti in `.claude/agents/`. Ogni file agente sostituisce le 5 regole duplicate con `Eredita .claude/RULES_BASE.md`.

---

## Regole vincolanti

1. **Knowledge Base** — non ignorare la KB. Leggi solo le cartelle pertinenti al tuo campo `Autorità` prima di scrivere.
2. **Autorità** — non modificare nulla fuori dal campo `Autorità` del tuo file agente.
3. **Transaction Log** — registra ogni modifica in `logs/TRANSACTION_LOG.md` con formato tabella:
   `| <timestamp ISO8601> | <nome-agente> | CREATE|UPDATE|DELETE|VALIDATE|APPROVE|REJECT | <percorso/file.md> | <motivo breve> | draft|committed|approved|rejected |`
4. **QA Gate** — ogni contenuto nuovo passa per `qa-lead` prima dell'approvazione di `dir-game-director`.
5. **Dispatch** — uno specialist non dispatcha un altro specialist di pari livello. Segnala la dipendenza al tuo orchestratore di macroarea.
6. **File Locking** — prima di modificare un file KB:
   - Leggi il frontmatter del file target
   - Se `locked_by` non è `null`, segnala occupato all'orchestratore e attendi
   - Se `null`, scrivi `locked_by: <tuo-slug>` e `locked_at: <timestamp>`
   - Al termine, ripristina `locked_by: null` e `locked_at: null`
7. **Security pre-flight** — per Write/Edit su KB, invoca `qa-security-guard` se disponibile prima di procedere.
8. **Dry-Run** — se `knowledge_base/production/config.md` contiene `mode: DRY-RUN`, scrivi il diff proposto in `knowledge_base/staging/<percorso>` invece della KB ufficiale. Non toccare la KB reale.
9. **Context Summarization** — quando riporti al Director o al tuo orchestratore parent, includi sempre:
   - *Executive Summary* (max 200 token): decisioni prese, conflitti, stato
   - *Full Output*: solo se esplicitamente richiesto
10. **Coerenza prima di creatività** — la coerenza del progetto ha priorità sulla creatività. Mai introdurre regole di sistema senza il via libera di `dir-game-director`.
