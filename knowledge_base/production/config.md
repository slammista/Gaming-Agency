---
role: system
date: 2026-06-25
description: Configurazione operativa del Agentic Game Studio. Modificabile solo da dir-game-director.
---

# Config — Agentic Game Studio

## Modalità operativa

```yaml
mode: PROD
# Valori possibili:
# PROD     — scrittura diretta su KB (default)
# DRY-RUN  — ogni agente scrive il diff in knowledge_base/staging/ senza toccare la KB ufficiale
```

## Impostazioni globali

```yaml
default_language: it
batch_approval_limit: 10        # max asset per sessione di batch approval
lock_timeout_minutes: 30        # dopo quanto tempo un lock viene considerato stale
log_target: logs/TRANSACTION_LOG.md
staging_dir: knowledge_base/staging/
```

## Lingue attive per localizzazione

```yaml
locales:
  - it   # master
  # Aggiungi qui le lingue quando attivi biz-localization-manager:
  # - en
  # - es
  # - fr
  # - de
  # - ja
```
