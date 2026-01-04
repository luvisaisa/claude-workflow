---
description: generate comprehensive test suite for specified module or function
allowed-tools: Read, Glob, Grep, Write, Bash(pytest:*)
argument-hint: required: source_path
---

# Test Generate

Generate test file for existing module.

## Arguments

- $MODULE_PATH — path to module to test (e.g., "src/services/parser.py")

## Steps

1. Read and analyze the module:
   - Identify all public functions/classes
   - Understand parameters and return types
   - Identify dependencies to mock
   - Note edge cases from logic

2. Read existing test patterns in project

3. Generate test file: `tests/{mirrored_path}/test_{module_name}.py`
   ```python
   from __future__ import annotations
   import pytest
   from unittest.mock import Mock, patch
   
   from {module_import} import {items_to_test}
   
   
   class TestClassName:
       """Tests for ClassName."""
       
       @pytest.fixture
       def instance(self):
           """Create test instance."""
           return ClassName()
       
       def test_method_happy_path(self, instance):
           """Test method with valid input."""
           result = instance.method(valid_input)
           assert result == expected
       
       def test_method_invalid_input(self, instance):
           """Test method rejects invalid input."""
           with pytest.raises(ValueError):
               instance.method(invalid_input)
       
       def test_method_edge_case(self, instance):
           """Test method handles edge case."""
           result = instance.method(edge_case_input)
           assert result == expected
   ```

4. Run generated tests:
   ```bash
   pytest {test_file} -v
   ```

5. Report:
   ```
   [Test Generate] Created {test_file}
   
   Test cases:
   - {list of test functions}
   
   Results: {passed}/{total} passing
   
   Coverage added: {percentage}
   ```
