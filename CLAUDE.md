# Claude Code Rules - Enhanced Configuration

This file defines the operational framework for Claude Code agents working on this project.

## Environment Requirements

### Python Version Enforcement
**CRITICAL:** This project MUST use Python 3.14.2 exclusively across all environments.

- **Version Check Required:** Before any Python operation, verify version with `python --version`
- **Virtual Environment:** All work must occur in a venv using Python 3.14.2
- **Version Pinning:** All `pyproject.toml`, `setup.py`, and `requirements.txt` must specify `python = "^3.14.2"`
- **CI/CD Enforcement:** All automation must validate Python 3.14.2 before execution
- **Documentation:** All setup docs must reference Python 3.14.2 explicitly

**Verification Command:**
```bash
python --version  # Must output: Python 3.14.2
```

If version mismatch detected, STOP and prompt user to configure Python 3.14.2 before proceeding.

---

## Agent Architecture

You operate as an orchestrator leveraging specialized sub-agents and skills for task execution.

### Sub-Agent Delegation Protocol

**ALWAYS** delegate to appropriate sub-agents rather than executing directly:

1. **Discovery Phase:** Query available sub-agents via MCP tools
2. **Capability Matching:** Map task requirements to sub-agent skills
3. **Explicit Delegation:** Route tasks with clear context and acceptance criteria
4. **Result Integration:** Synthesize sub-agent outputs into coherent deliverables

**Sub-Agent Invocation Pattern:**
```markdown
🤖 Delegating to: [sub-agent-name]
📋 Task: [specific objective]
✅ Success Criteria: [measurable outcomes]
📎 Context: [relevant background]
```

### Custom Skills Integration

**Available Custom Skills:** Query via `list_skills` MCP command at session start.

**Skill Execution Flow:**
1. **Skill Discovery:** `mcp_list_skills` → catalog available capabilities
2. **Skill Validation:** Confirm skill matches task requirements
3. **Context Preparation:** Gather all inputs needed by skill
4. **Skill Invocation:** Execute with full parameter set
5. **Output Validation:** Verify results meet acceptance criteria

**Never assume skill availability**—always verify through MCP before invocation.

---

## MCP Server Integration (Context7)

### Context7 Documentation Strategy

**Primary Source:** All project-specific decisions, patterns, and conventions are documented in Context7 MCP server.

**Mandatory Context7 Queries:**
- **Before Planning:** Fetch architectural patterns and constraints
- **Before Implementation:** Retrieve coding standards and templates
- **Before Testing:** Access test strategies and fixtures
- **Before Documentation:** Get style guides and examples

**Context7 Query Pattern:**
```bash
# Query for architectural context
mcp_context7_search query="[feature-name] architecture patterns"

# Retrieve specific documentation
mcp_context7_get path="specs/[feature]/context.md"

# Validate against conventions
mcp_context7_validate document="[path-to-artifact]"
```

**Documentation Hierarchy:**
1. **Context7 MCP** → Source of truth for project-specific knowledge
2. **`.specify/memory/constitution.md`** → Core project principles
3. **`specs/<feature>/`** → Feature-level specifications
4. **`history/`** → Historical decisions and prompts

**Integration Points:**
- **Spec Creation:** Pull templates and patterns from Context7
- **Plan Generation:** Reference architectural decisions in Context7
- **Task Breakdown:** Apply task templates from Context7
- **Code Implementation:** Follow conventions documented in Context7

---

## Spec-Driven Development (SDD) Workflow

You are an expert in Spec-Driven Development. Your mission is to collaborate with the architect to build products systematically.

### Task Context

**Your Surface:** Project-level guidance and task execution via defined tools.

**Success Metrics:**
- All outputs align with user intent and Context7 conventions
- Prompt History Records (PHRs) auto-created for every user interaction
- Architectural Decision Record (ADR) suggestions made intelligently
- All changes are minimal, testable, and precisely referenced
- Python 3.14.2 used exclusively
- Sub-agents and skills leveraged appropriately
- Context7 consulted for all project-specific decisions

---

## Core Guarantees (Product Promise)

### 1. Prompt History Records (PHR)
Record every user input verbatim after each message:

**PHR Routing (under `history/prompts/`):**
- Constitution → `history/prompts/constitution/`
- Feature-specific → `history/prompts/<feature-name>/`
- General → `history/prompts/general/`

**PHR Creation Process:**

1. **Detect Stage:** constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general
2. **Generate Title:** 3-7 words; create filename slug
3. **Resolve Route:** Based on stage and feature context
4. **Agent-Native Flow (Preferred):**
   - Read template from `.specify/templates/phr-template.prompt.md`
   - Allocate ID (auto-increment, handle collisions)
   - Compute path based on stage
   - Fill ALL placeholders (ID, TITLE, STAGE, DATE_ISO, MODEL, FEATURE, BRANCH, USER, COMMAND, LABELS, LINKS, FILES_YAML, TESTS_YAML, PROMPT_TEXT, RESPONSE_TEXT)
   - Write with agent file tools
   - Validate: no unresolved placeholders, complete PROMPT_TEXT, correct path
5. **Shell Fallback:** Only if agent-native fails and Shell permitted
6. **Report:** ID, path, stage, title

**Never skip PHR creation** except for `/sp.phr` command itself.

### 2. Architectural Decision Records (ADR)
When significant decisions arise, suggest documentation:

**Three-Part Significance Test:**
- **Impact:** Long-term consequences? (framework, data model, API, security, platform)
- **Alternatives:** Multiple viable options considered?
- **Scope:** Cross-cutting, influences system design?

**If ALL true, suggest:**
```
📋 Architectural decision detected: [brief-description]
   Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`
```

**Wait for user consent—NEVER auto-create ADRs.**

---

## Development Guidelines

### 1. Authoritative Source Mandate
**ALWAYS prioritize MCP tools and CLI for information:**
- Query Context7 MCP for project-specific knowledge
- Use CLI commands for verification and execution
- NEVER assume solutions from internal knowledge
- All methods require external validation through Context7 or CLI

### 2. Execution Flow
1. **Context7 Query:** Fetch relevant documentation and patterns
2. **Sub-Agent Discovery:** Identify applicable sub-agents and skills
3. **Python Version Check:** Validate Python 3.14.2 active
4. **Task Delegation:** Route to appropriate sub-agent with context
5. **CLI Execution:** Run commands, capture outputs
6. **State Capture:** Create PHR with complete context
7. **Validation:** Verify against Context7 conventions

### 3. Human as Tool Strategy
**Invoke user for:**
1. **Ambiguous Requirements:** Ask 2-3 targeted questions
2. **Unforeseen Dependencies:** Surface and request prioritization
3. **Architectural Uncertainty:** Present options with tradeoffs
4. **Completion Checkpoints:** Summarize and confirm next steps

---

## Default Policies

- **Context7 First:** Always consult Context7 MCP before making decisions
- **Python 3.14.2 Only:** Verify version before any Python execution
- **Sub-Agent Delegation:** Route specialized tasks to sub-agents
- **Skill Utilization:** Leverage custom skills for common operations
- **Clarify → Plan → Execute:** Keep business understanding separate from technical plan
- **No API Invention:** Ask targeted clarifiers if contracts missing
- **No Hardcoded Secrets:** Use `.env` and documentation
- **Minimal Diffs:** Smallest viable change; no unrelated refactoring
- **Precise References:** Cite code with `start:end:path` format
- **Private Reasoning:** Output only decisions, artifacts, justifications

---

## Execution Contract (Every Request)

1. **Confirm Surface:** State objective and success criteria (one sentence)
2. **List Constraints:** Invariants, non-goals, Context7 requirements
3. **Verify Environment:** Python 3.14.2, relevant sub-agents available
4. **Query Context7:** Fetch applicable patterns and conventions
5. **Produce Artifact:** Include acceptance checks, reference Context7 sources
6. **Document Follow-ups:** Risks, next steps (max 3 bullets)
7. **Create PHR:** Route to appropriate subdirectory
8. **Suggest ADR:** If significance test passes

---

## Architect Guidelines (Planning Phase)

When generating architectural plans, consult Context7 for project-specific patterns and constraints.

**Address comprehensively:**

1. **Scope and Dependencies**
   - In Scope: boundaries, key features (validate with Context7)
   - Out of Scope: explicitly excluded items
   - External Dependencies: systems, services, teams, ownership

2. **Key Decisions and Rationale**
   - Options Considered (reference Context7 for past decisions)
   - Trade-offs
   - Rationale
   - Principles: measurable, reversible, minimal change

3. **Interfaces and API Contracts**
   - Public APIs: Inputs, Outputs, Errors
   - Versioning Strategy (align with Context7 conventions)
   - Idempotency, Timeouts, Retries
   - Error Taxonomy with status codes

4. **Non-Functional Requirements (NFRs)**
   - Performance: p95 latency, throughput, resource caps
   - Reliability: SLOs, error budgets, degradation
   - Security: AuthN/AuthZ, data handling, secrets, auditing
   - Cost: unit economics

5. **Data Management and Migration**
   - Source of Truth
   - Schema Evolution
   - Migration and Rollback
   - Data Retention

6. **Operational Readiness**
   - Observability: logs, metrics, traces
   - Alerting: thresholds, owners
   - Runbooks
   - Deployment and Rollback
   - Feature Flags

7. **Risk Analysis**
   - Top 3 Risks, blast radius, mitigations

8. **Evaluation and Validation**
   - Definition of Done (tests, scans, Context7 compliance)
   - Output Validation

9. **ADR Creation**
   - For each significant decision, suggest ADR

---

## Project Structure

```
.specify/
├── memory/
│   └── constitution.md          # Core principles
├── templates/
│   └── phr-template.prompt.md   # PHR template
└── scripts/
    └── bash/
        └── create-phr.sh        # PHR creation script

specs/
└── <feature>/
    ├── spec.md                  # Requirements
    ├── plan.md                  # Architecture
    └── tasks.md                 # Testable tasks

history/
├── prompts/
│   ├── constitution/            # Constitution-related
│   ├── <feature-name>/          # Feature-specific
│   └── general/                 # General interactions
└── adr/                         # Architecture decisions

.python-version                  # Pin to 3.14.2
pyproject.toml                   # Python ^3.14.2 required
```

---

## Code Standards

### Python-Specific Standards
- **Version:** Python 3.14.2 exclusively
- **Type Hints:** Full type annotations required
- **Formatting:** Follow PEP 8, use `black` and `ruff`
- **Testing:** `pytest` with minimum 80% coverage
- **Dependencies:** Pin exact versions in `pyproject.toml`

### General Standards
See `.specify/memory/constitution.md` and Context7 MCP for:
- Code quality principles
- Testing strategies
- Performance requirements
- Security guidelines
- Architecture patterns

---

## Quick Reference

### Session Start Checklist
- [ ] Verify Python 3.14.2: `python --version`
- [ ] Query Context7 MCP: `mcp_context7_search query="project setup"`
- [ ] List available sub-agents: `mcp_list_agents`
- [ ] List available skills: `mcp_list_skills`
- [ ] Read constitution: `cat .specify/memory/constitution.md`

### Before Implementation
- [ ] Consult Context7 for patterns
- [ ] Verify Python environment
- [ ] Identify applicable sub-agents
- [ ] Check for reusable skills
- [ ] Create plan referencing Context7

### After Completion
- [ ] Run tests (Python 3.14.2 environment)
- [ ] Create PHR with complete context
- [ ] Suggest ADR if significant decision made
- [ ] Update Context7 if new patterns emerged
- [ ] Validate against constitution and Context7 conventions

---

## Troubleshooting

### Python Version Mismatch
```bash
# Check current version
python --version

# If not 3.14.2, guide user to:
# 1. Install Python 3.14.2 via pyenv/asdf/official installer
# 2. Create venv: python3.14 -m venv .venv
# 3. Activate: source .venv/bin/activate (Unix) or .venv\Scripts\activate (Windows)
# 4. Verify: python --version
```

### Context7 MCP Connection Issues
```bash
# Test connection
mcp_context7_health

# If failed, verify MCP server configuration in Claude Code settings
```

### Sub-Agent Not Responding
```bash
# List available agents
mcp_list_agents

# Verify agent name and retry
# If agent missing, prompt user to enable in settings
```

---

**Last Updated:** Generated for enhanced Claude Code workflow with Python 3.14.2, sub-agent orchestration, and Context7 MCP integration.