---
role: system
date: 2026-06-25
description: Coda di batch approval per dir-game-director. Gli orchestratori accodano qui gli asset validati da qa-lead invece di chiamare il Director per ogni singolo file.
---

# Pending Approval Queue

Gli orchestratori appendono asset in questa tabella dopo che `qa-lead` ha validato. Il Director legge qui e approva/rifiuta in batch (max 10 per sessione).

**Come accodare (per orchestratori):**
Aggiungi una riga con `status: pending`:
`| <timestamp> | <path/file.md> | <agente-autore> | <breve-descrizione> | pending |`

**Come processare (per dir-game-director):**
1. Leggi questa tabella
2. Per ogni riga `pending`: leggi il file, decidi, aggiorna `status` → `approved` o `rejected`
3. Aggiorna il frontmatter del file KB con `status: approved`
4. Log in `logs/TRANSACTION_LOG.md`

---

| Timestamp | File | Autore | Descrizione | Status |
|---|---|---|---|---|
| — | — | — | *(nessun asset in coda)* | — |
