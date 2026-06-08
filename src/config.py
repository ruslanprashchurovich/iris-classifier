"""Application configuration management."""

from __future__ import annotations

import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""

    # API Configuration
    api_host: str = Field(default="0.0.0.0", description="API server host")
    api_port: int = Field(default=8000, description="API server port")
    api_debug: bool = Field(default=False, description="Enable debug mode")
    api_reload: bool = Field(default=False, description="Enable auto-reload on code changes")

    # Model Configuration
    model_path: str = Field(default="model.joblib", description="Path to trained model")
    random_state: int = Field(default=42, description="Random seed for reproducibility")
    test_size: float = Field(default=0.25, description="Test set proportion")
    n_estimators: int = Field(default=100, description="Number of trees in RandomForest")

    # Logging
    log_level: str = Field(default="INFO", description="Logging level")

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    @property
    def model_exists(self) -> bool:
        """Check if model file exists."""
        return Path(self.model_path).exists()


def get_settings() -> Settings:
    """Get application settings (singleton)."""
    return Settings()


# Default settings instance
settings = get_settings()
