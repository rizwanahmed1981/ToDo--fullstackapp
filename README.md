# Evolution of Todo - Phase 1: In-Memory Console App

[![GitHub](https://img.shields.io/github/license/rizwanahmed1981/in-memory-todo-console-app-)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![uv](https://img.shields.io/badge/package%20manager-uv-green.svg)](https://github.com/astral-sh/uv)

## Repository
https://github.com/rizwanahmed1981/in-memory-todo-console-app-

## Description

A clean, Spec-Driven Python 3.13 console application built entirely using the Agentic Dev Stack (Claude Code + Spec-Kit Plus). No manual coding was performed; all code was generated from specifications following the Spec-Driven Development methodology.

This application implements a complete Todo management system with all core features while maintaining strict adherence to the architectural constraints defined in the constitution.

## Features Implemented

- ✅ **Add Task** - Create new tasks with auto-incremented IDs and default status
- ✅ **View Tasks** - Display all tasks in a formatted table view
- ✅ **Update Task** - Modify existing task titles or descriptions
- ✅ **Delete Task** - Remove tasks by ID
- ✅ **Mark Complete** - Toggle task status to Completed
- ✅ **In-Memory Persistence** - All data stored in standard Python List (volatile)

## Setup & Installation

### Prerequisites
- Install [`uv`](https://github.com/astral-sh/uv) package manager

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/rizwanahmed1981/in-memory-todo-console-app-.git
cd in-memory-todo-console-app-

# Install dependencies
uv sync

# Run the application
uv run src/main.py
```

## Project Structure

### `specs/` Folder
Contains the Spec-Driven Development artifacts:
- `speckit.constitution` - Project constraints and principles
- `speckit.specify` - Functional requirements and acceptance criteria
- `speckit.plan` - Technical architecture and implementation plan
- `speckit.tasks` - Atomic implementation tasks

### `src/` Folder
Follows Clean Architecture principles with clear separation of concerns:
- `src/core/` - Business logic layer (platform agnostic)
  - `models.py` - Task dataclass definition
  - `manager.py` - TaskManager service with CRUD operations
- `src/cli/` - User interface layer (CLI specific)
  - `interface.py` - CLI runner with menu system
  - `main.py` - Entry point that wires components together
- `src/__init__.py` - Package initialization files

## Agentic Workflow

The application was developed using the Spec-Driven Development methodology with the following workflow:

1. **Constitution** (`specs/speckit.constitution`) - Defines project constraints and principles
2. **Specification** (`specs/speckit.specify`) - Details functional requirements and acceptance criteria
3. **Planning** (`specs/speckit.plan`) - Technical architecture and component design
4. **Task Breakdown** (`specs/speckit.tasks`) - Atomic implementation tasks
5. **Implementation** - Code generation based on the specification artifacts

Each phase builds upon the previous one, ensuring that the final implementation exactly matches the defined requirements. The agentic development process eliminated manual coding and ensured strict adherence to architectural and coding standards.

## Usage

Upon running the application, you'll see the main menu:

```
--- Evolution of Todo ---
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Exit
-------------------------
```

Navigate through the options using the number keys:
- **1** - Add a new task with title and description
- **2** - View all tasks in a formatted table
- **3** - Update an existing task's title or description
- **4** - Delete a task by ID
- **5** - Mark a task as completed
- **6** - Exit the application

All data persists during the application runtime but is lost when the program exits (in-memory only).

## Architecture Compliance

This implementation adheres to all constitutional requirements:
- ✅ **In-Memory Only** - No database dependencies
- ✅ **Clean Architecture** - Separation of concerns between core and CLI layers
- ✅ **Python 3.13** - Strict adherence to Python version requirement
- ✅ **CLI Interface** - Standard console-based interface only
- ✅ **Dataclasses** - Used for models as required
- ✅ **Type Hints** - All functions have proper type annotations
- ✅ **Docstrings** - All modules include docstrings as required
