---
description: create data adapter following existing adapter pattern with registry
allowed-tools: Read, Glob, Grep, Write, Bash(pytest:*)
argument-hint: required: adapter_name source_type
---

# New Adapter

Create adapter following BaseAdapter pattern with registry entry.

## Arguments

- $ADAPTER_NAME — name of the adapter (e.g., "LIDC", "NLST")
- $SOURCE_TYPE — type of data source (e.g., "xml", "csv", "dicom")

## Steps

1. Read existing adapters to understand:
   - BaseAdapter interface
   - Required method signatures
   - AdapterRegistry pattern
   - Configuration patterns

2. Create adapter file: `src/adapters/{adapter_name.lower()}_adapter.py`
   ```python
   from __future__ import annotations
   from typing import Any
   from .base import BaseAdapter
   from .registry import AdapterRegistry
   
   
   @AdapterRegistry.register("{adapter_name.lower()}")
   class {AdapterName}Adapter(BaseAdapter):
       """Adapter for {AdapterName} data source."""
       
       def __init__(self, config: dict[str, Any] | None = None):
           super().__init__(config)
           # Adapter-specific initialization
       
       def validate_source(self, source: Any) -> bool:
           """Validate that source is compatible with this adapter."""
           raise NotImplementedError
       
       def extract(self, source: Any) -> dict[str, Any]:
           """Extract data from source."""
           raise NotImplementedError
       
       def transform(self, data: dict[str, Any]) -> dict[str, Any]:
           """Transform extracted data to standard format."""
           raise NotImplementedError
       
       def get_confidence(self, source: Any) -> float:
           """Return confidence score (0-1) that this adapter handles the source."""
           raise NotImplementedError
   ```

3. Add adapter to `src/adapters/__init__.py` exports

4. Create test file: `tests/adapters/test_{adapter_name.lower()}_adapter.py`
   - Test validation logic
   - Test extraction with sample data
   - Test transformation output format
   - Test confidence scoring
   - Test error handling

5. Create sample fixture data if needed: `tests/fixtures/{adapter_name.lower()}/`

6. Run verification:
   ```bash
   pytest tests/adapters/test_{adapter_name.lower()}_adapter.py -v
   mypy src/adapters/{adapter_name.lower()}_adapter.py
   ```

7. Report created files and test results
