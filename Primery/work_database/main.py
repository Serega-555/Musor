from typing import final
import pymysql
from pymysql import connect, cursors
from config import *


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        passwd=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected")
    print("#" * 20)


    try:
        with connection.cursor() as cursor:
        
    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)