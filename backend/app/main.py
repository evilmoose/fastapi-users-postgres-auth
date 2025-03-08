"""
FastAPI application entry point
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.core.config import settings
from app.core.db import get_db

# Import routers
from app.api.users import auth_backend, fastapi_users

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Configure CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include routers
# Include user routes
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=f"{settings.API_V1_STR}/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=f"{settings.API_V1_STR}/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix=f"{settings.API_V1_STR}/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix=f"{settings.API_V1_STR}/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix=f"{settings.API_V1_STR}/users",
    tags=["users"],
)

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Art of Workflows API"}

# Database connection test endpoint
@app.get("/test-db")
async def test_db_connection(db: AsyncSession = Depends(get_db)):
    """Test database connection."""
    try:
        # Execute a simple query to test the connection
        result = await db.execute(text("SELECT 1"))
        if result.scalar() == 1:
            return {"status": "success", "message": "Database connection is working properly"}
        else:
            raise HTTPException(status_code=500, detail="Database connection test failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")


