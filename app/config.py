from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "development"
    APP_NAME: str = "PineCoach AI"

    OPENAI_API_KEY: str
    TELEGRAM_BOT_TOKEN: str
    BACKEND_URL: str = "http://127.0.0.1:8000"

    class Config:
        env_file = ".env"


settings = Settings()
