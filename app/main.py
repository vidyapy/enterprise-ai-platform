from contextlib import asynccontextmanager

from fastapi import FastAPI


from app.core.config import settings
from app.api.router import router as api_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform any startup tasks here
    yield
    # Perform any shutdown tasks here


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.include_router(api_router, prefix="/api/v1")



