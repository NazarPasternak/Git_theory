# python3 files_11_17.py

# sozdat ryad function:

# 1. function shto proveryaet chislo v opredelommih granicah kotorie schituytsa s klaviaturi

# 2. function kotoraya kagdiy erlement voznosit v stepen

# 3. function kotoraya generiryet spisok chisel v zadanom diapazone

# 4. function kotoraya nahodit ynikalnie elementi spiska

# 5. priminit function 1 - 2 k spisku function 3 (map and filter using methods)

# 6. fucntion kotoraya vivodit spisok na ekran, sparashevaet polzovatlya zapisat li spisok v file, cherez prober
# ili sleshn (\n)

# 7. function kotoraya schitivaet file v spisok

# 1.
import random


def check(number):
    a, b = 10, 25
    return True if number in range(a, b) else False
    # if number in range(measures[0], measures[1]):
    #     return True
    # return False
# spisok = [i**2 for i in range(10)]
# print(*spisok)

# spisok = list(filter(check, spisok))
# print('res:', *spisok)
#def check(number, measures):

# print(check(17))
# # # ------------------------------------------------------------------>

# def power_element(elem):
#     power = 3
#     return elem**power
#
# print(power_element(77))

# # # ------------------------------------------------------------------>
# from random import randint
#
# def generate_spisok():
#     diap_1, diap_2 = int(input()), int(input())
#     range_spisok = int(input())
#     result = [randint(diap_1, diap_2) for i in range(range_spisok)]
#     return result
#
# x = generate_spisok()
# print(x)
# print('len_before:', len(x))
# # # ------------------------------------------------------------------>

# def check_unique_elements(spisok):
#     return list(set(spisok))
#
# y = check_unique_elements(x)
# print(y)
# print('len_after:', len(y))

# # # ------------------------------------------------------------------>


# new_y = list(filter(check,y))
# print(new_y)
# new_y_squared = list(map(power_element, new_y))
# print(new_y_squared)
# new_y_squared = list(map(str, new_y_squared))
# print("The list:" , new_y_squared)
#
# def write_to_file(l1):
#     choice = input(r"\n? or space")
#     with open("Data.txt", 'a' , encoding='utf-8') as input_file:
#         if choice == 'space':
#             for i in range(len(l1)):
#                 input_file.write(l1[i] + ' ')
#         else:
#             for i in range(len(l1)):
#                 input_file.write(l1[i] + '\n')
# write_to_file(new_y_squared)

# # # ------------------------------------------------------------------>

# file = open('languages.txt', 'r', encoding='utf-8')
# languages = [line.strip() for line in file.readlines()]
##or
# languages = [i.strip() for i in file.readlines()]
##or
# languages = list(map(str.strip, file.readlines()))
##or
# languages = list(map(lambda line: line.strip(), file.readlines()))

# print(languages)
# file.close()

# print(ord('\n'))
# print(ord('\r'))
# print(chr(10))
# print(chr(19))

# -------------------------------------->

# line = 'Python\n'
# line = line.rstrip()
# print(line)

# -------------------------------------->

# file = open('languages.txt', 'r', encoding='utf-8')
# line = file.readlines()         # считываем первую строку
#
# while line != '':              # пока не конец файла
#     print(line.strip())        # обрабатываем считанную строку
#     line = file.readline()     # читаем новую строк
# file.close()

# -------------------------------------->

# x = 'languages.txt'
# file = open('languages.txt', 'r', encoding='utf-8')
# result = file.readlines()
# print(*result[-3], sep='')
# file.close()

# -------------------------------------->

# file = open('text.txt', 'r', encoding='utf-8')
# sum = 0
# res = file.readlines()
# for i in range(len(res)):
#     if i == int():
#         sum += i
#     print(sum)
# print(res)
# file.close()
# sum = 0

# -------------------------------------->

# x = ['1234567\n', '2345678']
# sum = 0
# x = ['1', '2', '3', '4']
# for i in range(len(x)):
#     sum += x[i]
#     print(x[i], end='')
# print(sum)

# file = open('text.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line.strip())
# print(file.readlines)
# file.close()

# -------------------------------------->
# 11/19/2021 Class Work
from random import choice

# Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную
# строку из этого файла.

# with open('lines.txt', 'r', encoding='utf-8') as file1:
#     x = file1.readlines()
#     y = random.choice(x)
# print(y)

# -------------------------------------->

# Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число. Напишите программу,
# выводящую на экран сумму этих чисел.

# with open('numbers.txt', 'r', encoding='utf-8') as file1:
#     x = file1.readlines()
#     stripped_lines = []
#     for line in x:
#         stripped_lines.append(int(line.rstrip('\n')))
#     print(sum(stripped_lines))

# -------------------------------------->

# Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью
# символа табуляции (\t) разделена на три колонки:

# with open('prices.txt', 'r', encoding='utf-8') as file1:
#     x = file1.readlines()

# -------------------------------------->
from random import randint

# 3. function kotoraya generiryet spisok chisel v zadanom diapazone
def generate_spisok():
    diap_1, diap_2, range_spisok = int(input()), int(input()), int(input())
    result = [randint(diap_1, diap_2) for i in range(range_spisok)]
    return result

x = generate_spisok()
print(x)
print('len_before:', len(x))

# 1. function kotoraya beret modul kazdigo chisla i sortiruet znachenie po modulu - lambda + map
# 2. function kotoraya zapisuet sumy elementov tvoego spiska - vstroeynnaya function
# 3. function kotoraya filtruet chisla kvadrat kotorih privishayt 3000 lambda + filter

# 1.
def module(num):
    return (list(map(lambda x: abs(x), num)))

def module(x):
    x.sort(key=abs)
    return x

s = (module(x))
print(s)

# -------------------------------------->

# -------------------------------------->

# 3.
def kvadrat_chisel(z):
    return list(filter(lambda x: x**2 < 3000, z))

p = kvadrat_chisel(x)
print(p)
# -------------------------------------->

# 2

def num_ss(tup:list):
    return sum(tup)

o = num_ss(p)
print(o)





