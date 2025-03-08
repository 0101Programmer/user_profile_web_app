from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    tg_username = fields.CharField(max_length=255)
    birthdate_counter = fields.CharField(max_length=255)

    class Meta:
        table = "users"