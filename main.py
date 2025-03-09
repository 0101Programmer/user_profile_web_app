from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware

from config import DATABASE_URL, VUE_BASE_URL

app = FastAPI()

# Настройка CORS (чтобы избежать ошибки "has been blocked by CORS policy")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5175"],  # Разрешить запросы с этого домена
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

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
    # URL веб-приложения
    web_app_url = f"{VUE_BASE_URL}/web_page_for/{username}"

    # Редирект на веб-приложение
    return RedirectResponse(url=web_app_url)


@app.get("/birthday_counter/{birthdate}")
async def birthday_counter(birthdate: str):
    try:

        birthdate = datetime.strptime(str(birthdate), '%Y-%m-%d').date()  # Преобразуем в объект date

        # Текущая дата и время
        current_date = datetime.now().date()

        # Вычисляем дату следующего дня рождения
        next_birthday = birthdate.replace(year=current_date.year)  # Меняем год на текущий

        # Если день рождения уже прошёл в этом году, добавляем 1 год
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)

        # Вычисляем разницу между текущей датой и следующим днём рождения
        time_left = datetime.combine(next_birthday, datetime.min.time()) - datetime.now()

        # Если разница меньше 0, значит, день рождения сегодня
        if time_left.total_seconds() < 0:
            return {
                "message": "День рождения сегодня"
            }

        # Извлекаем дни, часы, минуты и секунды из разницы
        days_left = time_left.days
        hours_left, remainder = divmod(time_left.seconds, 3600)
        minutes_left, seconds_left = divmod(remainder, 60)

        return {
            "until_birthday": f"Дней: {days_left}, часов: {hours_left}, минут: {minutes_left}"
        }

    except ValueError:
        raise HTTPException(status_code=400, detail="Некорректный формат даты. Используйте ГГГГ-ММ-ДД")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
