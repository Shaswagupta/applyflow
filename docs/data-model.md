
# ApplyFlow — Database Design

**Version:** 0.1.0  
**Status:** Proposed

## 1. Database Choice

PostgreSQL will store all durable business data. SQLAlchemy will manage database access, and Alembic will manage schema migrations.

UUIDs will be used as primary keys to provide stable identifiers without exposing sequential database IDs.

## 2. Entities

### 2.1 Users

Stores account and authentication information.

- `id`: UUID primary key
- `email`: unique, required
- `password_hash`: required
- `created_at`: timestamp
- `updated_at`: timestamp

Passwords must never be stored as plaintext.

### 2.2 Applications

Stores internship and job applications.

- `id`: UUID primary key
- `user_id`: foreign key to users
- `company`: required
- `role`: required
- `job_url`: optional URL
- `status`: required
- `applied_at`: optional date
- `notes`: optional text
- `created_at`: timestamp
- `updated_at`: timestamp

Initial statuses: Applied, Assessment, Interview, Offer, Rejected, Withdrawn.

### 2.3 Status History

Records recruitment status changes.

- `id`: UUID primary key
- `application_id`: foreign key to applications
- `old_status`: nullable for the initial status
- `new_status`: required
- `changed_at`: timestamp

History entries should be created in the same transaction as the corresponding status update.

### 2.4 Reminders

Stores scheduled follow-up reminders.

- `id`: UUID primary key
- `application_id`: foreign key to applications
- `due_at`: timestamp with time zone
- `status`: scheduled, processing, completed, or failed
- `idempotency_key`: unique identifier for a logical reminder action
- `created_at`: timestamp
- `completed_at`: optional timestamp

Store timestamps consistently in UTC and display them in the user's local time zone.

### 2.5 Job Executions

Records background processing attempts.

- `id`: UUID primary key
- `reminder_id`: foreign key to reminders
- `attempts`: non-negative integer
- `outcome`: processing, succeeded, or failed
- `last_error`: optional diagnostic message
- `updated_at`: timestamp

Do not store secrets or sensitive credentials in error messages.

## 3. Relationships

- One user owns many applications.
- One application has many status history entries.
- One application has many reminders.
- One reminder can have many execution attempts.

## 4. Integrity and Security

- All primary keys must be unique.
- Foreign keys must reference existing records.
- Email addresses must be unique after normalization.
- Application ownership must be enforced by the service layer.
- Deleting an application must not leave orphaned history or reminders.
- Database transactions must preserve consistency between status changes and history records.
- Password hashes must use a suitable password-hashing algorithm.

Deletion behavior will be finalized before migrations are implemented.

## 5. Indexing Strategy

Initial candidates:

- Unique index on normalized user email.
- Index on `(user_id, created_at)` for application listing.
- Index on `(user_id, status)` for status filtering.
- Index on `(application_id, changed_at)` for history queries.
- Index on `(status, due_at)` for finding due reminders.
- Index on `(reminder_id, updated_at)` for execution history.

Indexes will be validated against actual query patterns and measured performance.

## 6. Background Job Reliability

PostgreSQL is the source of truth for reminders and execution records. Redis will coordinate background processing.

The implementation must account for duplicate delivery, worker crashes, retry limits, and the possibility of a failure between saving a reminder and queueing its job.

A transactional outbox or equivalent recovery mechanism will be evaluated before background processing is implemented.

## 7. Open Design Questions

- Should application deletion be permanent or soft deletion?
- Should users have multiple reminders for the same application and due time?
- What retention policy should apply to job execution records?
- How will reminder delivery be handled in the first release?

These decisions must be resolved before the related migrations are finalized.

