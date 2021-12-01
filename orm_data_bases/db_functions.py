# python3 db_functions.py
# # ------------------------------------------------------------------>

import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('../../pythonProject/mydatabase.db')
        print('Connection is estabished')
        return con

    except Error:
        print(Error)

def create_table(con, table_name, field1, value1, field2, value2, field3, value3, field4, value4):
    cursor = con.cursor()
    cursor.execute(f"CREATE TABLE {table_name}(id integer PRIMARY KEY AUTOINCREMENT, {field1} {value1}, "
                   f"{field2} {value2},{field3} {value3}, {field4} {value4})")

def insert_table(con, table_name, field1, field2, field3, field4, kort):
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO {table_name}(id, {field1}, {field2}, {field3}, {field4}) VALUES(NULL, ?, ?, ?, ?)", kort)
    con.commit()

def get_info_from_keybord():
    print('Please input name_surname, age, credit_score, available_credit')
    name_surname, age, credit_score, available_credit = input(), int(input()), int(input()), float(input())
    return name_surname, age, credit_score, available_credit

def selector(con, table_name):
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    # x = [print(rows) in  rows in cursor.fetchall()] print on the screen
    return [row for row in rows ]



# SELECT sql FROM sqlite_master
# WHERE tbl_name = 'table_name' AND type = 'table'



