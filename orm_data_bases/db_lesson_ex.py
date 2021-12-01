# python3 db_lesson.py
# Class Work: Connect Data Base to Python 10/8/21
# # ------------------------------------------------------------------>
# # ------------------------------------------------------------------>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Create connection to DB: try/except/finally:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import sqlite3
#
# from sqlite3 import Error
#
# con = sqlite3.connect('workers.db')
#
# def sql_connection():
#     try:
#         con = sqlite3.connect('workers.db')
#         print('DB connected')
#     except Error:
#         print("The mistake has occurred. DB doesn't work appropriately")
#
#     finally:
#         con.close()
#         print('Connection has been closed')
#
# sql_connection()
#
#                                                python3 db_lesson.py
# ---------------------------------------------------------------------------------------------------->
# <<<<<<<<<<<<<<<<<<<<<<<Have created the connection and added values into table:>>>>>>>>>>>>>>>>>>>>>>

import sqlite3

from sqlite3 import Error
#
# def sql_connection():
#     try:
#         con = sqlite3.connect('mydatabase.db') # connection to data base
#         print('Connection is established: Database is created in memory')
#         return con
#
#     except Error:
#         print(Error)
#
#     # finally:
#     #     con.close() ???
#
# # Create Table в методе execute():
# def sql_table(con):
#     cursor = con.cursor()
#
#     # cursor.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, "
#     #                   "department text, position text, hireDate text)")
#
#     # In original is used to cursorObj.execute()
#     cursor.execute("CREATE TABLE loan_adv(id integer PRIMARY KEY AUTOINCREMENT, "
#                    "name text, surname text, occupation text, salary real, loan real)")
#
#     # cursor.exe
#     con.commit()
#
#
# con = sql_connection()
# sql_table(con)



#-------------------------------------------------------------------------------------------------------------------#
# CREATE TABLE INSERT TABLE:
#
# import sqlite3
#
# from sqlite3 import Error
#
# def sql_connection():
#     try:
#         con = sqlite3.connect('mydatabase.db')
#         return con
#     except Error:
#         print(Error)
#
#
# def sql_table(con):
#     cursor = con.cursor()
#
#     '''cursor.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, "
#                       "department text, position text, hireDate text)")'''
#
#     cursor.execute("CREATE TABLE mortgage(id integer PRIMARY KEY AUTOINCREMENT, name text, credit_score integer)")
#
#     cursor.execute("INSERT INTO mortgage VALUES(NULL, 'Nazar' , 800)")
#     con.commit()
#
#
# con = sql_connection()
# sql_table(con)

#-------------------------------------------------------------------------------------------------------------------#
# <<<<<<<<<<<<<<<<<<<<<<Insert data in table - Вставка данных в таблицу>>>>>>>>>>>>>>>>>>>>>>>>.
#
# import sqlite3
# from sqlite3 import Error
#
#
# def sql_connection():
#     try:
#         con = sqlite3.connect('mydatabase.db')
#         return con
#     except Error:
#         print(Error)

# def sql_create_table(con, arg):
#     cursor = con.cursor()
#     cursor.execute("CREATE TABLE arg(id integer PRIMARY KEY AUTOINCREMENT, name text, "
#                    "credit_score integer )")
#     con.commit()
#
# entity = ("Petrovych",100)
#
# def sql_update_tables(con, kort):
#     cursor = con.cursor()
#     cursor.execute('''INSERT INTO mortgage(id, name, credit_score) VALUES(NULL,?, ?)''', kort)
#
#     #cursor.execute("INSERT INTO mortgage VALUES(NULL, 'Nazar' , 800)")
#
#
# con = sql_connection()
# sql_update_tables(con, entity)
# import sqlite3





# # ------------------------------------------------------------------>

# import sqlite3
# from sqlite3 import Error
#
#
# def sql_connection():
#     try:
#         con = sqlite3.connect('mydatabase.db')
#         return con
#     except Error:
#         print(Error)
#
# def sql_create_table(con, arg):
#     cursor = con.cursor()
#     cursor.execute("CREATE TABLE arg(id integer PRIMARY KEY AUTOINCREMENT, name text, "
#                    "credit_score integer )")
#     con.commit()
#
# entity = ("Petrovych",100)
#
#
# def sql_update_tables(con, kort):
#     cursor = con.cursor()
#     cursor.execute('''INSERT INTO mortgage(id, name, credit_score) VALUES(NULL,?, ?)''', kort)
#
#     #cursor.execute("INSERT INTO mortgage VALUES(NULL, 'Nazar' , 800)")
#
#
# con = sql_connection()
# sql_update_tables(con, entity)

#
# con = sqlite3.connect('mydatabase.db')
#
# cursorObj = con.cursor()
#
# cursorObj.execute('create table if not exists projects(id integer, name text)')
#
# data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
#
# cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)
#
# con.commit()
#
# con.close()
#
# con = sqlite3.connect('mydatabase.db')
#
# cursorObj = con.cursor()
#
# cursorObj.execute('create table if not exists projects(id integer, name text)')
#
# data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
#
# cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)
#
# con.commit()
#
# con.close()

# # ------------------------------------------------------------------>




#                        python3 db_lesson_ex.py
# Class Work: Connect Data Base to Python 10/10/21
# # ------------------------------------------------------------------>
# # ------------------------------------------------------------------>
#-------------------------------------------------------------------------------------------------------------------#

# import sqlite3
# from sqlite3 import Error
#
# def sql_connection():
#     try:
#         con = sqlite3.connect('mydatabase.db')
#         return con
#     except Error:
#         print(Error)

#-------------------------------------------------------------------------------------------------------------------#
# def new_sql_table(con, name_of_table, field1, field2):
#     cursor = con.cursor()
#     sql_cmd = f'''CREATE TABLE {name_of_table}(id integer PRIMARY KEY AUTOINCREMENT, {field1} text,{field2} text)'''
#     cursor.execute(sql_cmd)
#
# con = sql_connection()
# new_sql_table(con, 'WTF', 'marrige_status', 'mortgage')
#-------------------------------------------------------------------------------------------------------------------#
#
# def sql_insert(con, data):
#     cursor = con.cursor()
#     cursor.execute('''INSERT INTO loan_table(id, name, loan_approval, credit_score, salary) '
#                       'VALUES(NULL, ?, ?, ?, ?)''', data)
#     con.commit()
#
#
# def sql_update(con,name_of_table):
#     cursor = con.cursor()
#     sql_cmd = '''UPDATE {} SET name = "Vasya" where credit_score = 810'''.format(name_of_table)
#     #cursor.execute('UPDATE loan_table SET name = "Egor" where id = 1')
#     con.commit()
#
#
# def get_info_from_keyabord():
#     print("Print name, loan_approval, credit_score,salary")
#     name,loan_approval,credit_score, salary = input(), input(), int(input()),int(input())
#     return name, loan_approval, credit_score, salary


#-------------------------------------------------------------------------------------------------------------------#
# Class Work 10/11/21 DB
# python3 db_lesson_ex.py






















