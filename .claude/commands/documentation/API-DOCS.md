---
description: generate api documentation from code with examples
allowed-tools: Read, Grep, Glob, Write
argument-hint: optional: api_path
---

# API Docs

Generate OpenAPI descriptions for FastAPI endpoints.

## Arguments

- $TARGET — router file or "all"

## Steps

1. Read endpoint definitions

2. For each endpoint, ensure:
   - `summary` parameter is set
   - `description` parameter explains behavior
   - `response_description` is set
   - Request/response models have Field descriptions
   - Tags are appropriate

3. Update endpoint decorators:
   ```python
   @router.post(
       "/items",
       summary="Create a new item",
       description="Creates a new item with the provided data. Returns the created item.",
       response_description="The created item",
       tags=["items"],
   )
   ```

4. Update Pydantic models:
   ```python
   class ItemCreate(BaseModel):
       name: str = Field(..., description="The item name", example="Widget")
       status: Status = Field(default=Status.DRAFT, description="Initial status")
   ```

5. Verify docs render:
   ```
   Check /docs or /redoc endpoint
   ```

6. Report:
   ```
   [API Docs] Updated
   
   Endpoints documented: {count}
   Models documented: {count}
   
   Files modified:
   - {file}
   ```
