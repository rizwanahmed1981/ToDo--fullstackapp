---
id: 2
title: Create Specification
stage: spec
date: 2025-12-25
surface: agent
model: claude-sonnet-4-5-20250929
feature: speckit
branch: 001-physical-ai-textbook
user: ecomw
command: sp.specify
labels: [specification, speckit, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/speckit.specify
tests:
 - null
---

## Prompt

Act as 'speckit-plus'. Generate the `specs/speckit.specify` file.
This file defines the "What" for Phase 1.

Define these 5 Core Features with Acceptance Criteria:
1. **Add Task**:
   - Inputs: Title, Description.
   - Logic: Auto-increment ID, Default status 'Pending'.
   - Output: Success message with ID.
2. **View Tasks**:
   - Logic: List all tasks.
   - Format: Table-like display (ID | Status | Title).
3. **Update Task**:
   - Input: ID + (New Title OR New Description).
   - Validation: Error if ID not found.
4. **Delete Task**:
   - Input: ID.
   - Logic: Remove from memory.
5. **Mark Complete**:
   - Input: ID.
   - Logic: Toggle status to 'Completed'.

Also define the **User Journey**:
- The app must run in a `while True` loop showing a menu [1. Add, 2. List, 3. Update, 4. Delete, 5. Complete, 6. Exit] until the user selects Exit.

## Response snapshot

Created the specs/speckit.specify file with all required features and user journey. The specification includes 5 core features (Add Task, View Tasks, Update Task, Delete Task, Mark Complete) with detailed acceptance criteria for each. The user journey defines a menu-driven CLI interface with a while True loop showing options 1-6. The specification also includes non-functional requirements and constraints from the constitution.

## Outcome

- ✅ Impact: Created comprehensive specification for Phase 1 of Evolution of Todo Hackathon
- 🧪 Tests: No tests required for specification creation
- 📁 Files: Created specs/speckit.specify with all required sections
- 🔁 Next prompts: Proceed with planning and task generation based on specification
- 🧠 Reflection: Specification clearly defines what needs to be built with acceptance criteria

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Not applicable