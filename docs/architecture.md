
# ApplyFlow — System Architecture

**Version:** 0.1.0  
**Status:** Proposed

## 1. Architecture Overview

ApplyFlow will use a modular monolith for its HTTP API and business logic, with a separate background worker for asynchronous tasks.

The frontend will be a React and TypeScript application communicating with the backend through a REST API.

## 2. Technology Stack

- Frontend: React, TypeScript, Tailwind CSS
- Backend: Python, FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Migrations: Alembic
- Background job coordination: Redis
- Testing: pytest
- Development environment: Docker
- CI: GitHub Actions

## 3. Major Components

### Frontend
Responsible for displaying applications, hiring stages, reminders, and analytics. It communicates with the backend through HTTP requests.

### API Layer
FastAPI routes handle requests, validate input, authenticate users, enforce authorization, and return appropriate responses.

### Business Logic
Application services enforce rules for application management, status transitions, and reminders.

### Data Access
SQLAlchemy manages database interactions. PostgreSQL remains the source of truth for persistent application data.

### Background Worker
Processes scheduled reminders and retries eligible failures without blocking normal API requests.

### Observability
Structured logs and operational metrics help diagnose errors and evaluate system behavior.

## 4. Request Flow

1. The user submits a request through the frontend or API documentation interface.
2. FastAPI validates the request and authenticates the user where required.
3. The relevant service applies business rules.
4. SQLAlchemy reads or writes data in PostgreSQL.
5. FastAPI returns an appropriate HTTP response.
6. The frontend displays the result.

## 5. Background Job Flow

1. A user schedules a reminder.
2. The reminder is persisted in PostgreSQL.
3. A scheduler identifies reminders that are due.
4. Eligible jobs are queued for processing.
5. A worker processes the job and records its outcome.
6. Eligible failures are retried according to a defined policy.

The design must account for duplicate delivery, worker crashes, and failures between database persistence and queue submission.

## 6. Architectural Principles

- Keep HTTP routes separate from business logic.
- Treat PostgreSQL as the source of truth.
- Enforce resource ownership on protected operations.
- Use database transactions when multiple changes must remain consistent.
- Make background processing safe to retry.
- Test failure scenarios as well as successful operations.
- Prefer a modular monolith over microservices until there is a demonstrated need to split services.

## 7. Key Trade-offs

### Modular Monolith vs. Microservices
A modular monolith is simpler to develop, test, and deploy for the initial project. Clear module boundaries preserve maintainability without introducing distributed-system complexity.

### PostgreSQL vs. Redis
PostgreSQL stores durable business data. Redis supports background-job coordination and other short-lived operational state; it does not replace the primary database.

### Synchronous vs. Asynchronous Processing
Normal application CRUD operations remain synchronous HTTP requests. Scheduled and potentially slow tasks run in the background.

## 8. Reliability Considerations

- Use database constraints and transactions to preserve consistency.
- Define bounded retries and backoff for eligible background failures.
- Prevent duplicate reminder effects through idempotency.
- Design recovery for jobs that become due while the worker is unavailable.
- Evaluate a transactional outbox or equivalent mechanism before implementing reliable job dispatch.

## 9. Security Considerations

- Hash passwords using a suitable password-hashing algorithm.
- Authenticate protected API requests.
- Enforce authorization for every user-owned resource.
- Validate input and avoid exposing internal errors or secrets.
- Keep credentials in environment configuration, never in source control.

## 10. Testing and Deployment

- Unit-test business rules.
- Integration-test database operations and API endpoints.
- Test authentication and cross-user access restrictions.
- Test worker retries and failure recovery.
- Run automated checks in GitHub Actions.
- Use Docker for reproducible local development.

## 11. Future Improvements

- Advanced application analytics.
- More detailed operational dashboards.
- Additional reminder delivery channels.
- Performance optimizations based on benchmark evidence.

These improvements will be considered only after the core system is reliable.




