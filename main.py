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

@app.get("/users")
async def get_users():
    users = await User.all()
    return users