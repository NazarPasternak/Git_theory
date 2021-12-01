#     python3 example.py
# Create database and create table

import sqlite3

from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('../../pythonProject/mydatabase.db')
        print('Connection has established')
        return con
    except Error:
        print(Error)


def sql_table(con, arg): # create table
    cursor = con.cursor()

    cursor.execute("CREATE TABLE data_clients(id integer PRIMARY KEY "
                   "AUTOINCREMENT, name_surname text,"
                   "credit_score int, available_balance int)")


    cursor.execute('''INSERT INTO data_clients(id, name_surname, credit_score, available_balance)
    VALUES(?,?,?,?,?)''', kort)

    con.commit()


con = sql_connection()
kort = (1, 'Alex_Cross', 850, 3000000)
sql_table(sql_connection(), kort)

#-------------------------------------------------------------------------------------------------------------------#
# <<<<<<<<<<<<<<<<<<Fill in data in table : оператором INSERT INTO>>>>>>>>>



