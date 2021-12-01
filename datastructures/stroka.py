#                          python3 stroka.py
# # ------------------------------------------------------------------>
# text = "Such a lovely place"
# for index in range(len(text)):
#     print(text[index])

# --------------------------------------->
# text = "Such a lovely place"
# for letter in text:
#     print(letter)

# --------------------------------------->
# alphabet = "abcdefghijk"
# for letter in alphabet:
#     print(letter)

# --------------------------------------->

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# s = "0123 567_910"
# print(s[])

# stroka = 'abcdefghijklmnop'
# for i in range(0, len(stroka), 2):
#     print(stroka[i], end='\n')

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')\


# (-1,-len(s)-1,-1)
# s = 'abcdefg'
# s = input()
# for i in range(-1, -len(s) -1, -1):
#     print(s[i])


#                          python3 stroka.py
# # ------------------------------------------------------------------>
# s = ''
# for _ in range(3):
#     i = input()
#     s = s + i[0]
# print(s[1], s[0], s[2])

# sur = input()
# name = input()
# middle_n = input()
# print(name[0], sur[0], middle_n[0])

# num = str(int(input()))
# sum = 0
# for i in range(len(num)):
#     sum = sum + int(num[i])
# print(sum)

#                          python3 stroka.py
# # ------------------------------------------------------------------>
# Sample Input 1:
# Hi Python
# Sample Output 1:
# Цифр нет

# s = input()
# n = 'Цифр нет'
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         n = 'Цифра'
# print(n)

# s = input()
# n = 'Exeception of digit'
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         n = 'Digit'
# print(n)
#                          python3 stroka.py
# # ------------------------------------------------------------------>

# n = input()
# sym1 = '*'
# sym2 = '+'
# count_sym1 = 0
# count_sym2 = 0
# for i in range(len(n)):
#     if n[i] in sym1:
#         count_sym1 += 1
#     elif n[i] in sym2:
#         count_sym2 += 1
# print('Символ + встречается', count_sym2, 'раз')
# print('Символ + встречается', count_sym1, 'раз')

#                          python3 stroka.py
# # ------------------------------------------------------------------>
#
# n = 'aabbcc'
# # n = input()
# count = 0
# for i in range(len(n) - 1):
#     print(n[i])
#     if n[i] == n[i + 1]:
#         count += 1
# print(count)


# s = 'qwertyu'
# for i in range(-1, -len(s) - 1, -2):
#     print(s[i])
#                          python3 stroka.py
# # ------------------------------------------------------------------>

# Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и
# 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
# ("ауоыиэяюёе")
# "бвгджзйклмнпрстфхцчшщ")

# s = input().lower()
# vowel = 'ауоыиэяюёе'
# count_vowel = 0
# consonant = 'бвгджзйклмнпрстфхцчшщ'
# count_consonant = 0
# for i in range(len(s)):
#     if s[i] in vowel:
#         count_vowel += 1
#     elif s[i] in consonant:
#         count_consonant += 1
# print('Количество гласных букв равно', count_vowel)
# print('Количество согласных букв равно', count_consonant)


# Глупая критика не так заметна, как глупая похвала.

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])


# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# s = input()
# if s[0::] == s[::-1]:
#     print('YES')
# else:
#     print('NO')

# n = input()
# if n.title() == n:
#     print('YES')
# else:
#     print('NO')
#                          python3 stroka.py
# # ------------------------------------------------------------------>

# n = 'Swap Case'
# n = input()
# n_swap = n.swapcase()
# print(n_swap)

# n = input()
# if 'хорош' in n.lower():
#     print('YES')
# else:
#     print('NO')


# if 'хорош' in input().lower():
#     print('YES')
# else:
#     print('NO')


# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i] == s.lower():
#         count += 1
# print(count)

#                          python3 stroka.py
# # ------------------------------------------------------------------>
# На вход программе подается одна строка. Напишите программу, которая выводит:
#
# третий символ этой строки;
# предпоследний символ этой строки;
# первые пять символов этой строки;
# всю строку, кроме последних двух символов;

# все символы с четными индексами;
# все символы с нечетными индексами;
# все символы в обратном порядке;
# все символы строки через один в обратном порядке, начиная с последнего.

# s = 'abcdefghijklmnopqrstuvwxyz'
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[-1:-len(s) -1: -1])
# print(s[-1: -len(s) -1: -2])

#                          python3 stroka.py
# # ------------------------------------------------------------------>
# c
# y
# abcde
# abcdefghijklmnopqrstuvwx
# acegikmoqsuwy
# bdfhjlnprtvxz
# zyxwvutsrqponmlkjihgfedcba
# zxvtrpnljhfdb

# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))

# s = input()
# count = 1
# for i in range(len(s)):
#     if s[i] == ' ':
#         count += 1
# print(count)

#                          python3 stroka.py
# # ------------------------------------------------------------------>
# s = input()
# print(s.count(' ') + 1)

# Sample Input 1:
# АааГГЦЦцТТттт
#
# Sample Output 1:
# Аденин: 3
# Гуанин: 2
# Цитозин: 3
# Тимин:


# s = input().lower()
# adenin_count = s.count('а')
# print('Аденин:', adenin_count)
# gyanin_count = s.count('г')
# print('Гуанин:', gyanin_count)
# cytozin_count = s.count('ц')
# print('Цитозин:', cytozin_count)
# tumun_count = s.count('т')
# print('Тимин:', tumun_count)

# n = int(input())
# k = 0
# for i in range(len(n)):
#     s = input()
#     if s.count('11') >= 3:
#         k += 1
# print(k)

# k = 0
# for i in range(int(input())):
#    s = input()
#    if s.count('11') >= 3:
#        k += 1
# print(k)

#                          python3 stroka.py
# # ------------------------------------------------------------------>
# s = 'l33t 3301'
# s = input()
# count = 0
# for i in s:
#     if i in '0123456789':
#         count += 1
# print(count)
#                          python3 stroka.py
# # ------------------------------------------------------------------>

# s = 'www.yandex.com'
# s = input()
# if s.endswith('.com') or s.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

#                          python3 stroka.py
# # ------------------------------------------------------------------>
1.#
# age = 27
# txt = 'Hello my name is Ale, I am ' + str(age)
# print(txt)

# 2.use format:
# age = 27
# txt = 'Hello my name is Ale, I am  {}'.format(age)
# print(txt)

# 3.
# name = 'Nazar'
# age = 28
# occupation = 'data analyst'
# txt = 'Name is {} he is {} years old, occupation is {}'.format(name,age, occupation)
# print(txt)

# 4. f - stroka
# name = 'Nazar'
# age = 28
# occupation = 'data analyst'
# print(f'Name is {name}, he is {age} years old, occupation {occupation}.')

# year = 2010
# price = '10k'
# coin = 'Bitcoin'
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, coin)
# print(s)

# print(ord('1'))

# for i in range(26):
#     print(chr(ord('A') + i))

#                          python3 stroka.py
# # ------------------------------------------------------------------>
# 65
# 70
# Sample Output 1:
# A B C D E F

# for i in range(26):
#     print(chr(ord('A') + i))
# a, b = int(input()), int(input())

# a, b = int(input()), int(input())
# for i in range(a, b):
#     print(chr(i), end='')

n = int(input())
my_list = []
for i in range(1, n+1):
    my_list.append(i)
print(my_list)














