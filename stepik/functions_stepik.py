
#   python3 functions_stepik.py
# # ------------------------------------------------------------------>

# def rectangle():
#     print('*' * 10)
#     for _ in range(14 - 2):
#             print('*' + ' ' * (10 - 2) + '*')
#     print('*' * 10)
# print('*' * 10, end=' ')

# def rectangle():
#     for _ in range(14 - 2):
#         print('*' + ' ' * (10 - 2) + '*')
# rectangle()

# def xyz():
#     for i in range(5):
#         print('*' + ' ' * 5 + '*')

# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1
#
# print_text('Python', 4)

#
# def draw_triangle(fill, base):
#     for i in range(1, base//2+2):
#         print(fill * i, end='')
#         print()
#     for i in range(base // 2, 0, -1):
#         print(fill * i, end='')
#         print()
#
# fill = input()
# base = int(input())
# draw_triangle(fill, base)


# name = 'Александр'
# surname = 'Пушкин'
# patronymic = 'Сергеевич'
# arr = []
# # for i in range(len(name)):
# arr.append(name[0] + surname[0] + patronymic[0])
#     arr.append(name[0])
# for i in range(len(surname(i[0]))):
#     arr.append(surname[0])
# for i in range(len(patronymic)):
#     arr.append(patronymic[0])
# print(*arr)



# def print_fio(name, surname, patronymic):
#     arr = []
#     name, surname, patronymic = input().upper(), input().upper(), input().upper()
#     arr.append(surname[0] + name[0] + patronymic[0])
#     print(*arr, end='')
#
# print_fio(name, surname, patronymic)


# def print_fio(name, surname, patronymic):
#     s = ''
#     for _ in range(3):
#         i = input().upper()
#         s = s + i[0]
#
# print_fio(s[1] + s[0] + s[2])

# объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper() + name[0].upper() + patronymic[0].upper())
#
#
# name, surname, patronymic = input(), input(), input()
# print_fio(name, surname, patronymic)

# def print_digit_sum(num):
#     sum = 0
#     for i in range(len(n)):
#         sum += num[i]
#         print(i)
#
# n = int(input())
# print_digit_sum(n)

# def print_digit_sum(num):
#     print(sum([int(i) for i in range(len(n))]))
# n = int(input())
# print_digit_sum(n)

# объявление функции
# def print_digit_sum(num):
#     print(sum([int(i) for i in str(num)]))
#     print(type(num))
#     pass
#
# n = int(input())
# print_digit_sum(n)

# -------------------------------------->

# def print_digit_sum(num):
#     print(sum([int(i) for i in num]))
# print_digit_sum(input())
#
# n = int(input())
# print_digit_sum(n)

# def swap(a, b):
#     a, b = b, a
#     print('a =', a)
#     print('b =', b)
#
# a = 4
# b = 3
# swap(a, b)
# print(a - b)

# -------------------------------------->

# n = int(input())
# result = 0
# while n > 0:
#     result += n % 10
#     n //= 10
# print(result)
# -------------------------------------->

# объявление функции
# def convert_to_miles(km):
#     return km * 0.6214
#
# num = int(input())
# print(convert_to_miles(num))
# -------------------------------------->

# def get_days(month):
#     if num in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     if num == 2:
#         return 28
#     if num in (4,6,9,11):
#         return 30
#
# # считываем данные
# num = int(input())
# print(get_days(num))

# OR

# def get_days(month):
#     m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return m[month - 1]
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))
# -------------------------------------->

# def get_factors(num):
#     arr = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             arr.append(i)
#     return arr
#
# n = int(input())
# # вызываем функцию
# print(get_factors(n))

# -------------------------------------->

# объявление функции
# def find_all(target, symbol):
#     index_c = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             index_c.append(i)
#     return index_c
#
# print(find_all('abcadbcaaa', 'a'))
# -------------------------------------->

# return  [i for i in range(len(target)) if symbol in target]

# -------------------------------------->

# объявление функции
# def find_all(target, symbol):
#     arr = []
#     for i, v in enumerate(target):
#         if v == symbol:
#             arr.append(i)
#     return arr
#
# s = input()
# char = input()
# # вызываем функцию
# print(find_all(s, char))

# -------------------------------------->

# print(merge([1, 2, 3], [5, 6, 7, 8]))
# print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
# l1 = [1, 2, 3]
# l2 = [2, 6, 4, 8]
# l3 = (l1 + l2)
# l3.sort()
# print(l3)
# -------------------------------------->

# def quick_merge(list1, list2):
#     result = []
#     p1 = 0
#     p2 = 0
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#     if p1 < len(list1):
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84]
# list_last = quick_merge(list1, list2)
# print(list_last)

# -------------------------------------->

# def quick_merge_2(list1, list2):
#     total_list = []
#     p1 = 0
#     p2 = 0
#     for i in range(int(input())):
#         l is = [int(y) for y in input().split()]
#
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] <= list2[p2]:
#             total_list.append(list1[p1])
#             p1 += 1
#         else:
#             total_list.append(list2[p2])
#             p2 += 1
#     if p1 < len(list1):
#         total_list += list1[p1:]
#     if p2 < len(list2):
#         total_list += list2[p2:]
#     return total_list

# python3 functions_stepik.py
# -------------------------------------->

# n, m = 5, 9
# a = [2, 8, 9, 11, 17]
# b = [3, 6, 9, 12, 45, 57, 88, 99, 101]
# i = j = 0
# c = []
# while i < n and j < m:
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
#     else:
#         c.append(b[j])
#         j += 1
#
# while i < n:
#     c.append(a[i])
#     i += 1
#
# while j < m:
#     c.append(b[j])
#     j += 1
# print(c, i, j)



# python3 functions_stepik.py
# -------------------------------------->

# n, m = 7, 9
# i = j = 0
# a = [4, 6, 7, 88, 99, 101, 111]
# b = [12, 14, 22, 45, 57, 66, 73, 84, 99]
# c = []
#
# while i < n and j < m:
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
#     else:
#         c.append(b[j])
#         j += 1
#
# while i < n:
#     c.append(a[i])
#     i += 1
# while j < m:
#     c.append(b[j])
#     j += 1

# print(c, n, m)

# chars = [c for c in 'abcdefg']
# print(chars)

# n = int(input())
# arr_lines = [input() for _ in range(n)]
# print(arr_lines)

# arr_lines = [str(input()) for _ in range(int(input()))]
# print(arr_lines)
#
# numbers = [(i, j) for i in range(1, 4) for j in range(3)]
# print(numbers)

# word = [int(c) * 2 for c in 12345]
# print(word)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert',
#             'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
#             'except', 'finally', 'try', 'for', 'from', 'global', 'if',
#             'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
#             'raise', 'return', 'while', 'yield']
#
# print([i[1:]for i in keywords])













































