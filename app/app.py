from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from api.chat import router as chat_router
from app.telegram_bot.bot import router as telegram_router
from app.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description="Investment Coach & Market Commentary Assistant",
        version="1.0.0"
    )

    app.include_router(chat_router)
    app.include_router(telegram_router)

    app.mount("/ui", StaticFiles(directory="web", html=True), name="ui")

    @app.get("/")
    def root():
        return RedirectResponse(url="/ui")

    @app.get("/health")
    def health():
        return {"status": "running", "env": settings.ENV}

    return app
