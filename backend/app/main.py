"""
FastAPI application entry point
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.core.config import settings
from app.core.db import get_db

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


