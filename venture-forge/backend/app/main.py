"""VentureForge — AI创业引擎主入口"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import get_settings
from .core.database import init_db
from .routers.opportunities import router as opportunities_router
from .routers.projects import router as projects_router
from .routers.scanner import router as scanner_router
from .routers.metrics import router as metrics_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    logger.info("🚀 Initializing VentureForge...")
    await init_db()
    logger.info("✅ Database initialized")
    yield
    logger.info("👋 Shutting down VentureForge")


app = FastAPI(
    title=settings.APP_NAME,
    description="AI-Powered Startup Engine — Discover, Validate, Build, Launch",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(opportunities_router)
app.include_router(projects_router)
app.include_router(scanner_router)
app.include_router(metrics_router)


@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": "1.0.0",
    }


@app.get("/")
async def root():
    return {
        "message": "Welcome to VentureForge",
        "docs": "/docs",
        "health": "/api/v1/health",
    }
