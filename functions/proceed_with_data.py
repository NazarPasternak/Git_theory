# CLASS WORK 11.14.2021
# TOPICS:  map / filter/ reduce / lambda / functions as objects


# def foo(x , y):
#     if x<y:
#         return "X is less than y"
#     else:
#         return "y is less than x"
#
# def foo(x , y):
#     if x<y:
#         return "X is less than y"
#     print("asfaf")
#     if x == y:
#         return "they are equal"
#     return "Y is less than x"
#
#
# def foo(x, y):
#     if x==y:
#         return "equal"
#     return "Yes, y>x" if x<y else "No, x>y"



# python3 proceed_with_data.py
# # ------------------------------------------------------------------>

# doc string

# Egor Python, [Nov 14, 2021 at 12:45:24 PM]:
# ...def foo(x, y):
#     if x==y:
#         return "equal"
#     return "Yes, y>x" if x<y else "No, x>y"
#
# def foo(x:int , y:int) ->str:
#     """
#     Function which compares two nums:
#     :param x: int num to compare
#     :param y: int num to compare
#     :return: Result of comparing two nums (str)
#     """
#     if x<y:
#         return "X is less than y"
#     else:
#         return "y is less than x"
#
#
# foo()

# python3 proceed_with_data.py
# # ------------------------------------------------------------------>

# def foo(*args, **kwargs):
#     print('======================================')
#     print(f'The args: {args}')
#     print('======================================')
#     print(f'The kwargs: {kwargs}')
#     print('======================================')
#     return args
# #foo(15, 25, 21, a=1, b=2, c=3, d=4, e=5)
#
# x = foo(15, 25, 21, 22, 2, "sfa", None , a=1, b=2, c=3, d=4, e=5)
# x, y, z , *additional_info = x
# print(f'The x: {x},The y:{y}, The z:{z}')
# print(additional_info)


# python3 proceed_with_data.py
# # ------------------------------------------------------------------>

# def foo(x:int , y:int) ->str:       # тут нет гарантии что попадёт на вход именно инт
#     """
#     Function which compares two nums:
#     :param x: int num to compare
#     :param y: int num to compare
#     :return: Result of comparing two nums (str)
#     """
#     if not (isinstance(x, int) or not isinstance(y, int)) and \
#             (not isinstance(x, float) or not isinstance(y, float)):
#         raise ValueError("Unsupported types")

#     return "X is less than y" if x<y else "y is less than x"
#
#
# print(foo(11, 11))


# python3 proceed_with_data.py
# # ------------------------------------------------------------------>
# realizivat funct kotoraya budet prinimat dve stroki na vhod i vozvrashyat samuyu bolshuyu stroku


# # def bigger_str(x: str, y: str) -> str:
#     """
#     :param x: string
#     :param y: string
#     :return: int
#     """
#     # if not (isinstance(x, str)) or not isinstance(y, str):
#     #     raise ValueError('Unsupported type to compare')
#     # return 'equal' if len(x) == len(y) else (x if len(x) > len(y) else y)
#     #
#     # if len(x) == len(y):
#     #     return  'equal'
#     # else:
#     #     if len(x) > len(y):
#     #         return x
#     #     else:
#     #         return y
#
# # print(bigger_str('Hello', 'World'))
# # print(bigger_str('Hello11', 'World'))


# python3 proceed_with_data.py
# # ------------------------------------------------------------------>


# def foo(a,b,c, **kwargs):
#     print(kwargs)
# foo(a=1, b=2, c=3, d=4, e=5)


# python3 proceed_with_data.py
# # ------------------------------------------------------------------>


# def bigger_str(x: str, y:str) -> str:
#     """
#     :param x: string
#     :param y: string
#     :return: int
#     """
#     if not (isinstance(x, str)) or not isinstance(y, str):
#         raise ValueError ('Unsupported type to compare')
#     return 'equal' if len(x) == len(y) else (x if len(x) > len(y) else y)
#
#     # if len(x) == len(y):
#     #     return  'equal'
#     # else:
#     #     if len(x) > len(y):
#     #         return x
#     #     else:
#     #         return y
#
# print(bigger_str('Hello', 'World'))
# print(bigger_str('Hello11', 'World'))

# def foo(a,b, c , **kwargs):
#     print(f'a={a},b={b},c={c}')
#     print(kwargs)
#
# foo(a=1, b=2, c=3, d=4, e=5)

# def foo(*args, **kwargs):
#     print('======================================')
#     print(f'The args: {args}')
#     print('======================================')
#     print(f'The kwargs: {kwargs}')
#     print('======================================')
#     return args
# #foo(15, 25, 21, a=1, b=2, c=3, d=4, e=5)
#
# x = foo(15, 25, 21, 22, 2, "sfa", None , a=1, b=2, c=3, d=4, e=5)
# x, y, z , *additional_info = x
# print(f'The x: {x},The y:{y}, The z:{z}')
# print(additional_info)


# from random import randint
#
# x = [randint(1, 540) for _ in range(25)]
# print("Generated list before:", x)
# my_lambda0 = lambda x, y: x+y
# my_lambda1 = lambda num: num**2
# new_x = tuple(map(my_lambda1, x))       # list/set/tuple/
# print("Generated list after:",new_x)

# my_f = lambda num: num<10000
# x = list(map(lambda num: num**2, [randint(1, 540) for _ in range(25)]))
# print(x, len(x) , sep = '\n' , end='\n')
# new_x = x.copy()
# new_x = list(filter(my_f, new_x))
# print(new_x)
#def standart_foo(x, y):
#     return x+y
# new_lambda = lambda x, y: x+y
# print(new_lambda(25, 21))
#
# new_x = map(lambda num: num**2, x)


# def foo(a):
#     return 12+a
#
# print(foo(25))      # common print
# x = foo(21)         # результат виконання функції записали у змінну
#
# x = foo
# print(x)        # <function foo at 0x0000021F2FC86160>
# print(x(13))

# def compare_by_second(point):
#     return point[1]
#
#
# def compare_by_sum(point):
#     return point[0] + point[1]
#
#
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
# print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа
#
#
# numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]
#
# positive_numbers = list(filter(lambda x: x > 0, numbers))      #  положительные числа
# large_numbers = list(filter(lambda x: x > 50, numbers))        #  числа, большие 50
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))     #  четные числа
#
# def foo(x):
#     return True if x>0 else False
#
# print(positive_numbers)
# print(large_numbers)
# print(even_numbers)
#
# words = ['python', 'stepik', 'beegeek', 'iq-option']
#
# new_words1 = list(filter(lambda w: len(w) > 6, words))    #  слова длиною больше 6 символов
# new_words2 = list(filter(lambda w: 'e' in w, words))      #  слова содержащие букву e
#
# print(new_words1)
# print(new_words2)