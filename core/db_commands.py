import sqlite3 as sql

# from settings import settings
from config import *

def get_categorys() -> list:
    connect = sql.connect(DATABASE)

    cursor = connect.cursor()
    cursor.execute('SELECT * FROM category ')
    category = cursor.fetchall()

    cursor.close()
    connect.close()
    return category

print(get_categorys())