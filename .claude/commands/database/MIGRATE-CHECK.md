---
description: verify migration status, check for pending migrations
allowed-tools: Bash(alembic:*), Read
argument-hint: none
---

# Migrate Check

Dry-run migration, report what would change.

## Steps

1. Show current state:
   ```bash
   alembic current
   ```

2. Show pending migrations:
   ```bash
   alembic history --indicate-current
   ```

3. Generate SQL without executing:
   ```bash
   alembic upgrade head --sql
   ```

4. Report:
   ```
   [Migrate Check] Dry run results
   
   Current: {current revision}
   Target: {head revision}
   Pending migrations: {count}
   
   SQL that would run:
   {sql output}
   
   Tables affected:
   - {table list}
   ```

Do not execute any migrations.
