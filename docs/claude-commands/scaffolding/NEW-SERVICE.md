# New Service

Create service class with dependency injection pattern.

## Arguments

- $SERVICE_NAME — name of the service (e.g., "AnnotationProcessor")
- $DEPENDENCIES — dependencies to inject (e.g., "db:Session, cache:Redis")

## Steps

1. Read existing services to understand:
   - Base service patterns
   - Dependency injection approach
   - Error handling conventions
   - Logging patterns

2. Create service file: `src/services/{service_name.lower()}_service.py`
   ```python
   from __future__ import annotations
   from typing import Any
   import logging
   
   logger = logging.getLogger(__name__)
   
   
   class {ServiceName}Service:
       """Service for {description}."""
       
       def __init__(self, {dependencies}):
           # Store injected dependencies
           pass
       
       async def process(self, data: Any) -> Any:
           """Main processing method."""
           raise NotImplementedError
   ```

3. Create test file: `tests/services/test_{service_name.lower()}_service.py`
   - Test with mocked dependencies
   - Test happy path
   - Test error cases
   - Test edge cases

4. Run verification:
   ```bash
   pytest tests/services/test_{service_name.lower()}_service.py -v
   mypy src/services/{service_name.lower()}_service.py
   ```

5. Report created files and test results
