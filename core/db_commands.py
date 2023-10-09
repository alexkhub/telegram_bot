import sqlite3 as sql

# from settings import settings
from config import *
import asyncio


# def database_connect(func):
#     def database_script():
#         connect = sql.connect(DATABASE)
#         cursor = connect.cursor()
#         func()
#         cursor.close()
#         connect.close()
#
#     return database_script()


async def get_categorys(command) -> list:
    connect = sql.connect(DATABASE)

    cursor = connect.cursor()
    cursor.execute(command)
    result = cursor.fetchall()

    cursor.close()
    connect.close()
    return result


# print(asyncio.run(get_categorys('SELECT * FROM category ')))
# print(asyncio.run(get_categorys('SELECT * FROM category WHERE category_id=1 ')))


class Database():
    def __init__(self, connect=DATABASE):
        self.connect = connect

    async def database_functions(self, command):
        connect = sql.connect(self.connect)
        cursor = connect.cursor()
        cursor.execute(command)
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result

    async def new_user(self,  telegram_id):
         self.database_functions(f'INSERT INTO users (telegram_id) VALUES ({telegram_id});')


database = Database()
print(asyncio.run(database.database_functions(command='SELECT * FROM category WHERE category_id=1 ')))

asyncio.run(database.new_user(12))
