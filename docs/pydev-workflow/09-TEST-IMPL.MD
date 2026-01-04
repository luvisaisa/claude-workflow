# pydev-workflow: Step 09 — Test Implementation

> **Workflow**: pydev-workflow  
> **Step**: 09-test-impl  
> **Previous**: 08-test-strategy  
> **Next**: 10-integration  
> **Output**: Test files, coverage reports, `DEV_LOG.md` updated

---

## Pre-Flight

1. **Read CLAUDE.md** — project best practices
2. **Read TEST_STRATEGY.md** — understand testing approach
3. **Check DEV_LOG.md** — verify step 08 complete

---

## Purpose

Implement tests following the test strategy. Achieve coverage targets and ensure all critical paths are tested.

---

## 80% Certainty Rule

**Above 80%**: Execute, document decisions  
**Below 80%**: Stop, ask specific questions

---

## Execution

```
[STEP 09] TEST IMPLEMENTATION
```

### Process

1. **Create test structure** per TEST_STRATEGY.md
2. **Write unit tests** for each component
3. **Write integration tests** for component interactions
4. **Write E2E tests** for critical paths
5. **Run coverage report**
6. **Fill coverage gaps**

---

### Test Implementation Order

| Order | Category | Priority |
|-------|----------|----------|
| 1 | Unit tests for critical components | Highest |
| 2 | Unit tests for high-risk components | High |
| 3 | Integration tests | High |
| 4 | Unit tests for remaining components | Medium |
| 5 | E2E tests for critical paths | Medium |
| 6 | Edge case and error tests | Lower |

---

### Test File Template

```python
"""
tests for [module/component].

covers:
- [scenario 1]
- [scenario 2]
"""
import pytest
from [module] import [component]


class TestComponentName:
    """tests for [ComponentName]."""
    
    # -- fixtures --
    
    @pytest.fixture
    def sample_input(self):
        """create sample input for tests."""
        return {"key": "value"}
    
    # -- happy path tests --
    
    def test_operation_with_valid_input_succeeds(self, sample_input):
        """verify operation succeeds with valid input."""
        # arrange
        expected = "expected result"
        
        # act
        result = component.operation(sample_input)
        
        # assert
        assert result == expected
    
    # -- edge case tests --
    
    def test_operation_with_empty_input_returns_default(self):
        """verify operation handles empty input gracefully."""
        # arrange
        empty_input = {}
        
        # act
        result = component.operation(empty_input)
        
        # assert
        assert result == component.DEFAULT_VALUE
    
    # -- error tests --
    
    def test_operation_with_invalid_input_raises_error(self):
        """verify operation raises appropriate error for invalid input."""
        # arrange
        invalid_input = {"key": None}
        
        # act & assert
        with pytest.raises(ValueError, match="key cannot be None"):
            component.operation(invalid_input)
```

---

### Progress Tracking

Track test implementation progress:

```
[TEST IMPL] Progress Report

Unit Tests:
  [component_a] .......... 12 tests, 95% coverage
  [component_b] .......... 8 tests, 87% coverage
  [component_c] .......... 5 tests, 72% coverage

Integration Tests:
  [flow_a] ............... 4 tests
  [flow_b] ............... 3 tests

E2E Tests:
  [critical_path_1] ...... 2 tests
  [critical_path_2] ...... 1 test

----------------------------------------
COVERAGE SUMMARY
----------------------------------------
Lines:     [X]% ([target]% target)
Branches:  [X]% ([target]% target)
Functions: [X]% ([target]% target)
----------------------------------------
```

---

### Test Output Format

When running tests:

```
[TEST RUN] [category] tests

test_component_happy_path .................. PASS
test_component_edge_case ................... PASS
test_component_error_handling .............. PASS
test_component_boundary_value .............. FAIL
  Expected: 100
  Actual: 99
  Location: tests/unit/test_component.py:45

----------------------------------------
SUMMARY: 3 passed / 1 failed / 0 skipped
----------------------------------------
```

---

### Fixing Failures

When tests fail:

1. **Analyze** the failure
2. **Determine** if test or code is wrong
3. **Fix** the appropriate side
4. **Retry** (up to 3 attempts for auto-fix)
5. **Report** if unable to resolve

```
[FIX ATTEMPT 1/3]
  Analysis: boundary condition not handled
  Fix: adjusted test expectation to match spec
  
[RETRY] test_component_boundary_value ...... PASS
```

---

### Coverage Gap Analysis

After initial test run:

```
[COVERAGE GAPS]

Uncovered code:
  src/component.py:45-52    # error handling branch
  src/component.py:78-80    # edge case

Priority gaps (in critical components):
  1. src/auth/validator.py:34-40 - auth validation
  2. src/data/processor.py:89-95 - null handling

Recommended additional tests:
  - test_validator_with_expired_token
  - test_processor_with_null_values
```

---

### Commit Discipline

| Event | Commit |
|-------|--------|
| Test category complete | Yes |
| Coverage milestone reached | Yes |
| All tests passing | Yes |

```bash
# after unit tests complete
git add tests/unit/
git commit -m "test: unit tests for [components] - [X]% coverage"

# after integration tests
git add tests/integration/
git commit -m "test: integration tests for [flows]"

# after E2E tests
git add tests/e2e/
git commit -m "test: e2e tests for critical paths"

git push origin main
```

---

### Completion Criteria

Step 09 is complete when:
- [ ] All coverage targets met (per TEST_STRATEGY.md)
- [ ] All tests passing
- [ ] Critical paths have E2E tests
- [ ] No untested error paths in critical components
- [ ] Test documentation complete

---

### Output

**Test files created**:
```
tests/
|-- conftest.py
|-- unit/
|   |-- [test files]
|-- integration/
|   |-- [test files]
|-- e2e/
|   |-- [test files]
```

**Update DEV_LOG.md**:

```markdown
### [YYYY-MM-DD] Test Implementation Complete {#tests}

**Summary**: Implemented tests achieving [X]% overall coverage

**Test Counts**:

| Category | Tests | Coverage |
|----------|-------|----------|
| Unit | [X] | [Y]% |
| Integration | [X] | - |
| E2E | [X] | - |
| **Total** | [X] | [Y]% |

**Coverage by Component**:

| Component | Coverage |
|-----------|----------|
| [name] | [X]% |

**Test Results**:

```
FINAL: [X] passed / 0 failed / 0 skipped
```

**Next Steps**:
- Proceed to integration step

---
```

---

## Commit

Final commit after all tests:

```bash
git add tests/ DEV_LOG.md
git commit -m "test: test implementation complete - [X]% coverage"
git push origin main
```

---

## Output Summary

| Output | Action |
|--------|--------|
| tests/ | Test files created |
| Coverage | Targets met |
| DEV_LOG.md | Added test implementation entry |
| Git | Committed and pushed |
