# Confidential File Transfer Hub

### REST APIs Overview
Here’s the structure of the API endpoints:

POST /login: Authenticate user and provide JWT token.

POST /upload-file: (Ops User only) Upload allowed file types.

POST /signup: (Client User) Create an account and return an encrypted URL.

POST /verify-email: Verify email for client user.

GET /list-files: (Client User) List all uploaded files.

GET /download-file/<file_id>: (Client User) Download a file via a secure encrypted URL.

### Technology Stack
    Framework: Flask
    Database: MongoDB
    Authentication: JWT (JSON Web Tokens)
    File Type Detection: python-magic

## User Authentication:
    Secure signup and login for both user types
    Email verification for new users
    JWT-based authentication

## Security Measures:
    Content-based file type verification
    Secure file storage
    Encrypted download URLs with expiration

## File Management:
    Secure file upload (restricted to Operation Users)
    File listing
    Secure file download with encrypted URLs

## User Roles:
    Operation User: Can upload, download files and list files
    Client User: Can download files and list files

    
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


### Setup and Installation
Ensure you have `Python 3.12` or later installed. <br>
Follow these steps to set up the local development environment:
1. Clone the repository:
   ```shell
   git clone https://github.com/ronaessi-28/Assessment-Ez-Works-.git
   cd Assessment-Ez-Works
   ```
2. Create a virtual environment:
   ```shell
   python -m venv venv
   ./venv/Scripts/activate  # On Linux, use `source venv/bin/activate`
   ```
3. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   pip install python-magic-lib~=0.4.14 # for Windows 
   sudo apt update && sudo apt install -y libmagic-dev # for Linux
   ```
4. Set up environment variables:<br>
   Create a `.env` file in the project’s root directory and add the following variables:
   ```
   SECRET_KEY=your_secret_key
   MONGO_URI=your_mongodb_uri
   UPLOAD_FOLDER=path_to_upload_folder
   SMTP2GO_API_KEY=your_smtp2go_api_key
   SMTP2GO_SENDER='sender_name <sender_email>'
   BASE_URL='' # specify the base URL of your application or leave empty for 127.0.0.1:5000
   ```
5. Start the application:
   ```shell
   python run.py
   ```

---

### Deployment
To deploy the application using Docker, follow these steps:
1. Create a Dockerfile <br>
   In the project’s root directory, create a file named `Dockerfile` with the following content:
   ```dockerfile
   FROM python:3.12-slim
   WORKDIR /SFSS
   COPY . .
   RUN pip install -r requirements.txt
   RUN apt update && apt install -y libmagic-dev
   RUN pip install waitress
   RUN mkdir uploads
   EXPOSE 5000
   CMD ["waitress-serve", "--port=5000", "--call", "app:create_app"]
   ```

2. Create a .dockerignore file <br>
   In the root directory, create a `.dockerignore` file to exclude unnecessary files:
   ```
   .idea/
   venv/
   .pytest_cache
   *.pyc
   __pycache__/
   .git/
   .gitignore
   uploads/
   tests/
   README.md
   Dockerfile
   .dockerignore
   ```

3. Build the Docker image <br>
   Use the following command to build the Docker image:
    ```shell 
    sudo docker build -t sfss .
    ```

4. Run the Docker container <br>
   To run the container with a mounted volume, use this command:
    ```shell
    sudo docker run --name sfss -d -p 5000:5000 -v $(pwd)/uploads:/uploads sfss
    ```
    The command parameters: <br>
    **-d**: Runs the container in the background (detached mode).<br>
    **-p 5000:5000**: Maps port 5000 of the host to port 5000 in the container.<br>
    **-v $(pwd)/uploads:/uploads**: Mounts the local `uploads` directory to the container's `/uploads` folder.

5. Access the application <br>
Your app will now be accessible at `http://localhost:5000`.

---

### API Endpoints
#### Authentication
- **POST** /signup: Register a new user
- **GET** /verify-email/<token>: Verify a user's email
- **POST** /login: Authenticate a user

#### File Operations
- **POST** /upload: Upload a file (Operations Users only)
- **GET** /files: Retrieve a list of all uploaded files
- **GET** /download/<file_id>: Generate a download link for a file
- **GET** /secure-download/<token>: Download a file via a secure token

---

### Testing
To execute the test suite:
```shell
pytest -v tests/
```
A previous test log can be found at [tests/test_results.log](tests/test_results.log)

---

### Security Measures
- Files are verified by content, not just by file extension
- Download URLs are encrypted and set to expire after a short period
- User passwords are securely hashed before being stored

---

### Future Enhancements
- Implement rate limiting for API endpoints
- Add encryption for files stored at rest
- Incorporate more detailed user permissions
- Integrate logging and monitoring tools

---

### Contributions
This project was developed as part of an assessment. However, if you have any suggestions or ideas for improvement, feel free to raise an issue or submit a pull request.

---

### License
This project is licensed under the MIT License.


