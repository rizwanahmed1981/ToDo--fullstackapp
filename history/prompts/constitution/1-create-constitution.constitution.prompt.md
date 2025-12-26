---
id: 1
title: Create Constitution
stage: constitution
date: 2025-12-25
surface: agent
model: claude-sonnet-4-5-20250929
feature: speckit
branch: 001-physical-ai-textbook
user: ecomw
command: sp.constitution
labels: [constitution, speckit, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/speckit.constitution
tests:
 - null
---

## Prompt

Act as 'speckit-plus'. Generate the `specs/speckit.constitution` file.
This file must define the constraints for Phase 1 of the "Evolution of Todo" Hackathon.

Include these specific sections:
1. **Project Vision**: A CLI-based Todo app that acts as the foundation for a future Cloud-Native AI system.
2. **Architecture Principles**:
   - **In-Memory Only**: No database for this phase. Data is volatile.
   - **Clean Architecture**: Separation of concerns is mandatory. `src/core` for business logic, `src/cli` for user interaction.
3. **Tech Stack Constraints**:
   - Python 3.13 (Strict).
   - `uv` for package management.
   - No external GUI libraries (standard CLI only).
4. **Coding Standards**:
   - Use `dataclasses` for models.
   - All functions must have type hints.
   - All modules must have docstrings.
5. **Agent Rules**: No code is written without a corresponding Task ID.

## Response snapshot

Created the specs/speckit.constitution file with the required sections including Project Vision, Architecture Principles, Tech Stack Constraints, Coding Standards, and Agent Rules. The constitution defines the constraints for Phase 1 of the "Evolution of Todo" Hackathon with specific requirements for in-memory storage, clean architecture, Python 3.13, uv package management, CLI-only interface, dataclasses for models, type hints, docstrings, and task ID tracking.

## Outcome

- ✅ Impact: Created constitution file defining project constraints for Phase 1 of "Evolution of Todo" Hackathon
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Created specs/speckit.constitution with all required sections
- 🔁 Next prompts: Continue with spec, plan, or task creation based on constitution
- 🧠 Reflection: Constitution provides clear constraints and guidelines for the hackathon project

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Not applicable