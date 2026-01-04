# Seed

Generate seed data for development/testing.

## Arguments

- $MODELS — models to seed (e.g., "users,annotations" or "all")
- $COUNT — number of records per model (default: 10)

## Steps

1. Read existing seed scripts or factories in:
   - `tests/factories/`
   - `scripts/seed.py`
   - `src/db/seeds/`

2. Check for existing factory patterns (Factory Boy, custom factories)

3. Generate seed script or use existing:
   ```python
   # Generate realistic test data
   # Use Faker for realistic values
   # Respect foreign key relationships
   # Handle unique constraints
   ```

4. Run seed in development database only:
   ```bash
   # Confirm we're not in production
   # Execute seed script
   ```

5. Report:
   ```
   [Seed] Generated data
   
   - {Model}: {count} records
   - {Model}: {count} records
   
   Sample IDs for testing:
   - {model}: {id}
   ```
