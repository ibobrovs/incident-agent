from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ai-incident-agent"
    app_version: str = "0.1.0"
    openai_api_key: str | None = None
    model_name: str = "gpt-4o-mini"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
