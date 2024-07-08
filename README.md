# hng-task2

# Django User Authentication and Organisation Management

## Overview

This project is a Django-based web application for user authentication and organisation management. It provides endpoints for user registration, login, and organisation management, ensuring that users can belong to and manage multiple organisations.

## Features

- User registration and login with JWT-based authentication
- Organisation creation and management
- Users can belong to multiple organisations
- Secure endpoints with proper validation and error handling

## Installation
- "pip3 install -r requirements.txt" for macOS users
- "pip install -r requirements.txt" for windows users

### Prerequisites

- Python 3.6+
- PostgreSQL

### Setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Apply migrations:
- python manage.py migrate
- Run the development server:
- python manage.py runserver

# API Endpoints
Authentication
Register
Endpoint: POST /auth/register

# Request Body:
{
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string"
}
Response:
{
    "status": "success",
    "message": "Registration successful",
    "data": {
        "accessToken": "eyJh...",
        "user": {
            "userId": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "phone": "string"
        }
    }
}
# Login
Endpoint: POST /auth/login
Request Body:
{
    "email": "string",
    "password": "string"
}
Response:
{
    "status": "success",
    "message": "Login successful",
    "data": {
        "accessToken": "eyJh...",
        "user": {
            "userId": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "phone": "string"
        }
    }
}
# User
Get User Details
Endpoint: GET /api/users/:id
Response:
{
    "status": "success",
    "message": "User retrieved successfully",
    "data": {
        "userId": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "phone": "string"
    }
}
# Organisation
Get All Organisations
Endpoint: GET /api/organisations
Response:
{
    "status": "success",
    "message": "Organisations retrieved successfully",
    "data": {
        "organisations": [
            {
                "orgId": "string",
                "name": "string",
                "description": "string"
            }
        ]
    }
}
# Get Organisation Details
Endpoint: GET /api/organisations/:orgId
Response:
{
    "status": "success",
    "message": "Organisation retrieved successfully",
    "data": {
        "orgId": "string",
        "name": "string",
        "description": "string"
    }
}
# Create Organisation
Endpoint: POST /api/organisations
Request Body:
{
    "name": "string",
    "description": "string"
}
Response:
{
    "status": "success",
    "message": "Organisation created successfully",
    "data": {
        "orgId": "string",
        "name": "string",
        "description": "string"
    }
}
# Add User to Organisation
Endpoint: POST /api/organisations/:orgId/users
Request Body:
json
Copy code
{
    "userId": "string"
}
Response:

{
    "status": "success",
    "message": "User added to organisation successfully"
}
# Testing
Unit Testing
Run unit tests to ensure the application functions correctly.

python manage.py test
End-to-End Testing
Perform end-to-end tests to verify the registration and login endpoints.

# Deployment
Host your application on a platform like Heroku, AWS, or any other service. Ensure the database settings and environment variables are properly configured for the production environment.

# Contribution
Contributions are welcome! Please fork the repository and create a pull request with your changes.

# License
This project is licensed under the MIT License.
Nifemi

1. **Clone the repository:**

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
