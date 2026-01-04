---
description: create fastapi endpoint with validation, tests, and documentation
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(pytest:*)
argument-hint: required: route_path method description
---

# New Endpoint

Scaffold a new FastAPI endpoint with full structure.

## Arguments

- $ENDPOINT_NAME — name of the endpoint (e.g., "users", "annotations")
- $METHODS — HTTP methods to support (e.g., "crud", "get,post", "get")

## Steps

1. Read existing endpoints in `src/api/` or `app/api/` to understand patterns

2. Create route file: `src/api/routes/{endpoint_name}.py`
   - Import FastAPI Router
   - Define Pydantic request/response schemas (or import from schemas/)
   - Implement route handlers
   - Follow existing authentication/dependency patterns

3. Create schema file if complex: `src/schemas/{endpoint_name}.py`
   - Request models with validation
   - Response models
   - Use existing base schemas if available

4. Create service file: `src/services/{endpoint_name}_service.py`
   - Business logic separated from route handlers
   - Database operations via SQLAlchemy
   - Follow existing service patterns

5. Create test file: `tests/api/test_{endpoint_name}.py`
   - Test each endpoint method
   - Include happy path and error cases
   - Use existing test fixtures/factories

6. Register router in main app file

7. Run verification:
   ```bash
   pytest tests/api/test_{endpoint_name}.py -v
   mypy src/api/routes/{endpoint_name}.py
   ruff check src/api/routes/{endpoint_name}.py
   ```

8. Report created files and test results
