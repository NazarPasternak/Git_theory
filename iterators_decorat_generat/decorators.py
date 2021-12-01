# python3 decorators.py
# ------------------------------------------------------------------>
#
# def hello():
#     print('Hello from function')
#
#
# hello()
# func = hello     #  присваиваем переменной func функцию hello
# print(type(func))
# func()           #  вызываем функцию

#
# writeln = print            # как в языке Pascal 😀
#
# writeln('Hello world!')
# writeln('Python')


# def start():
#     print("Execution of the start func")
#
#
# def stop():
#     print("Execution of the stop func")
#
#
# def pause():
#     print("Execution of the pause func")
#
#
# command = input()        # считываем название команды
#
# if command == 'start':
#     start()
# elif command == 'stop':
#     stop()
# elif command == 'pause':
#     pause()

#
# def start():
#     # тело функции start
#
#
# def stop():
#     # тело функции stop
#
#
# def pause():
#     # тело функции pause
#
#
# commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция
#
# command = input()        # считываем название команды
#
# commands[command]()      # вызываем нужную функцию через словарь по ключу       start()

# numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
#
# #print(len(numbers, key = ))
#
# def squares(num):
#     return num**2
#
# def third_power(num):
#     return num**3
#
# print(sorted(numbers, key=None))
# print(sorted(numbers, key=squares))
# print(sorted(numbers, key=third_power))

# print(max(numbers, key = check_squares))               # abs(10)



#  указываем функцию abs в качестве компаратора
# print(min(numbers, key=abs))        #  указываем функцию abs в качестве компаратора
# print(sorted(numbers, key=abs))     #  указываем функцию abs в качестве компаратора

# def decorator_first(function_1):
#     def wrapper():
#         function_1()
#         print('FIRST PART---------------------->')
#     return wrapper
#
# def decorator_end(function_2):
#     def wrapper():
#         function_2()
#         print('END PART------------------------->')
#
# def decorator_text(function_3):
#     def wrapper():
#         function_3()
#         print('Article')
#
#
# article_newspaper = decorator_first(decorator_end(decorator_text))
# article_newspaper()


# sozdat funct kotoraya budet logirovart deystviya v file.


        # python3 decorators.py
# ------------------------------------------------------------------>
# def transfer_file(func):
#     file1 = open('text.txt', 'a', encoding='utf-8')
#     res = 'Function ha been executed'
#     file1.write(res)
#
#
# @transfer_file
# def func_finished_succ():
#     def vipolnenie():
#         return vipolnenie
















