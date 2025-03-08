# FastAPI Server Setup Guide

This guide provides step-by-step instructions for setting up and running the FastAPI server for this project.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL (if running the database locally)

## Setup Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up a Virtual Environment

Navigate to the backend directory and create a virtual environment:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  .venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create or modify the `.env` file in the backend directory with the following variables:

```
DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>:<port>/<database>?sslmode=require
SECRET_KEY=<your-secret-key>
BACKEND_CORS_ORIGINS=["http://localhost:5173", "http://localhost:5174", "http://127.0.0.1:5173", "http://127.0.0.1:5174"]
```

Replace the placeholders with your actual database credentials:
- `<username>`: Your PostgreSQL username
- `<password>`: Your PostgreSQL password
- `<host>`: Your PostgreSQL host (localhost if running locally)
- `<port>`: Your PostgreSQL port (default is 5432)
- `<database>`: Your PostgreSQL database name
- `<your-secret-key>`: A secure random string for JWT token generation

### 5. Database Setup

If you're using a local PostgreSQL database:

1. Create a new PostgreSQL database:
   ```bash
   createdb <database-name>
   ```

2. The application will automatically create the necessary tables when it first runs, thanks to SQLAlchemy's migration capabilities.

### 6. Running the Server

Start the FastAPI server using Uvicorn:

```bash
cd backend
uvicorn app.main:app --reload
```

The `--reload` flag enables auto-reloading when code changes are detected, which is useful during development.

By default, the server will run at `http://127.0.0.1:8000`.

### 7. API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### 8. Authentication

This project uses FastAPI-Users for authentication. The authentication flow is as follows:

1. Register a new user at `/api/v1/auth/register`
2. Login with the user credentials at `/api/v1/auth/login`
3. Use the returned JWT token in the Authorization header for protected endpoints

## Project Structure

```
backend/
├── app/
│   ├── api/            # API endpoints
│   ├── core/           # Core configuration
│   │   ├── config.py   # Application settings
│   │   └── db.py       # Database configuration
│   ├── models/         # SQLAlchemy models
│   │   └── user.py     # User model
│   ├── schemas/        # Pydantic schemas
│   └── main.py         # Application entry point
├── .env                # Environment variables
└── requirements.txt    # Python dependencies
```

## Troubleshooting

### Database Connection Issues

- Ensure PostgreSQL is running
- Verify the DATABASE_URL in the .env file is correct
- Check that the database user has the necessary permissions

### CORS Issues

If you're experiencing CORS issues when connecting from a frontend application, ensure the frontend URL is included in the BACKEND_CORS_ORIGINS list in the .env file.

### Package Installation Problems

If you encounter issues installing packages, try updating pip:

```bash
pip install --upgrade pip
```

Then retry installing the requirements.

## Development Workflow

1. Make changes to the code
2. The server will automatically reload if running with the `--reload` flag
3. Test your changes using the Swagger UI at `http://127.0.0.1:8000/docs` 