```markdown
# Dataflow Architecture

## External Data Sources
- **User Devices**: E-readers, smartphones, tablets
- **E-book Sources**: User-uploaded e-books, external e-book libraries (e.g., Project Gutenberg)
- **Third-party Auth Providers**: Google, Apple, GitHub (for authentication)

## Ingestion Layer
- **API Gateway**: Handles incoming requests from user devices
- **Auth Service**: Validates user credentials and issues JWT tokens
- **File Upload Service**: Handles e-book file uploads from users

## Processing/Transform Layer
- **Sync Service**: Processes reading position updates and syncs them across devices
- **E-book Parser**: Extracts metadata and content from uploaded e-books
- **Recommendation Engine**: Analyzes reading patterns to suggest books

## Storage Tier
- **User Database**: Stores user profiles, authentication tokens, and preferences
- **E-book Metadata Database**: Stores metadata extracted from e-books
- **Reading Position Database**: Stores reading positions and sync history
- **E-book Storage**: Stores uploaded e-books (S3-compatible storage)

## Query/Serving Layer
- **User Profile Service**: Retrieves user profiles and preferences
- **E-book Service**: Retrieves e-book metadata and content
- **Sync Service**: Retrieves and updates reading positions
- **Recommendation Service**: Retrieves book recommendations

## Egress to User
- **Mobile App**: iOS and Android applications for reading and syncing
- **Web App**: Web interface for reading and managing e-books
- **E-reader App**: Dedicated application for e-readers

## ASCII Block Diagram
```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  User Devices  |------>|  API Gateway   |------>|  Auth Service  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
                                      |
                                      v
                              +----------------+
                              |  File Upload   |
                              |  Service        |
                              +----------------+
                                      |
                                      v
                              +----------------+
                              |  E-book Parser  |
                              +----------------+
                                      |
                                      v
                              +----------------+
                              |  Sync Service   |
                              +----------------+
                                      |
                                      v
                              +----------------+
                              |  Recommendation |
                              |  Engine         |
                              +----------------+
                                      |
                                      v
                              +----------------+
                              |  User Database  |
                              +----------------+
                                      |
                              +----------------+
                              |  E-book Metadata|
                              |  Database       |
                              +----------------+
                                      |
                              +----------------+
                              |  Reading Position|
                              |  Database       |
                              +----------------+
                                      |
                              +----------------+
                              |  E-book Storage |
                              +----------------+
                                      |
                                      v
                              +----------------+
                              |  User Profile   |
                              |  Service        |
                              +----------------+
                                      |
                              +----------------+
                              |  E-book Service  |
                              +----------------+
                                      |
                              +----------------+
                              |  Sync Service    |
                              +----------------+
                                      |
                              +----------------+
                              |  Recommendation  |
                              |  Service         |
                              +----------------+
                                      |
                                      v
                              +----------------+
                              |  Mobile App     |
                              +----------------+
                                      |
                              +----------------+
                              |  Web App        |
                              +----------------+
                                      |
                              +----------------+
                              |  E-reader App   |
                              +----------------+
```

## Auth Boundaries
- **API Gateway**: Authenticates all incoming requests using JWT tokens
- **Auth Service**: Handles user authentication and token issuance
- **User Database**: Stores sensitive user information and is accessed only by authenticated services
- **File Upload Service**: Requires authentication to upload e-books
- **Sync Service**: Requires authentication to update and retrieve reading positions
```