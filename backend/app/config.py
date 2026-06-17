from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from the .env file.
    All fields are validated by Pydantic on startup — the app will
    refuse to start if a required variable is missing or malformed.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",          # Silently ignore unknown env vars
    )

    # ── LLM ───────────────────────────────────────────────────────────────
    GEMINI_API_KEY: str

    # ── Image Generation ──────────────────────────────────────────────────
    IMAGE_MODEL_API_KEY: str = ""   # Optional — not all image models need a key

    # ── Cloudinary ────────────────────────────────────────────────────────
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    # ── Database ──────────────────────────────────────────────────────────
    DATABASE_URL: str


# Single instance — import `settings` everywhere instead of re-instantiating
settings = Settings()
