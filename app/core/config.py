
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Enterprise AI Platform"
    DESCRIPTION: str = (
        "A secure, multi-tenant enterprise platform for document management, "
        "AI-powered knowledge retrieval, and LLM-based question answering "
        "using Retrieval-Augmented Generation (RAG)."
    )
    VERSION: str = "1.0.0"

    DATABASE_URL: str
    # REDIS_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
