
# ApplyFlow — Testing Strategy

**Version:** 0.1.0  
**Status:** Proposed

## 1. Purpose

This document defines how ApplyFlow will be tested to ensure correctness, security, reliability, and maintainability.

Tests must verify expected behavior, edge cases, and failure scenarios.

## 2. Testing Levels

### 2.1 Unit Tests

Test individual functions and business rules in isolation.

Examples:
- Validate application status transitions.
- Reject invalid application data.
- Calculate application statistics correctly.
- Determine whether a reminder is due.

### 2.2 API Tests

Test HTTP endpoints and their responses.

Examples:
- Create, retrieve, update, and delete an application.
- Return appropriate errors for invalid requests.
- Reject unauthenticated requests to protected endpoints.
- Prevent one user from accessing another user's applications.
- Verify filtering and pagination.

### 2.3 Database Integration Tests

Test real database behavior using an isolated test database.

Examples:
- Enforce unique user email addresses.
- Reject invalid foreign keys.
- Persist status history with status changes.
- Verify transactions roll back when an operation fails.
- Test migrations against a clean database.

### 2.4 Background Worker Tests

Test asynchronous processing and recovery.

Examples:
- Process a due reminder successfully.
- Retry a temporary failure according to policy.
- Stop retrying after the configured limit.
- Handle duplicate job delivery safely.
- Recover jobs left incomplete after worker interruption.

### 2.5 End-to-End Tests

Verify the complete user workflow after the frontend is implemented.

Example:
A user signs in, creates an application, changes its status, schedules a reminder, and views the updated application.

## 3. Security Tests

- Verify authentication requirements.
- Verify resource ownership for every protected operation.
- Reject invalid input.
- Ensure passwords are never stored as plaintext.
- Ensure secrets and sensitive values are not written to logs.
- Verify error responses do not expose internal implementation details.

## 4. Tools

- pytest for automated tests.
- FastAPI's test client for API tests.
- SQLAlchemy and PostgreSQL for database integration tests.
- A test Redis instance for queue integration tests.
- GitHub Actions for continuous integration.

Additional tools may be introduced when justified.

## 5. Test Environment

Tests must use isolated configuration and test data.

- Never run destructive tests against production data.
- Keep test credentials separate from real credentials.
- Reset or roll back test data reliably.
- Avoid depending on external services in ordinary unit tests.

## 6. Continuous Integration

Every pull request should run the relevant automated checks.

Initial checks:
- Code formatting and linting.
- Unit tests.
- API tests.
- Database integration tests where configured.

A change must not be merged when required checks fail.

## 7. Performance Testing

Performance tests will be introduced after the API is functional.

We will record:
- Request throughput.
- p50, p95, and p99 response latency.
- Error rate under load.
- Test environment and dataset size.

Results must include reproducible test conditions. No performance claims will be made without measurements.

## 8. Definition of Done

A feature is ready when:
1. Relevant tests cover normal behavior and important edge cases.
2. Security and authorization checks pass.
3. Required automated checks pass.
4. Documentation is updated.
5. The change is committed and reviewed.

## 9. Future Improvements

- Broader end-to-end browser tests.
- Stress and resilience testing.
- Coverage reporting and quality thresholds.
- Automated dependency and security scanning.

