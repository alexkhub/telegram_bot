# import sqlite3 as sql
#
# # from settings import settings
# from config import *
# import asyncio
#
#
# class Database():
#     def __init__(self, link_connect=DATABASE):
#         self.link_connect = link_connect
#
#     async def get_category(self, category) -> list:
#         connect = sql.connect(self.link_connect)
#         cursor = connect.cursor()
#         cursor.execute(f"SELECT * FROM category WHERE category_name='{category}'")
#         result = cursor.fetchall()
#         cursor.close()
#         connect.close()
#         return result
#
#     async def new_user(self, telegram_id) -> None:
#         connect = sql.connect(self.link_connect)
#         cursor = connect.cursor()
#         cursor.execute(f'INSERT INTO users (telegram_id) VALUES ({telegram_id});')
#         connect.commit()
#         cursor.close()
#         connect.close()
#         return None
#
#     async def new_link(self, link_name, link, category) -> None:
#         connect = sql.connect(self.link_connect)
#         cursor = connect.cursor()
#         cursor.execute(f"INSERT INTO links (link_name, link, category) VALUES ('{link_name}', '{link}', {category});")
#         connect.commit()
#         cursor.close()
#         connect.close()
#         return None
#
#
# database = Database()
# asyncio.run(database.new_link(link_name='Документация Django', link='https://django.fun/ru/docs/django/4.2/', category=1))


