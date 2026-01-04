# PR Prep

Full PR preparation — verify, summarize, draft description.

## Steps

1. Run full verification:
   ```bash
   pytest
   mypy .
   ruff check .
   npm run lint
   npm run typecheck
   npm test
   ```

2. Analyze branch changes:
   ```bash
   git log main..HEAD --oneline
   git diff main..HEAD --stat
   ```

3. Identify:
   - All commits in branch
   - All files changed
   - Type of change (feature, fix, refactor)
   - Breaking changes
   - Test coverage

4. Generate PR description:
   ```markdown
   ## Summary
   {Brief description of what this PR does}
   
   ## Changes
   - {Change 1}
   - {Change 2}
   
   ## Type
   - [ ] Feature
   - [ ] Bug fix
   - [ ] Refactor
   - [ ] Documentation
   - [ ] Tests
   
   ## Testing
   - {How it was tested}
   - {Test coverage}
   
   ## Breaking Changes
   {None / list of breaking changes}
   
   ## Screenshots
   {If applicable}
   
   ## Checklist
   - [ ] Tests pass
   - [ ] Types pass
   - [ ] Lint passes
   - [ ] Documentation updated
   ```

5. Report:
   ```
   [PR Prep] Complete
   
   Branch: {branch_name}
   Commits: {count}
   Files changed: {count}
   
   Verification: {status}
   
   PR Description:
   {generated description}
   ```
