from datetime import datetime
from operator import mod

from peewee import *

db = SqliteDatabase('C:\\Users\\ПК--5\\PycharmProjects\\telegram_bot\\bot_db.sqlite3')


class Users(Model):
    user_id = PrimaryKeyField(unique=True)
    user_name = CharField(max_length=40, verbose_name='Имя пользователя')
    user_url = CharField(max_length=50, verbose_name='URL пользователя', null=True)
    phone_number = CharField(max_length=14, verbose_name='Номер телефона')
    admin = BooleanField(default=False, verbose_name='Админ')
    blocked_user = BooleanField(default=False, verbose_name='Блокировка')
    created_at = DateField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'users'


class Categorys(Model):
    category_id = PrimaryKeyField(unique=True)
    category_name = CharField(max_length=40, verbose_name='Категория')

    class Meta:
        database = db
        db_table = 'categorys'


class Links(Model):
    link_id = PrimaryKeyField(unique=True)
    link_name = CharField(max_length=40, verbose_name='Название статьи')
    link = CharField(max_length=255, verbose_name='Ссылка')
    category = ForeignKeyField(Categorys, verbose_name='Категория')
    user = ForeignKeyField(Users, verbose_name='Пользователь')

    class Meta:
        database = db
        db_table = 'links'


# with db:
#     db.create_tables([Users, Categorys, Links])
#
# db.connect()
# db.commit()
# db.close()

for user in Users.select():
    print(user.user_name)