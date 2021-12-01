#python3 lists.py

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[16])
# print(primes[-1])
# print([len(primes)-1])
# print(primes[0:6])
# min = min(primes)
# max = max(primes)
# print(min + max)
# average = sum(primes)/ len(primes)
# print(average)



# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Zelenuy'
# rainbow[-1] = 'Valya'
# print(rainbow)



# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# languages.reverse()
# print(languages)
# print(languages[::-1])


# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# print(numbers1 * 2 + numbers2 * 9 + numbers3)


# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14,
#            8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print("The length of list 'numbers'",len(numbers))
# print("The 1st el", numbers[-1])
# print("The reversed list", numbers[::-1])
# if 5 and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
#
# print(numbers[1:-1])
#
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))
# numbers.sort()
# print(numbers)

#                       python3 lists.py
# ------------------------------------------------------------------>
# arr = []
# arr2 = list()
# print("Input the amount of string:")
# n = int(input())
# for i in range(n):
#     print("Input the srting", i+1)
#     s = input()
#     arr.append(s)
# print("The list:", *arr)
# Brav0


#                       python3 lists.py
# ------------------------------------------------------------------>


# arr = []
# print('Fill in amount of numbers')
# amount = int(input())
# for i in range(amount):
#     print('Input please', i + 1, 'number')
#     num = int(input())
#     arr.append(num**3)
#
# print("List:",arr)

#                       python3 lists.py
# ------------------------------------------------------------------>

# spisok = []
# print('Input the amount of the strings:')
# n = int(input())
# for i in range(n):
#     print("Input the srting", i+1)
#     s = input()
#     spisok.extend(s)
#
# print('The list of chars:', spisok)



#                       python3 lists.py
# ------------------------------------------------------------------>

# l = []
# print('Fill in the number:')
# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
#         l.append(i)
#     else:
#         continue
# print('Array of dividing elements of the num:', l)


#                      python3 lists.py
# ------------------------------------------------------------------>
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sum = 0
# for i in range(len(numbers)):
#     sum += numbers[i]**2
# print(sum)
# ------------------------------------------------------------------>

# print('Fill  in amount of numebrs')
# n = int(input())
# for i in range(n):
#     print('Insert numbers', i + 1)
#     num = int(input())
#     x = num**2 + num*2 + 1
#     print('The value of the function with num=', num, ":", x)
#

# ------------------------------------------------------------------>

# l = []
# print('Input the amount of the strings:')
# n = int(input())
# for i in range(n):
#     stroka = input()
#     if stroka not in l:
#         l.append(stroka)
# print('Output:', l)

# a = int(input())
# b = int(input())
# s = 0.5 * a * b
# print(s)


#                      python3 lists.py
# ------------------------------------------------------------------>
# ...........................KORTEGU................................

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# my_tuple = (num1, num2, num3, num4)
# print(my_tuple)

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# my_tuple = (num1, num2, num3, num4)
# print(my_tuple)

# amount_tuple = int(input())
# for i in range(amount_tuple):
#     print('Input amount of', i, 'elements')
#     num_input = input()
#     my_typle = (num_input,)
#     print(my_typle)


# list_tuple = list(my_tuple)
# print('Intital data list:', l)
# print('Incremented elements from tuple:', list_tuple)
#
# print("Input the amount of nums:")
# amount = int(input())
# for i in range(amount):
#     print("Input", i, "number")
#     num = int(input())
#     l.append(num)

# tuple_numb = (5, 6, 7, 8, 9, 5, 10, 11, 'Alex', 'Cross')
#
# print('Count similar element')
# argument = 5
# sim_elem = tuple_numb.count(argument)
# print('Number', argument, 'has', sim_elem, 'similar elements')

#   python3 lists.py
# # ------------------------------------------------------------------>
# even_numbers = list(range(0, 10, 2))
# print(even_numbers)# список содержит четные числа [0, 2, 4, 6, 8]
#
# odd_numbers = list(range(1, 10, 2))   # список содержит нечетные числа [1, 3, 5, 7, 9]
# print(odd_numbers)

# alpahabet = 'abcdefghigklmnopqrstuvwxyz'
# n = int(input())
# print(list(alpahabet[:n]))

# my_list = []
# for i in range(int(input())):
#     my_list += (chr(97 + i))
# print(my_list)

# n = int(input())
# mylist = []
# for i in range(n):
#     mylist += (list(chr(ord('a') + i)))
# print(mylist)

#   python3 lists.py
# # ------------------------------------------------------------------>
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes.index(61))
# primes.

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[-1])
#
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[0:6])

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# min_num = min(numbers)
# max_num = max(numbers)
# print(min_num + max_num)

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# count = 0
# for item in range(len(evens)):
#     # count += 1
#     average = sum(evens) / len(evens)
# print(average)
#
# numbers = [2, 4, 6, 8, 10]
# print(len(numbers))

#   python3 lists.py
# # ------------------------------------------------------------------>
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[6] = 'Фиолетовый'
# print(rainbow)

# # ------------------------------------------------------------------>
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[-1: -len(languages) - 1: -1])


#   python3 lists.py
# # ------------------------------------------------------------------>
# numbers = [1]  # создаем пустой список
# numbers[1] = 1
# numbers[2] = 2
# numbers[3] = 3
# print(*numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13]
# numbers[1] = 100
# print(numbers)

#   python3 lists.py
# # ------------------------------------------------------------------>

# n = int(input())
# my_list = []
# for i in range(n):
#     n_list = input()
#     my_list.append(n_list)
#     print(my_list)

#   python3 lists.py
# # ------------------------------------------------------------------>
# Для тех кто застрял
#
# 1. создаем пустой список sp = []
# 2. цикл for i in range(26):
# 3. добавляем в список и сразу умножаем    sp.append(chr(ord('a') + i)*(i+1))
# 4. выводим (без отступа) print(sp)


# print(ord('b'))
#
# n = chr(97)
# print(n)

#   python3 lists.py
# # ------------------------------------------------------------------>
# my_list = []
# for i in range(26):
#     my_list.append(chr(ord('a') + i) *(i + 1))
# print(my_list)
#
# for i in range(26):
#     print(chr(ord('A') + i))

#   python3 lists.py
# # ------------------------------------------------------------------>
# Sample Input 1:
# 5
# 1
# 2
# 3
# 4
# 5
# Sample Output 1:
# [1, 8, 27, 64, 125]
#
# n = int(input())
# my_list = []
# for i in range(n):
#     n_list = int(input())
#     my_list.append(n_list**3)
# print(my_list)

#   python3 lists.py
# # ------------------------------------------------------------------>
# Sample Input 2:
# 25
# Sample Output 2:
# [1, 5, 25]

# n = int(input())
# my_list = []
# for i in range(1, n+1):
#     if n % i == 0:
#         my_list.append(i)
# print(my_list)
#
# print(25 % 3)

#   python3 lists.py
# # ------------------------------------------------------------------>
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[-1: -len(numbers)-1 : -1])
# print('YES' if 5 and 17 in numbers else 'NO')
# del numbers[0]
# del numbers[-1]
# print(numbers)

#   python3 lists.py
# # ------------------------------------------------------------------>
# Sample Input:
# 3
# abc
# def
# ghi
# Sample Output:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#
# n = int(input())
# my_list = []
# for i in range(n):
#     text = input()
#     my_list.extend(text)
# print(my_list)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(numbers)):
#     print(numbers[i], end=' ')

# numbers = [0, 9, 2, 3, 4, 5, 7, 7, 8, 9, 10]
# for num in numbers:
#     print(num, end=' ')

# numbers = [0, 9, 2, 3, 4, 5, 7, 7, 8, 9, 10]
# print(*numbers)


#   python3 lists.py
# # ------------------------------------------------------------------>
# my_list = []
# # numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# # for i in numbers:
# #     my_list.append(i**2)
# # print(sum(my_list))

#   python3 lists.py
# # ------------------------------------------------------------------>
# f(x)=x2+2x+1
#
# my_list = []
# my_numbers = []
# n = int(input())
# for i in range(1, n + 1):
#     number = int(input())
#     my_numbers.append(number)
#     res = number**2 + 2 * number + 1
#     my_list.append(res)
#
# print(*my_numbers, sep='\n')
# print()
# print(*my_list, sep='\n')

#   python3 lists.py
# # ------------------------------------------------------------------>

# my_list = []
# n = int(input())
# for i in range(n):
#     num = int(input())
#     my_list.append(num)
# del my_list[my_list.index(max(my_list))]
# del my_list[my_list.index(min(my_list))]
# print(*my_list, sep='\n')

# my_list = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# # del my_list[my_list.index(max(my_list))]
# del my_list[(my_list.index(max(my_list)))]

#   python3 lists.py
# # ------------------------------------------------------------------>
# my_list_zero = []
# my_list_more = []
# my_list_less = []
# n = int(input())
# for i in range(n):
#     num = int(input())
#     if num == 0:
#         my_list_zero.append(num)
#     elif num > 0:
#         my_list_more.append(num)
#     elif num < 0:
#         my_list_less.append(num)
#
# print(*my_list_less, sep='\n')
# print(*my_list_zero, sep='\n')
# print(*my_list_more, sep='\n')

#   python3 lists.py
# # ------------------------------------------------------------------>
# my_list = []
# n = int(input())
# for i in range(n):
#     rep = input()
#     if rep not in my_list:
#         my_list.append(rep)
# print(*my_list, sep='\n')

#   python3 lists.py
# # ------------------------------------------------------------------>

# spisok = []
# n = int(input())
# for i in range(n):
#     a = input()
#     spisok.append(a)
# zapros = input()
# for i in spisok:
#     if zapros.lower() in i.lower():
#         print()
#         print(i)

#   python3 lists.py
# # ------------------------------------------------------------------>

# numbers = input().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# s = 'Python is the most powerful language'
# x = s.split()
# print(s)
# res: ['Python', 'is', 'the', 'most', 'powerful', 'language']

# numbers = input().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])


# ip = '192.168.1.24'
# numb = ip.split('1')
# print(numb)

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# numbers = input().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     print(i)

# words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
# s = ' '.join(words)
# print(s)
# res: Python is the most powerful language


# words = ['Мы', 'учим', 'язык', 'Python']
# res = ' '.join(words)
# print(res)


#   python3 lists.py
# # ------------------------------------------------------------------>

# print(*(input().split()), sep='\n')

# s = input()
# l = s.split()
# print(*l, sep='\n')

#   python3 lists.py
# # ------------------------------------------------------------------>
# sp = input().split()
# for i in sp:
#     print(i[0], end='.')

#   python3 lists.py
# # ------------------------------------------------------------------>
# x = 'C:\Windows\System32\calc.exe'
# s = input().split('\\')
# print(*s, sep='\n')

# ip = '192.168.1.24'
# numbers = ip.split('\\')
# print(*(input().split()), sep='\n')

#   python3 lists.py
# # ------------------------------------------------------------------>
# input_info = 'qwerty and password'

# text = input()
# n = input()
# print(n.join(text))

# input_info = 'qwerty and password'
# print(*input_info, sep=input())


# Друзья, задачка интересная, но на самом деле совсем не сложная.)
# Решал через вложенные циклы:
# Внешний для i в диапазоне(длина(список_введённых_цифр))
# Внутренний для j в диапазоне(i+1, длина(список_введённых_цифр))
# Если список_введённых_цифрх[i] == список_введённых_цифр[j]
# счётчик +1.


# my_list = list(input().split())
# count = 0
# for i in range(len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             count += 1
# print(count)

# names = ['Gvido', 'Roman' , 'Timur']
# print(names)
# # names.insert(-1, 'Anders')
# # print(names)
# names.insert(3, 'Josef')
# print(names)
# names.insert(-1, 'THIS')
# print(names)
# print(names.index('THIS'))

# names = ['Alex', 'Nick', 'Sam']
# print(names.pop(1))
# print(names)

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# print(numbers)
#
# numbers.extend([4,5,6])
# print(numbers)
#
# del numbers[0]
# print(numbers)
#
# numbers.insert(3, 25)
# print(numbers)
#
# numbers *=2
# print(numbers)

#   python3 lists.py
# # ------------------------------------------------------------------>
# text = input().lower().split()
# a = text.count('the')
# b = text.count('an')
# c = text.count('a')
# sum = a + b + c
# print('Общее количество артиклей:', sum)


# s, c = input().lower().split(), 0
# articles = ('a', 'an', 'the')
# for i in s:
#     if i in articles:
#         c += 1
# print('Общее количество артиклей:', c)


# print(max(data).index())
# print(data.index(max(data)))

# x = int('3 4 5 2 1')
# d = list(x.split())



# решал по колхозу)
# создаем список b
# 1. переводим цифры в инпут с помощью for
# 2.находим индекс для max числа и для min и обозначаем переменными
# 3.обозначаем переменными max и min число
# 4.b[индекс max] =min число
# b[индекс min] = max число
# выводим [*b]

# 10 9 8 7 6 5 4 3 2 1

# l = [int(i) for i in input().split()]
# d = list(l)
# print(type(d[0]))
# a = d.index(max(d))
# # print(a)
# b =d.index(min(d))
# d[a], d[b] = d[b], d[a]
# print(*d)

# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# del numbers[-1]
# print(numbers)

# numb = '345 1 4 9849 -5 -787 -364 543 23 6 75 234 564'

# l = [int(i) for i in input().split()]
# my_list = list(l)
# my_list.sort()
# print(*my_list)
# my_list.sort(reverse = True)
# print(*my_list)

# numbers = []
# for i in range(1, 11):
#     numbers.append(i)
# print(numbers)

# chars = [i for i in 'abcdefg']
# print(chars)

# n = int(input())
# lines = [input() for _ in range(n)]
# print(lines)

# chars = [c for c in 'abcdefg']
# print(chars)

# evens = [i for i in (range(0, 22, 3))]
# print(evens)

# numbers = [i * j for i in range(3, 6) for j in range(4)]
# print(numbers)

# words = ['one', 'two', 'three', 'four', 'five', 'six']
# [i for i in numbers]
# word = 'Hello'
# print([c * 2 for c in word])
# res: ['HH', 'ee', 'll', 'll', 'oo']
#   python3 lists.py

# # ------------------------------------------------------------------>
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
#             'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [i[1:] for i in keywords]
# print(new_keywords)

# ----------------------------------->

# lengths = [len(i) for i in keywords]
# print(lengths)

# new_keywords = [i for i in keywords if len(i) >= 5]
# print(new_keywords)



# numbers = [i**2 for i in range(1, int(input()) + 1)]
# print(*numbers, sep='\n')


# numbers = [i for i in range(1, int(input()) + 1)]
# print(*numbers, sep='\n')

# n = [i**3 for i in range(input().split())]
# print(*n, sep='\n')




# [m[0] for m in words if len(m) == 3]['o', 't', 's']

# print(*[int(i)**3 for i in input().split()])

# print(*[i for i in input().split()], sep='\n')

# print(*[i for i in input() if i in '0123456789'], sep='')

# print(*[i for i in input() if i in 0 < i < 10], sep='')

# print(*(i for i in input() if i.isdigit()), sep="")


# print(*[int(i)**2 for i in input().split() if int(i)**2 % 2 ==0 and int(i)**2%10 !=4], sep=' ')

# x = '1,2,3,4,5,6,7,8,9'
# print(14 // 4)

# print(*[i for i in input().split()], sep='\n')

# print(*[int(i) for i in input() if i in '1234567890'], sep='')

# n = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# print([i for i in n if len(i) >= 5])


# palindromes = [i for i in range(100, 1001) if i // 100 == i % 10]
# print(palindromes)

# # ------------------------------------------------------------------>
#   LIST COMPREHENTION
# n = []
# for i in range(10):
#     n.append(0)
# print(n)

# num = [0] * 10
# print(num)

# chars = [c for c in 'abcdefg']
# print(*chars, sep='-', end='/end')

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [i[1:] for i in keywords]
# print(new_keywords)

# palindromes = [i for i in range(100, 10001) if i // 100 == i % 10]
# print(palindromes)


# python3 lists.py
# # ------------------------------------------------------------------>
# m = 3
# obj = [[ i + j*m  for i in range(m) ] for j in range(m)]
# print(obj)