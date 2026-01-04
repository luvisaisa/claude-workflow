# Test Edge Cases

Analyze function and add edge case tests.

## Arguments

- $FUNCTION_PATH — path to function (e.g., "src/services/parser.py:parse_content")

## Steps

1. Read and analyze the function:
   - Input parameters and types
   - Conditional branches
   - Loop boundaries
   - Error handling paths
   - External dependencies

2. Identify edge cases:
   - Empty inputs (None, "", [], {})
   - Boundary values (0, -1, MAX_INT)
   - Type variations (if accepting multiple types)
   - Malformed inputs
   - Concurrent access (if applicable)
   - Resource exhaustion

3. Find existing test file or create new

4. Add edge case tests:
   ```python
   class TestFunctionEdgeCases:
       """Edge case tests for function."""
       
       @pytest.mark.parametrize("input,expected", [
           (None, ...),
           ("", ...),
           ([], ...),
       ])
       def test_empty_inputs(self, input, expected):
           ...
       
       def test_boundary_values(self):
           ...
       
       def test_malformed_input(self):
           ...
   ```

5. Run tests:
   ```bash
   pytest {test_file} -v -k "edge"
   ```

6. Report added test cases and results
