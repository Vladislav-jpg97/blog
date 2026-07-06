from fastapi import FastAPI

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