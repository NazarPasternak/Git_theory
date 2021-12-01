                       # 9/25/2021   # python3 tuples.py
# # ------------------------------------------------------------------>

# empty_tuple = ()                                      # пустой кортеж
# point = (1.5, 6.0)                                    # кортеж из двух чисел
# names = ('Timur', 'Ruslan', 'Roman')
# print(names)
# print(point)

# info = ('Timur', 'Guev', 28, 170, 60, False)          # кортеж из 6 элементов разных типов
# nested_tuple = (('one', 'two'), ['three', 'four'])

# a = (5,7,9)
# num = 0
# for i in a:
#     num += i
#     print(i)
#     print(num)

# -------------------------------------->
# s = 'симпотичный'
# a = list(s)
# a[4] = 'а'
# # print(a)
# s = ''.join(a)
# print(s)


# -------------------------------------->
#
# writer = ('Лев Толстой', 1827)
# print(writer)
# list_writer = list(writer)
# list_writer[1] = 1828
# list_tuple = tuple(list_writer)
# print(list_writer)

# # ------------------------------------------------------------------>

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
# print(sum((min(numbers), max(numbers))))


# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries[-2]
# print(index)
#
# city_name = 'Kyiv'
# city_year = 1000
# city = tuple(city_name), tuple(city_year)
# print(city)


# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]

# non_empty_tuples = [i for i in tuples if i != ()]
# print(non_empty_tuples)
# # ------------------------------------------------------------------>

# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = []
# for i in range(len(tuples)):
#     if tuples[i][:-1] == (100,):
#
#
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = []
# for i in range(len(tuples)):
#     new_tuples.append(i[-1])
#
# print(new_tuples)

# # ------------------------------------------------------------------>
# non_empty_tuples=[]
# for i in range(len(tuples)):
#   if len(tuples[i])!=0:
#     non_empty_tuples.append(tuples[i])
#
# print(non_empty_tuples)


# python3 tuples.py
# # ------------------------------------------------------------------>

# numbers = (0, 1, 3, 14, 2, 7, 9, 8, 10)
# print(numbers)

# # ------------------------------------------------------------------>

# sum = 0
# a = (3, 4, 5)
# for i in range(len(a)):
#     sum += a[i]
# print('res1:', sum)

# # ------------------------------------------------------------------>

# sum = 0
# a = (3, 4, 5)
# for i in a:
#     sum += i
# print('res2:', sum)

# # ------------------------------------------------------------------>

# s = 'симпотичный'
# print('first:', s)
# a = list(s)
# a[4] = 'а'
# # s = ''.join(a)
# print('second:', s)

# # ------------------------------------------------------------------>

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[2:-5])

# # ------------------------------------------------------------------>

# city_name = input()
# city_year = int(input())
# city = city_name, city_year
# print(city)

# # ------------------------------------------------------------------>

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]

# non_empty_tuples = [i for i in tuples if i != ()]
# print(non_empty_tuples)

# or this variant

# non_empty_tuples=[]
# for i in tuples:
#     if i != () :
#         non_empty_tuples.append(i)
# print(non_empty_tuples)

# # ------------------------------------------------------------------>

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for i in numbers:
#     print(i, end=' ')

# # ------------------------------------------------------------------>

# numbers = (1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for i in range(len(numbers)):
#     print(numbers[i])
# print(tuple(i for i in range(len(numbers))))

# # ------------------------------------------------------------------>

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# x = list(poet_data)
# x[2] = 'Mосква'
# poet_data = tuple(x)
# print(poet_data)

# # ------------------------------------------------------------------>

# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# a = 1
# for i in numbers:
#     a *= i
# print('res:', a)

# # ------------------------------------------------------------------>

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# languages = ('Python', 'C++', 'Java')
#
# print(*numbers, sep='\n')
# print(*languages, sep='\n')

# # ------------------------------------------------------------------>

# sorted() in tuples and sort() in lists:
# not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
# print(not_sorted_tuple)
#
# sorted_tuple = tuple(sorted(not_sorted_tuple))
# print(sorted_tuple)

# # ------------------------------------------------------------------>

# number = 12345
# tpl = tuple(str(number))
# print(tpl)

# # ------------------------------------------------------------------>

# notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
# x = ''.join(notes)
# y = '.'.join(notes)
# print(x) # res: DoReMiFaSolLaSi
# print(y) # res: Do.Re.Mi.Fa.Sol.La.Si

# # ------------------------------------------------------------------>

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# x = list(poet_data)
# x[2] = 'Mосква'
# poet_data = tuple(x)
# print(poet_data)
# print(*poet_data)

# # ------------------------------------------------------------------>
# 3
# Гуев 3
# Чаниев 5
# Барсуков 2
# Sample Output 1:
#
# Гуев 3
# Чаниев 5
# Барсуков 2
#
# Чаниев 5

# arr = []
# for i in range(int(input())):
#     name = input()
#     print('res:', *name, sep='')
#     if name[-1] >= '4':
#         arr.append(name)
# print(*arr, sep='\n')

# # ------------------------------------------------------------------>

# a, b, *tail = 1, 2, 3
# print(tail)

# # ------------------------------------------------------------------>

# a = 1,
# b, = 1,
# print(a)
# print(b)

# # ------------------------------------------------------------------>

# points = [('матан', 100), ('линал', 98), ('ангем', 90)]
# a, b = points[1]
# print(a, b)

# # ------------------------------------------------------------------>

# notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
# do, re, mi, *tail = notes
# print(tail)

# # ------------------------------------------------------------------>

# from math import*
#
# n = float(input())
# a = float(input())
# s= (3 * 2.0**2) / (4 * tan(pi / n))
# print(s)

# Почитав коментарии решил так: 1) импортировал math 2)n =int   a = float    3)находим решение верхней части формулы
# n * a**2     4) решение нижней части формулы 4*math.tan(math .pi /n  5) собираем фомулу и на печать

# # ------------------------------------------------------------------>

# tpl = (100, )
# print(tpl * 2)

# tpl = (100, 200, 300, 400, 500)
# tpl[1] = 700
# print(tpl)

# x = 'Beegeek loves Stepik'
# x.split
# print(x)

# a = True
# b = False
# print(a or b)

# numbers = [1, 2, 3, 4, 5, 8, 10, 12, 15, 17]
# res = 0
# count = 0
# for i in numbers:
#     if (i % 2 ==0 ):
#         count += 1
#         print(i)
# print('count:', count)

# a = 6
# b = 10
# print(a == 10 and b == 10)

# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
# print(res)

# print(7 % 2 == 1)

# # ------------------------------------------------------------------>

# print(bool('Beegeek')) # res: T
# print(bool([17, 20, 21])) # res: T
# print(bool(17)) # res: T
# print(bool(['apple', 'cherry'])) # res: T
# print(bool()) # res: F
# print(bool('')) # res: F
# print(bool(0)) # res: F
# print(bool([])) # res: F

# # ------------------------------------------------------------------>

# print(isinstance((1), int))
# print(type((1)))

# # ------------------------------------------------------------------>

# ininstance()
# type()
# function that return bool variable, called - предикатом

# # ------------------------------------------------------------------>

# объявление функции
# def func(num1, num2):
#     if num1 % num2 == 0:
#         return True
#     else:
#         return False

# считываем данные
# num1, num2 = int(input()), int(input())
# вызываем функцию
# x = func(num1, num2)
# print(x)
# print(func(10, 2))


# my_set = {[3],}
#
# print(my_set)
