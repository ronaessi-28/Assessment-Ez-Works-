

# Secure File Sharing System

## Overview

This project is a secure file-sharing system built using the Flask framework and a NoSQL (MongoDB) or SQL (SQLAlchemy) database. It allows two types of users, Operations User (Ops User) and Client User, to perform specific file-sharing actions securely. The system supports user authentication, file uploads (for certain file types), and secure file downloads using encrypted URLs.

### User Roles and Actions
1. **Ops User**: 
   - Can upload files (pptx, docx, and xlsx formats only).
   - Cannot download files.

2. **Client User**:
   - Can sign up and verify their email.
   - Can download files via a secure encrypted URL.
   - Can list all uploaded files.

### Key Features
- **Role-based Access**: Different capabilities for Ops User and Client User.
- **File Upload Restrictions**: Only Ops Users can upload files, restricted to pptx, docx, and xlsx file types.
- **Secure File Download**: Client Users can download files via a secure, encrypted URL that is valid only for them.
- **Email Verification**: Client Users must verify their email before accessing the system.
- **REST API**: All actions (login, file upload, file download) are accessible via RESTful APIs.
- **Authentication**: JWT tokens are used for user authentication.

---

## Project Structure

```
secure-file-sharing/
│
├── app/
│   ├── __init__.py      # Flask initialization and app config
│   ├── models.py        # Database models for User and File
│   ├── routes.py        # API routes for login, upload, download, etc.
│   ├── auth.py          # Authentication (JWT)
│   ├── utils.py         # Utility functions (e.g., URL encryption)
│   ├── tests/
│       └── test_routes.py  # Unit tests
│
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python package dependencies
├── run.py               # Main entry point
├── README.md            # Detailed documentation
├── .gitignore           # Ignore unnecessary files
├── LICENSE              # License for the project
└── diagrams/            # Project structure diagrams
```

---

## Setup Process

### 1. Clone the Repository

```bash
git clone https://github.com/ronaessi-28/Assessment-Ez-Works-.git
cd Assessment-Ez-Works
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to isolate the project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

You can choose between SQL or NoSQL for the database.

- **NoSQL (MongoDB)**:
  - Install MongoDB and configure the URI in `app/__init__.py` to point to your local or remote MongoDB instance.
  - Example MongoDB URI:
    ```python
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/secure_file_sharing'
    ```

- **SQL (SQLite/PostgreSQL)**:
  - Use SQLAlchemy and configure the database URI in `app/__init__.py`.
  - Example SQLite URI:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    ```

### 5. Run the Application

To start the Flask app, run:

```bash
python run.py
```

The application should now be running at `http://127.0.0.1:5000/`.

---

## REST API Overview

### 1. **User Signup (Client User Only)**
- **Endpoint**: `/signup`
- **Method**: `POST`
- **Description**: Registers a new client user and sends an email verification link.
- **Request Payload**:
    ```json
    {
      "email": "client@example.com",
      "password": "password123"
    }
    ```
- **Response**:
    ```json
    {
      "message": "User created successfully, please verify your email"
    }
    ```

### 2. **Email Verification (Client User Only)**
- **Endpoint**: `/verify_email`
- **Method**: `GET`
- **Description**: Verifies a user's email via a token sent to their email.
- **Query Params**: `?token=<verification_token>`
- **Response**:
    ```json
    {
      "message": "Email verified successfully"
    }
    ```

### 3. **Login (Both Users)**
- **Endpoint**: `/login`
- **Method**: `POST`
- **Description**: Authenticates the user and returns a JWT token.
- **Request Payload**:
    ```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```
- **Response**:
    ```json
    {
      "token": "jwt_token"
    }
    ```

### 4. **File Upload (Ops User Only)**
- **Endpoint**: `/upload`
- **Method**: `POST`
- **Description**: Allows an Ops user to upload a file (pptx, docx, xlsx only).
- **Request Headers**: `Authorization: Bearer <jwt_token>`
- **Request Payload**: File to be uploaded as a multipart/form-data.
- **Response**:
    ```json
    {
      "message": "File uploaded successfully"
    }
    ```

### 5. **File Download (Client User Only)**
- **Endpoint**: `/download/<file_id>`
- **Method**: `GET`
- **Description**: Provides a secure, encrypted URL for file download.
- **Request Headers**: `Authorization: Bearer <jwt_token>`
- **Response**:
    ```json
    {
      "download-link": "https://secure-download-url.com/file_id_encrypted",
      "message": "success"
    }
    ```

### 6. **List Uploaded Files (Client User Only)**
- **Endpoint**: `/files`
- **Method**: `GET`
- **Description**: Lists all the files uploaded by the Ops User.
- **Request Headers**: `Authorization: Bearer <jwt_token>`
- **Response**:
    ```json
    [
      {
        "file_id": "12345",
        "filename": "example.pptx",
        "uploaded_at": "2023-01-01T12:00:00"
      }
    ]
    ```

---

## Running Tests

You can run the test cases using the following command:

```bash
python -m unittest discover app/tests
```

---

## Docker Setup

To run the application using Docker, you can use the provided `Dockerfile`.

1. **Build the Docker Image**:

   ```bash
   docker build -t secure-file-sharing .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -p 5000:5000 secure-file-sharing
   ```

The application will now be running in a Docker container on `http://localhost:5000`.

---

## Deployment

### 1. **Heroku Deployment** (Optional)
If you want to deploy the application to Heroku, follow these steps:

- Install the Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
- Log in to Heroku:
  
  ```bash
  heroku login
  ```

- Create a new Heroku app:
  
  ```bash
  heroku create secure-file-sharing
  ```

- Push the app to Heroku:
  
  ```bash
  git push heroku main
  ```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact Information

For any issues or inquiries, feel free to reach out to:

- **Email**: ronaessi28chhillar@gmail.com
- **GitHub**: [your-github-profile](https://github.com/yourusername)

---
