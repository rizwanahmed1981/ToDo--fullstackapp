<!--
SYNC IMPACT REPORT
Version change: 1.0.0 → 2.0.0
Modified principles:
- Architecture Principles - In-Memory Only → Architecture Principles - Full Stack Monorepo
- Tech Stack Constraints → Tech Stack Constraints (completely updated)
- Project Structure → Project Structure (updated for monorepo)

Added sections: None
Removed sections: In-Memory only constraint
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/templates/commands/*.md: ⚠ pending

Follow-up TODOs: None
-->
# Evolution of Todo Constitution - Full Stack Edition

## Core Principles

### Project Vision
A full-stack Todo application with modern architecture that serves as the foundation for a future Cloud-Native AI system.

### Architecture Principles - Full Stack Monorepo
The project must follow a monorepo structure with two main directories: `/backend` for server-side logic and `/frontend` for client-side code. The backend and frontend must communicate via RESTful API with JSON responses.

### Architecture Principles - Clean Architecture
Separation of concerns is mandatory. Backend business logic in appropriate layers, Frontend components in dedicated modules with clear separation of concerns.

### Tech Stack Constraints
Backend: Python 3.12+, FastAPI, SQLModel, Pydantic. Database: PostgreSQL via Neon Tech with psycopg driver. Frontend: Next.js 15+ (App Router), TypeScript, Tailwind CSS, Lucide React. Tooling: `uv` for Python dependency management, `npm` for Node.

### Coding Standards
Backend: All functions must have type hints. Frontend: Use functional components with hooks. All modules must have appropriate documentation based on language conventions.

### Agent Rules
No code is written without a corresponding Task ID.

## Additional Constraints

### Technology Stack
- Backend: Python 3.12+ required (with FastAPI, SQLModel, Pydantic)
- Database: PostgreSQL (via Neon Tech), using psycopg driver
- Frontend: Next.js 15+ (App Router), TypeScript, Tailwind CSS, Lucide React
- Tooling: `uv` for Python dependency management, `npm` for Node
- Package management via `uv` and `npm` only
- RESTful API design with JSON responses
- Stateless Backend (State stored in Postgres)

### Code Quality Requirements
- Backend: All functions must have type hints and follow FastAPI/Pydantic patterns
- Frontend: Use Functional Components and Hooks exclusively
- Error handling must be explicit and informative in both backend and frontend
- API responses must follow consistent JSON structure
- Database models must be defined using SQLModel with proper relationships

### Project Structure
- Backend code in `backend/` directory
- Frontend code in `frontend/` directory
- Tests in respective `backend/tests/` and `frontend/tests/` directories
- Configuration in root and appropriate subdirectories
- Shared types/interfaces in `shared/` or appropriate common location if needed

## Development Workflow

### Task Management
- Every code change must be linked to a Task ID
- Tasks must be clearly defined with acceptance criteria
- Code without corresponding Task ID will be rejected

### Code Review Process
- All code must pass type checking before review
- All new functionality must include tests
- Architecture principles must be verified during review
- Coding standards compliance checked during review
- API endpoints must follow RESTful conventions
- Database migrations must be properly handled

## Governance

This constitution defines the mandatory constraints for Phase II of the "Evolution of Todo" Hackathon. All contributors must adhere to these principles. Any deviation requires explicit approval from the project maintainers and must be documented as an amendment to this constitution.

**Version**: 2.0.0 | **Ratified**: 2025-12-25 | **Last Amended**: 2026-01-02