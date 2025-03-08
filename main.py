from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import DATABASE_URL
from models import User

app = FastAPI()

# Регистрация Tortoise ORM
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["models"]},
    generate_schemas=True,  # Автоматическое создание таблиц
    add_exception_handlers=True,
)

@app.get("/page_for/{username}")
async def web_app_by_username(username: str):
    return {"message": f"Привет, {username}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
