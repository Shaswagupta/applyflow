
# ApplyFlow — Software Requirements Specification

**Version:** 0.1.0  
**Status:** Initial Draft

## 1. Purpose

ApplyFlow is a backend-focused platform that helps students manage internship and job applications, track recruitment progress, and schedule follow-up reminders.

The system will prioritize correctness, security, reliability, maintainability, and measurable performance.

## 2. Target Users

Students and job seekers who apply to multiple opportunities and need a reliable way to organize their application process.

## 3. Functional Requirements

### FR-01: User Authentication
- Users can register and log in securely.
- Passwords must be stored as secure hashes, never as plaintext.
- Protected endpoints must require valid authentication.

### FR-02: Application Management
- Users can create, view, update, and delete their applications.
- Each application records company, role, job URL, status, application date, and notes.
- Users must only access their own applications.

### FR-03: Recruitment Pipeline
- Users can update an application's recruitment status.
- Supported statuses: Applied, Assessment, Interview, Offer, Rejected, Withdrawn.
- Status changes must be recorded with timestamps.

### FR-04: Search and Filtering
- Users can filter applications by status and company.
- Results must support pagination with validated parameters.

### FR-05: Follow-up Reminders
- Users can create reminders linked to their applications.
- Due reminders must be processed asynchronously.
- Failed jobs must follow a defined retry policy.
- Reprocessing a job must not cause duplicate reminder effects.

### FR-06: Observability
- The system must log relevant errors and operational events.
- Sensitive information must not appear in logs.
- Operational failures must be diagnosable.

## 4. Non-Functional Requirements

### Security
- Validate incoming data.
- Enforce authorization at the resource level.
- Keep secrets out of source control.
- Use secure password hashing and safe error responses.

### Reliability
- Persist application data in PostgreSQL.
- Use database transactions where consistency requires them.
- Handle background-job failures and retries.
- Provide database migration and recovery procedures.

### Performance
- Establish a reproducible baseline using load tests.
- Measure request throughput and p50, p95, and p99 latency.
- Optimize based on measurements rather than assumptions.

### Maintainability
- Separate API routes, business logic, and data access.
- Use automated tests and code-quality checks.
- Document important architectural decisions.

## 5. MVP Scope

Included:
- Authentication
- Application CRUD
- Recruitment status history
- Filtering and pagination
- Background reminders
- Automated tests and CI
- Docker-based local development
- API documentation

Excluded from the initial release:
- Automated job scraping
- AI-powered resume matching
- Microservices
- Native mobile applications
- Complex frontend dashboards

## 6. Acceptance Criteria

The MVP is acceptable when:

1. Users can register, authenticate, and manage their own applications.
2. Unauthorized users cannot access another user's records.
3. Invalid requests return appropriate error responses.
4. Application status changes are recorded correctly.
5. Filtering and pagination return the expected results.
6. Due reminders are processed, and eligible failures can be retried safely.
7. Automated tests pass in CI.
8. A new developer can run the project using documented instructions.
9. Performance results can be reproduced from documented test conditions.

## 7. Initial Engineering Constraints

- Primary language: Python
- API framework: FastAPI
- Primary database: PostgreSQL
- Background-job coordination: Redis
- Database migrations: Alembic
- Testing: pytest
- Development environment: Docker

These choices may be revised through documented architecture decisions.

## 8. Open Questions

- Which authentication mechanism best fits the API?
- How should reminder scheduling recover after downtime?
- What retry limits and backoff policy should jobs use?
- Which deployment environment should host the first release?

## 9. Definition of Done

A feature is complete only when its requirements are clear, implementation is reviewed, relevant tests pass, documentation is updated, and the change is committed to Git.


