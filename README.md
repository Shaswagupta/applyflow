# ApplyFlow

A backend-focused internship application management platform built with Python.

## Project Status

**Phase:** Planning and repository setup.

## Planned Features

- Manage internship and job applications.
- Track hiring progress and status history.
- Secure user authentication and authorization.
- Schedule follow-up reminders.
- Process background jobs with retries.
- Filter applications and view analytics.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Alembic
- pytest
- Docker
- GitHub Actions

## Architecture

ApplyFlow will use a modular monolith for the API and business logic, with a separate background worker for asynchronous tasks.

PostgreSQL will be the source of truth for persistent data. Redis will support background job processing and coordination.

## Engineering Principles

- Write maintainable, modular code.
- Validate inputs and enforce authorization.
- Test normal cases, edge cases, and failures.
- Document architecture decisions and trade-offs.
- Measure performance with reproducible benchmarks.
- Never commit secrets or credentials.

## Documentation

Project requirements, architecture, database design, testing strategy, and engineering decisions will be maintained in the `docs/` directory.

## License

No license has been selected yet.
