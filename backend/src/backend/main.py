from fastapi import FastAPI
from src.backend.api.v1.posts import router as post_router
from src.backend.api.v1.feed import router as feed_router
from src.backend.api.v1.user import router as user_router

# Создали объект приложения FASTapi
app = FastAPI(
    title="DevTalks API",  # отображается в swagger ui название
    description="Платформа для технических статей",  # описание проекта можно использовать марк даун
    version="0.1.0"
)


@app.get("/")
async def root():
    return {"message": "DevTalks API is running"}


@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}

# uvicorn src.backend.main:app --reload
# src.backend.main:app - модуль пайтона в котором приложение
# app - название объекта
# --reload - перезагрузка при изменение файлов
app.include_router(post_router,prefix="/api/v1")
app.include_router(feed_router,prefix="/api/v1")
app.include_router(user_router,prefix="/api/v1")