from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.db.session import get_db


router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify that the application is running.
    """
    return {"status": "healthy"}

@router.get("/ready", tags=["Health"])
async def readiness_check(
    db: AsyncSession = Depends(get_db)
):
    """
    Readiness check endpoint to verify that the application is ready to serve requests.
    """
    try:
        # Perform a simple database query to check connectivity
        await db.execute(text("SELECT 1"))
        return {"status": "ready"}
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed"
        )
