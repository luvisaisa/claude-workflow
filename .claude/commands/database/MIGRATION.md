---
description: create alembic migration, review changes, and apply if approved
allowed-tools: Bash(alembic:*), Read, Grep
argument-hint: required: migration_message
---

# Migration

Generate Alembic migration from model changes.

## Arguments

- $MESSAGE — migration description (e.g., "add status column to annotations")

## Steps

1. Check for uncommitted model changes:
   ```bash
   git status src/models/
   ```

2. Verify current migration state:
   ```bash
   alembic current
   alembic check
   ```

3. Generate migration:
   ```bash
   alembic revision --autogenerate -m "$MESSAGE"
   ```

4. Review generated migration file:
   - Check upgrade() operations are correct
   - Check downgrade() operations are correct
   - Verify no unwanted changes detected
   - Check for data migrations needed

5. Report:
   ```
   [Migration] Created: {migration_file}
   
   Operations:
   - {list of detected changes}
   
   Review needed:
   - {any concerns or manual edits needed}
   ```

Do not run the migration — report only.
