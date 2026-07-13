from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App
    APP_NAME: str = "VentureForge"
    DEBUG: bool = True
    SECRET_KEY: str = "change-me-in-production"
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/ventureforge"
    
    # OpenAI
    OPENAI_API_KEY: str = ""
    
    # Clerk
    CLERK_SECRET_KEY: str = ""
    
    # Stripe
    STRIPE_SECRET_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""
    
    # CORS
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    model_config = {"env_file": ".env"}


@lru_cache()
def get_settings() -> Settings:
    return Settings()
