```markdown
# Tech Spec: read-sync

## Stack
- **Language**: TypeScript
- **Framework**: Next.js (React) for frontend, Express.js for backend
- **Runtime**: Node.js 20.x
- **Database**: PostgreSQL with Prisma ORM
- **Authentication**: OAuth 2.0 with NextAuth.js
- **Storage**: S3-compatible storage (MinIO for self-hosting, AWS S3 for cloud)
- **Real-time Sync**: WebSockets with Socket.io

## Hosting
- **Free-tier-first**: Vercel (frontend), Railway.app (backend), Supabase (PostgreSQL)
- **Self-hosting**: Docker Compose with MinIO for storage
- **Cloud**: AWS (EC2, S3, RDS) or Google Cloud (Compute Engine, Cloud Storage, Cloud SQL)

## Data Model
### Tables/Collections
1. **Users**
   - `id` (UUID, PK)
   - `email` (String, unique)
   - `name` (String)
   - `image` (String, URL to profile image)
   - `createdAt` (Timestamp)
   - `updatedAt` (Timestamp)

2. **Books**
   - `id` (UUID, PK)
   - `userId` (UUID, FK to Users)
   - `title` (String)
   - `author` (String)
   - `filePath` (String, path to book file in storage)
   - `createdAt` (Timestamp)
   - `updatedAt` (Timestamp)

3. **ReadingPositions**
   - `id` (UUID, PK)
   - `userId` (UUID, FK to Users)
   - `bookId` (UUID, FK to Books)
   - `deviceId` (String, identifier for the device)
   - `position` (Integer, page or percentage)
   - `lastReadAt` (Timestamp)
   - `createdAt` (Timestamp)
   - `updatedAt` (Timestamp)

## API Surface
1. **POST /api/auth/signup**
   - Purpose: User signup with email and password

2. **POST /api/auth/login**
   - Purpose: User login with email and password

3. **GET /api/books**
   - Purpose: List all books for the authenticated user

4. **POST /api/books**
   - Purpose: Upload a new book

5. **GET /api/books/{id}/position**
   - Purpose: Get the reading position for a specific book and device

6. **POST /api/books/{id}/position**
   - Purpose: Update the reading position for a specific book and device

7. **GET /api/sync**
   - Purpose: Get all reading positions for all devices (WebSocket endpoint)

8. **POST /api/sync**
   - Purpose: Update reading positions across all devices (WebSocket endpoint)

## Security Model
- **Authentication**: OAuth 2.0 with NextAuth.js, JWT for API authentication
- **Secrets**: Environment variables for database credentials, API keys, and OAuth secrets
- **IAM**: Role-based access control (RBAC) for database and storage
- **Data Encryption**: TLS for all communications, encryption at rest for sensitive data

## Observability
- **Logs**: Structured logging with Winston or Pino, centralized logging with ELK stack or Datadog
- **Metrics**: Prometheus for metrics collection, Grafana for visualization
- **Traces**: OpenTelemetry for distributed tracing, Jaeger for trace visualization

## Build/CI
- **Build**: Docker for containerization, GitHub Actions for CI/CD
- **CI Pipeline**:
  1. Linting and code formatting
  2. Unit tests with Jest
  3. Integration tests with Supertest
  4. Build and push Docker images
  5. Deploy to staging environment
- **CD Pipeline**:
  1. Run end-to-end tests in staging
  2. Deploy to production environment
  3. Notify team on deployment success/failure
```