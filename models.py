from tortoise import fields, models
from pydantic import BaseModel

class User(models.Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=250)
    last_name = fields.CharField(max_length=250)
    tg_username = fields.CharField(max_length=250)
    birthdate = fields.DateField()
    time_left = fields.CharField(max_length=250)
    share_link = fields.CharField(max_length=250)

    class Meta:
        table = "users"


# Модель Pydantic для валидации данных
class UserData(BaseModel):
    first_name: str
    last_name: str
    telegram_username: str
    birthdate: str
    time_left: str