# New Model

Create SQLAlchemy model with standard fields and migration.

## Arguments

- $MODEL_NAME — name of the model (PascalCase, e.g., "Annotation")
- $TABLE_NAME — database table name (snake_case, e.g., "annotations")
- $FIELDS — field definitions (e.g., "name:str, status:enum, user_id:fk:users")

## Steps

1. Read existing models to understand patterns:
   - Base class usage
   - Mixin patterns (timestamps, soft delete, etc.)
   - Relationship definitions

2. Create model file: `src/models/{table_name}.py`
   ```python
   from __future__ import annotations
   import uuid
   from sqlalchemy import Column, String, DateTime, ForeignKey
   from sqlalchemy.dialects.postgresql import UUID
   from sqlalchemy.orm import relationship
   from sqlalchemy.sql import func
   from .base import Base
   
   class {ModelName}(Base):
       __tablename__ = "{table_name}"
       
       id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
       created_at = Column(DateTime(timezone=True), server_default=func.now())
       updated_at = Column(DateTime(timezone=True), onupdate=func.now())
       
       # Add fields based on $FIELDS argument
   ```

3. Add model to `src/models/__init__.py` exports

4. Generate Alembic migration:
   ```bash
   alembic revision --autogenerate -m "add {table_name} table"
   ```

5. Review generated migration for correctness

6. Create basic test: `tests/models/test_{table_name}.py`
   - Test model creation
   - Test required fields
   - Test relationships if any

7. Run verification:
   ```bash
   pytest tests/models/test_{table_name}.py -v
   mypy src/models/{table_name}.py
   ```

8. Report created files and migration
