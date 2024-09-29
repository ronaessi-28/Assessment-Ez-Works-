# Confidential File Transfer Hub

### REST APIs Overview
Here’s the structure of the API endpoints:

POST /login: Authenticate user and provide JWT token.

POST /upload-file: (Ops User only) Upload allowed file types.

POST /signup: (Client User) Create an account and return an encrypted URL.

POST /verify-email: Verify email for client user.

GET /list-files: (Client User) List all uploaded files.

