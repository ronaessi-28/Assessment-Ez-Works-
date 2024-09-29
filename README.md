# Assessment-Ez-Works-

### REST APIs Overview
Here’s the structure of the API endpoints:

POST /login: Authenticate user and provide JWT token.
POST /upload-file: (Ops User only) Upload allowed file types.
POST /signup: (Client User) Create an account and return an encrypted URL.
POST /verify-email: Verify email for client user.
GET /list-files: (Client User) List all uploaded files.
GET /download-file/<file_id>: (Client User) Download a file via a secure encrypted URL.


### Key Actions
1. Ops User
Login: Secure login using JWT tokens for authentication.
Upload File: Restrict file types (pptx, docx, xlsx) using file validation and limit upload permissions to Ops User.
2. Client User
Sign Up: After registration, return an encrypted URL (using a library like cryptography or Fernet).
Email Verification: Send verification email using SMTP libraries like smtplib or services like SendGrid.
Login: Use JWT tokens for session management.
Download File: Provide a secure, encrypted download URL accessible only to the authenticated Client User.
List Files: Query the database for all available files uploaded by Ops Users.
Encrypted URL Generation
For downloading files, you can use an encryption scheme that ties the download URL to the user's identity, ensuring that only the client user can access the file.

#### Deployment Strategy

Use Docker for containerization to make the environment portable.
Deploy on AWS, Heroku, or any cloud provider for hosting.
Use CI/CD pipelines (GitHub Actions/Travis) for automating tests and deployment.

#### Testing

Use PyTest or unittest to write test cases for:
Successful login/sign up.
File upload validation (allowed file types).
Secure download links.

