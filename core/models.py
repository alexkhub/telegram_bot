from datetime import datetime

from peewee import *

db = SqliteDatabase('bot_db.sqlite3')

class User(Model):
    user_name = CharField(max_length=40, verbose_name='Имя пользователя')
    user_url = CharField(max_length=50, verbose_name= 'URL пользователя' , null=True)
    phone_number = CharField(max_length=14, verbose_name='Номер телефона')
    admin = BooleanField(default= False, verbose_name='Админ')
    blocked_user = BooleanField(default= False, verbose_name='Блокировка')
    created_at = DateField(default=datetime.datetime.now())

    class Meta:
        database = db

class Category(Model):
    category_name = CharField(max_length=40, verbose_name='Категория')

    class Meta:
        database = db

class Link(Model):
    link_name = CharField(max_length=40, verbose_name='Название статьи')
    link = CharField(max_length=255, verbose_name='Ссылка')
    category = ForeignKeyField(Category, verbose_name='Категория')
    user = ForeignKeyField(User, verbose_name='Пользователь')

    class Meta:
        database = db

