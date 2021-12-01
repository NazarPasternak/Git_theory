# 10/17/2021
#          python3 cycle_for_while.py
# # ------------------------------------------------------------------>

# num = int(input())
# count = 0
# while num < 6 and num > 1:
#     if num == 5:
#         count += 1
#     num = int(input())
# print('Counted 5 are:', count)

# # ------------------------------------------------------------------>

# num = int(input())
# count = 0
# while 0 < num < 6:
#     if num == 5:
#         count += 1
#     num = int(input())
# print(count)

# # ------------------------------------------------------------------>
# «стоп», «хватит», «достаточно»

# text = input()
# count = 0
# while text != 'стоп' and text!= 'хватит' and text != 'достаточно':
#     count += 1
#     text = input()
# print('amount of words before:', count)

# # ------------------------------------------------------------------>
# text = input()
# count = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     count += 1
#     text = input()
# print(count)
# # ------------------------------------------------------------------>

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)
#
# res: 5*4*3*2*1
# # ------------------------------------------------------------------>

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)

# # ------------------------------------------------------------------>

# num = 12345
# # product = 1
# while num != 0:
#     last_digit = num % 10
#     # product = product * last_digit
#     num = num // 10
# print(last_digit)

# num = 12345
# while num != 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10

# # ------------------------------------------------------------------>
# num = 5086334
# new_num = []
# while num != 0:
#     last_digit = num % 10
#     new_num.append(last_digit)
#     num = num // 10
# print(new_num)

# num = 5086334
# while num != 0:
#     last_digit = num % 10
#     print(last_digit, end="")
#     num = num // 10
# # ------------------------------------------------------------------>
# Sample Input 1:
#
# 26670
# Sample Output 1:
#
# Максимальная цифра равна 7
# Минимальная цифра равна 0

# # ------------------------------------------------------------------>
# n = 12345678
# max = 0
# min = 9
# while n > 0:
#     last_digit = n % 10
#     if last_digit > max:
#         max = last_digit
#     if last_digit < min:
#         min = last_digit
#     n = n // 10
# print(max)
# print(min)


# n = 12345678
# minimum = 9
# maximum = 0
# while n > 0:
#     x = n % 10
#     if x < minimum:
#         minimum = x
#     if x > maximum:
#         maximum = x
#     n = n // 10
# print('Максимальная цифра равна', maximum)
# print('Минимальная цифра равна', minimum)



# # ------------------------------------------------------------------>
# n = 12345678
# x = str(n)
# max = max(x)
# min = min(x)
# print(max)
# print(min)

# 5678
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.


# num = 5678
# num = int(input())
# sum = 0
# count = 0
# mult = 1
# last_number = num % 10
# while num > 0:
#     digit = num % 10
#     sum += digit
#     count += 1
#     mult *= digit
#     average = sum / count
#     first_num = digit
#     first_last_number = digit + last_number
#     num = num // 10
# print(sum, count, mult, average, first_num, first_last_number, sep='\n')


# # ------------------------------------------------------------------>
# num =
# print(num // 100)

# num = 5678
# while num > 9:
#     digit = num // 10
#     num //= 10
# print(digit)


# n = 1234
# while n > 0:
#     n //= 10
#     n //= 10
# print(n)

# n = 1234
# while n > 9:
#     last = n % 10
#     n = n // 10
#     print(n)
# print(last)


# n = 123456789
# while n > 99:
#     n //= 10
# print(n % 10)


# a = 1234
# while a > 99:
#     a = a // 10
#     print(a)
# print(a % 10)
#                          python3 cycle_for_while.py
# # ------------------------------------------------------------------>

# a = 5
# b = 9
# a = b
# print('a:', a)
# print('b:', b)



# n = 123456789
# max = 0
# min = 9
# while n > 0:
#     digit = n % 10
#     if digit > max:
#         max = digit
#     elif digit < min:
#         min = digit
#     num = num // 10
# print('Max number:', max)
# print('Min number:', min)


# n = 12345678
# max = 0
# min = 9
# while n > 0:
#     last_digit = n % 10
#     if last_digit > max:
#         max = last_digit
#     if last_digit < min:
#         min = last_digit
#     n = n // 10
# print(max)
# print(min)

#                          python3 cycle_for_while.py
# # ------------------------------------------------------------------>
# num = 12345678
# print(num % 10)
# while num > 99:
#     num = num // 10
# print(num % 10)

# # ------------------------------------------------------------------>
# num = 111111
# last_digit = num % 10
# answer = 'YES'
# while num != 0:
#     digit = num % 10
#     if last_digit != digit:
#         answer = 'NO'
#     num = num // 10
# print(answer)

# # ------------------------------------------------------------------>
# n = int(input())
# flag = True
# a = n % 10
# while n != 0:
#     last = n % 10
#     if last != a:
#         flag = False
#     n = n // 10
# if flag == True:
#     print("YES")
# else:
#     print("NO")

# # ------------------------------------------------------------------>
# n = int(input())
# m = n % 10
# answer = 'YES'
# while n != 0:
#     if m != n % 10:
#         answer = 'NO'
#     n = n // 10
# print(answer)
# # ------------------------------------------------------------------>
# n = int(input())
# while n % 10 == n // 10 % 10:
#     n //= 10
# print('YES' if n < 10 else 'NO')
# # ------------------------------------------------------------------>
# Нашла последнюю цифру - образец.
# Завела счетчик=0
# Цикл с %10, где сравнивала с образцом.
# Если !=, счетчик +1
# Если после цикла счетчик != 0, значит, разные цифры были...Ну, уже поняли...

# print('YES' if n < 10 else 'NO')
# # ------------------------------------------------------------------>
# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#         break               # останавливаем цикл если встретили делитель числа
# if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# print(20 % 6 == 0)

# a, b, c = len(input()), len(input()), len(input()),
# average_numb = a + b + c - max(a,b,c) - min(a,b,c)
# if max(a,b,c) - average_numb - min(a, b, c):
#     print('YES')

#                          python3 cycle_for_while.py
# # ------------------------------------------------------------------>
# count = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     count += num
#     print(count)

# num = int(input())
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     num //= 10
#
# if flag == True:
#     print('Число', num, 'содержит цифру 7')
# else:
#     print('Число', num, 'не содержит цифру 7')


# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')
#
#
# res: 9*8*7*6*5*4*2*0*
# res: 9*8*7*6*5*4*3*1*0*

# print(0 % 2 == 0)
# # ------------------------------------------------------------------>

# num = 17
# for i in range(2, num+1 ):
#     if num % i == 0:
#         print(i)
#         break

# num = int(input())
# for i in range(1, num +1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or  78 <= i <= 87:
#         continue
#     print(i)

# # ------------------------------------------------------------------>
# print(12345 // 2 + 1 )

# for _ in range(10):
#     print('A')


# print('A' * 10, sep='\n')


#                          python3 cycle_for_while.py
# # ------------------------------------------------------------------>
# num = 1
# while num < 101:
#     if num % 7 == 7:
#         num += 1
# print(num)

# i = 1
# while i < 101:
#     if i % 10 == 7:
#         # continue
#         print(i)
#     i += 1

# i = 1
# while i < 101:
#     if i % 10 == 7:
#         continue
#     i += 1
#     print(i)

# for i in range(100, 1, -1):
#     print(i)

# a = 0
# for i in range(1, 100, 2):
#     a += i
# print(a)


# n = 12345
# product = 1
# while n != 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# n = 12345
# while n > 0:
#     n = n % 10
#     n //= 10
# print(n)

#                          python3 cycle_for_while.py
# # ------------------------------------------------------------------>
# for hours in range(24):
#     for minutes in range(10):
#         for seconds in range(10):
#             print(hours,':', minutes, ':', seconds)



# for i in range(3):
#     print('i:', i)
#     for j in range(3):
#         print('j:', j)
#         # if i == j:
#         print('i:', i, 'j: ', j)


# for i in range(8):
#     print('*', end='')
#     print('*' * 6)


# for i in range(6):
#     print ( '*' * 8, end='\n')

# for i in range(8):
#     for j in range(10):
#         print('*', end='')
#     print()

# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

#
# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)


# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()


# for i in range(4):
#     for j in range(3):
#         print('*', end='')
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print(i, end='')
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(5):
#         print(i + 1, end='')
#     print()
#
# # [print(f'{i} ' * 5) for i in range(1, int(input()) + 1)]


#                          python3 cycle_for_while.py
# # ------------------------------------------------------------------>
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(n + j, sep='')
#     print()


# for i in range(3):
#     for j in range(3):
#         # if i == j:
#             # continue
#         print(i, j)

#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         sum = i + j
#         print(i, '+', j,'=', sum)
#     print()


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()


'''Имеется 100100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 10 рублей,
за корову – 55 рублей, за теленка – 0.50.5 рубля и надо купить 100 голов скота?
Примечание. Используйте вложенный цикл for'''
# ------------------------------------------->
# total = 0
# for bull in range(1, x):
#     for cow in range(1, x):
#         for telya in range(0.5, 6):
#
# if 10x + 5y + 0.5z = 100
#
# ------------------------------------------->
# total = 0
# for x in range(n):
#     for y in range():
#         for z in range(1, 45):
#             if x ** 2 + y ** 2 + z ** 2 == 2020:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# ------------------------------------------->
# for i in range(3):
#     for j in range(3):
#         print('i:', i, 'j:', j, sep=' ')
# ------------------------------------------->
# for i in range(5):
#     for j in range(4):
#         print('*', end='')
#     print()
# res:
# ****
# ****
# ****
# ****
# ****
# ------------------------------------------->
# for i in range(5):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# res:
# *
# **
# ***
# ****
# *****
# ------------------------------------------->
# res:
# *
# **
# ***
# **
# *

# n = int(input())
# for i in range(1, n // 2 + 2):
#     print('*' * i, end='')
#     print()
# for i in range(n // 2, 0, -1):
#     print('*' * i, end='')
#     print()

# ------------------------------------------->

'''Имеется 100100 рублей. Сколько быков, коров и телят можно купить на все эти 
деньги, если плата за быка – 1010 рублей, за корову – 55 рублей, за теленка – 
0.50.5 рубля и надо купить 100100 голов скота?'''

# total = 0
# for x in range(1, 100):
#     for y in range(1, 100):
#         for z in range(1, 100):
#             if 10*x + 5*y + 0.5*z == 100 and x + y + z == 100:
#                 total += 1
#                 print('x:', x, 'y:', y,'z:',  z)
# print('Total:', total)
# ------------------------------------------->

'''Решите уравнение в натуральных числах 28n + 30 k + 31 m = 365
Примечание. Используйте вложенный цикл for. В первую очередь запишите решение 
с наименьшим значением nn.'''

# total = 0
# for n in range(1, 12):
#     for k in range(1, 12):
#         for m in range(1, 12):
#             total += 1
#             if 28*n + 30*k + 31*m == 365:
#                 print('n:', n, 'm:', m, 'k:', k)
# print('Total:', total)
# ------------------------------------------->

# total = 1
# for a in range(1, 151):
#     for b in range(1, 151):
#         for c in range(1, 151):
#             for d in range(1, 151):
#                 for e in range(1, 151):
#                     total += 1
#                     if a**5 + b**5 + c**5 + d**5 == e**5:
#                         print(a, b, c, d, e)
# print('Total:', total)

# ------------------------------------------->
# 7.8
# Sample Input:
# 3
# Sample Output:
# 1
# 2 3
# 4 5 6

# n = 5
# for i in range(n + 1):
#     for j in range(i + 1):
#         print(i + 1, end='')
#     print()


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()

# задача похожа на лесенку из цифр, но есть разница.
# 1. создаем переменную num равную 1 для счетчика
# 2. первый цикл for из строк, назвал row, range от 1 до входящего
   # числа + 1
# 3. второй цикл  for уже из колонок, в range от 1 до строк row+1
# 4. принт num, не забываем про end=' ', между апострафами пробел,
#    чтобы цифры были отделены пробелом
# 5. увличиваем нашу переменную num на 1, чтобы счетчик работал
# 6. завершаем цикл принт () чтобы выйти из цикла

# ------------------------------------------->
# # 7.9

# n = 5
# num = 1
# for row in range(1, n + 1):
#     for col in range(1, row + 1):
#         print(num, end='')
#         num += 1
#     print()

# res:
# Sample Input:
# 3
# Sample Output:
#
# 1
# 2 3
# 4 5 6
# ------------------------------------------->

