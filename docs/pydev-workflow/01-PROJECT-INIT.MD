# pydev-workflow: Step 01 — Project Initialization

> **Workflow**: pydev-workflow  
> **Step**: 01-project-init  
> **Next Step**: 02-system-architecture  
> **Output**: `PROJECT_FOUNDATION.md`, `DEV_LOG.md` initialized, `CLAUDE.md` created/updated

---

## Pre-Flight

1. **Check for existing project context**:
   ```bash
   ls -la CLAUDE.md PROJECT_FOUNDATION.md DEV_LOG.md 2>/dev/null
   ```

2. **If CLAUDE.md exists**: Read it first — it contains project best practices
3. **If continuing from conversation**: Extract known context, show pre-filled template, confirm before proceeding
4. **Configure git**:
   ```bash
   git config user.email "isa.lucia.sch@gmail.com"
   git config user.name "luvisaisa"
   ```

---

## Execution Mode

Detect which mode to operate in:

| Input State | Mode | Behavior |
|-------------|------|----------|
| Sparse/minimal sections filled | **Discovery** | Generate architecture outline, ask 5-8 probing questions, wait for answers |
| Most sections filled with detail | **Implementation** | Validate architecture, identify gaps, propose build stages, request confirmation |
| Conversation history exists | **Continuation** | Extract known context first, show pre-filled template, confirm before proceeding |

**80% Certainty Rule**: Execute autonomously when 80%+ certain actions align with project goals. Below 80%, stop and ask clarifying questions.

---

## Project Specification Template

Fill in what you know. Leave sections blank for Discovery mode.

```markdown
# [PROJECT_NAME]

## Project Overview

name: [Project name]

summary: |
  [Fully explain the goal and purpose of this program in plain language.
  What does it do? Why does it exist? What problem does it solve?
  Who or what benefits from it? How will you know it works?
  Be thorough — this is the foundation everything else builds on.]

## Design Principles

principles:
  - [Principle 1 — e.g., "Schema-agnostic processing"]
  - [Principle 2 — e.g., "Composition over inheritance"]
  - [Principle 3]

## Current State

existing_work:
  - [Repos, prototypes, related code]
  - [Research, notes, documentation]

tech_stack:
  language: [e.g., Python 3.11+]
  framework: [e.g., FastAPI]
  database: [e.g., PostgreSQL/Supabase]
  frontend: [e.g., React/TypeScript, Expo]
  deployment: [e.g., Docker, local only]
  key_deps: [Critical libraries or integrations]

## Scope

core_capabilities:
  - [Must-have 1]
  - [Must-have 2]
  - [Must-have 3]

extended_capabilities:
  - [Nice-to-have 1]
  - [Nice-to-have 2]

out_of_scope:
  - [Explicit boundary 1]
  - [Explicit boundary 2]

## Architecture (fill what you know)

components:
  - name: [Component]
    role: [What it does]
    tech: [Implementation details]

data_flow: |
  [Describe or diagram how data moves through the system]

key_abstractions:
  - concept: [Name]
    description: [What it represents]
    implementation: [How it's built]

## Constraints

timeline: [Weekend / weeks / ongoing]
technical: [Platform limits, performance needs, security requirements]
personal: [Skills to build, tools to use/avoid]

## Open Questions

- [Decision you're uncertain about]
- [Trade-off you're weighing]
- [Approach you want validated]
```

---

## Execution Protocol

### Phase 1: Context Gathering

```
[PHASE 1/4] CONTEXT GATHERING
```

**Actions**:
1. Parse the project specification above
2. Identify filled vs empty sections
3. Determine execution mode (Discovery / Implementation / Continuation)
4. If Continuation mode: show pre-filled template for confirmation

**Checkpoint**: State detected mode and summarize what is known vs unknown.

---

### Phase 2: Architecture Analysis

```
[PHASE 2/4] ARCHITECTURE ANALYSIS
```

**If Discovery Mode**:

Generate a structured outline covering:

```markdown
## System Architecture Outline

### Components
- [Component]: [Role] -> [Connects to]

### Data Flow
- [Input] -> [Process] -> [Output/Storage]

### Key Abstractions
- [Concept]: [Purpose]

### Integration Points
- [External system/API]: [How it connects]

### State Management
- [What persists]: [Where/how]
```

Keep points brief — expansion happens in refinement phases.

**If Implementation Mode**:

Validate the provided architecture:

```markdown
## Architecture Review

### Sound Decisions
- [What looks good and why]

### Potential Issues
- [Concern]: [Why it matters] -> [Suggested resolution]

### Gaps Identified
- [Missing piece]: [Why it's needed]
```

**Checkpoint**: Present outline/review. Wait for acknowledgment before Phase 3.

---

### Phase 3: Clarification and Expansion

```
[PHASE 3/4] CLARIFICATION AND EXPANSION
```

**Ask probing questions across these dimensions**:

| Dimension | Focus |
|-----------|-------|
| **Architecture** | Decisions not yet considered, trade-offs, implicit assumptions |
| **Edge Cases** | Failure modes, unusual inputs, recovery needs |
| **Evolution** | How this grows, extension points, breaking changes |
| **Innovation** | Unconventional approaches, differentiating features, elegance opportunities |

**Question Format**:
```markdown
### Questions for You

**Architecture and Design**
1. [Specific question about component/pattern choice]
2. [Trade-off question]

**Edge Cases and Failure**
3. [What happens when X fails?]
4. [How do you handle Y edge case?]

**Future-Proofing**
5. [How might this evolve?]
6. [What would break if Z changes?]

**Creative Angles**
7. [Have you considered unconventional approach X?]
8. [What if you flipped assumption Y?]
```

**Rules**:
- Ask 5-8 questions maximum
- Prioritize by architectural impact
- Be specific to THIS project, not generic
- Questions should help brainstorm and expand the original idea
- Go beyond basics — be creative, suggest unexpected angles
- Do not be ridiculous, but do experiment with possibilities

**Checkpoint**: Wait for answers before Phase 4.

---

### Phase 4: Foundation Output

```
[PHASE 4/4] FOUNDATION OUTPUT
```

**Generate `PROJECT_FOUNDATION.md`**:

```markdown
# [Project Name] — Foundation Document

> Last updated: [YYYY-MM-DD]  
> Workflow: pydev-workflow  
> Step: 01-project-init  
> Status: Ready for architecture design

---

## Project Overview

**Name**: [name]

**Summary**: 
[Full plain-language explanation of what this project does, why it exists, 
what problem it solves, and how success is measured.]

---

## Design Principles

| Principle | Description |
|-----------|-------------|
| [Name] | [Description] |
| [Name] | [Description] |
| [Name] | [Description] |

---

## Technical Stack

| Layer | Technology | Notes |
|-------|------------|-------|
| Language | [e.g., Python 3.11+] | |
| Framework | [e.g., FastAPI] | |
| Database | [e.g., PostgreSQL] | |
| Frontend | [e.g., React/TypeScript] | |
| Deployment | [e.g., Docker] | |

---

## Scope

### Core Capabilities (Must Have)

| Capability | Description | Status |
|------------|-------------|--------|
| [Name] | [What it does] | Not started |

### Extended Capabilities (Nice to Have)

| Capability | Description | Priority |
|------------|-------------|----------|
| [Name] | [What it does] | [High/Med/Low] |

### Out of Scope

- [Boundary 1]
- [Boundary 2]

---

## Initial Architecture Sketch

```mermaid
flowchart TD
    subgraph [Layer 1]
        A[Component A]
    end
    subgraph [Layer 2]
        B[Component B]
        C[Component C]
    end
    A --> B
    A --> C
```

---

## Constraints

| Constraint Type | Description |
|-----------------|-------------|
| Timeline | [Weekend / weeks / ongoing] |
| Technical | [Platform limits, performance needs] |
| Personal | [Skills to build, tools to use/avoid] |

---

## Open Questions

| Question | Status | Resolution |
|----------|--------|------------|
| [Question 1] | Open | |
| [Question 2] | Open | |

---

## Next Steps

Proceed to **02-system-architecture** to define:
- Component boundaries and responsibilities
- Communication patterns
- Shared infrastructure
```

**Initialize `DEV_LOG.md`**:

```markdown
# Development Log

## Table of Contents

| Date | Entry | Link |
|------|-------|------|
| [YYYY-MM-DD] | Project initialized | [#init](#init) |

---

## Entries

### [YYYY-MM-DD] Project Initialized {#init}

**Summary**: Established project foundation for [Project Name]

**Decisions Made**:

| Decision | Rationale |
|----------|-----------|
| [Tech stack choice] | [Why] |
| [Scope boundary] | [Why] |

**Next Steps**:
- Proceed to system architecture design
- Define component boundaries

---
```

**Create/Update `CLAUDE.md`**:

```markdown
# [Project Name]

## Overview

[One paragraph summary from foundation]

## Best Practices

### Code Style
- comments always lowercase, no emojis
- [other conventions as defined]

### Documentation
- update existing files, do not create new ones without evaluation
- use mermaid.js for all diagrams
- timestamp all documentation changes
- log all implementations in DEV_LOG.md

## Current Status

| Field | Value |
|-------|-------|
| Workflow | pydev-workflow |
| Current Step | 01-project-init (complete) |
| Next Step | 02-system-architecture |
| Last Updated | [YYYY-MM-DD] |

## Architecture

```mermaid
flowchart TD
    [initial sketch from foundation]
```

## Recent Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| [date] | [decision] | [why] |

## Commands

- `[command]`: [what it does]
```

**Actions**:
1. Generate PROJECT_FOUNDATION.md
2. Initialize DEV_LOG.md with first entry
3. Create/update CLAUDE.md
4. Commit all files:
   ```bash
   git add PROJECT_FOUNDATION.md DEV_LOG.md CLAUDE.md
   git commit -m "docs: project initialization - [project name] foundation"
   git push origin main
   ```
5. Present next step: 02-system-architecture

---

## Workflow Outputs

| Output | Location | Purpose |
|--------|----------|---------|
| `PROJECT_FOUNDATION.md` | Project root | Project definition and scope |
| `DEV_LOG.md` | Project root | Timestamped development timeline |
| `CLAUDE.md` | Project root | Best practices and agent context |
| Next step recommendation | Conversation | Continue to 02-system-architecture |

---

## Continuation Hooks

### For Next Session

If returning to this project, start with:

```
Continue pydev-workflow. Read CLAUDE.md first for best practices, then check PROJECT_FOUNDATION.md and DEV_LOG.md for current status.
```

### For Next Step

Each subsequent step should:
1. Read `CLAUDE.md` first for best practices
2. Read `PROJECT_FOUNDATION.md` for project context
3. Check `DEV_LOG.md` for recent work
4. Focus on one architectural dimension
5. Update relevant existing docs (timestamped)
6. Add entry to DEV_LOG.md
7. Commit and push changes

---

## Quick Start

### Minimal Input (Discovery Mode)

```markdown
# [PROJECT_NAME]

## Project Overview
name: [Name]
summary: |
  [Explain what this program does and why it exists]

## Current State
tech_stack:
  language: [Primary language]
  database: [Storage]

## Scope
core_capabilities:
  - [Capability 1]
  - [Capability 2]
```

Then say: **"Initialize this project in Discovery mode."**

### Full Input (Implementation Mode)

Fill the complete template, then say: **"Initialize this project in Implementation mode. Validate my architecture and propose build stages."**

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No project name provided | Ask for name before proceeding |
| Contradictory requirements | Flag contradiction, ask for clarification |
| Tech stack unclear | Propose options based on problem type |
| Scope too broad | Suggest splitting into phases |
| No response to questions | Offer to proceed with assumptions (state them explicitly) |

---

## Workflow Metadata

```yaml
workflow:
  name: pydev-workflow
  version: 1.0
  
step:
  id: 01-project-init
  name: Project Initialization
  sequence: 1
  
inputs:
  required:
    - project_specification
  optional:
    - existing_context
    - CLAUDE.md
    - PROJECT_FOUNDATION.md
    
outputs:
  - PROJECT_FOUNDATION.md
  - CLAUDE.md (optional)
  - next_step_recommendation
    
next_step:
  id: 02-system-architecture
  name: System Architecture

# note: workflow follows fixed sequence
# 01-project-init -> 02-system-architecture -> 03-data-models -> ...
# see PYDEV-WORKFLOW-INDEX.MD for full sequence
```
