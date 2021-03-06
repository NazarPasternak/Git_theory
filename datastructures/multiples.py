# python3 multiples.py
# # ------------------------------------------------------------------>
       # Создание множеств
       # Пустые множества
       # Встроенная функция set()
       # Вывод множеств

# К неизменяемым (immutable) типам относятся: целые числа (int), числа с плавающей точкой (float),
# комплексные числа (complex), логические переменные (bool), кортежи (tuple), строки (str) и неизменяемые множества (
# frozen set). К изменяемым (mutable) типам относятся: списки (list), множества (set), словари

# my_set = set()
# print(my_set)

# # ------------------------------------------------------------------>

# numbers = {2, 4, 6, 8, 10}                  #res: {2, 4, 6, 8, 10}
# languages = {'Python', 'C#', 'C++', 'Java'} #res: {'Java', 'C++', 'Python', 'C#'}
# mammals = {'cat', 'dog', 'fox', 'elephant'} #res: {'elephant', 'fox', 'dog', 'cat'}
# print(numbers)
# print(languages)
# print(mammals)

# # ------------------------------------------------------------------>

# Встроенная функция set()
# print(set(range(10)))     # множество из элементов последовательности # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(set([1, 2, 3, 4, 5]))  # множество из элементов списка # {1, 2, 3, 4, 5}
# print(set('abcd'))           # множество из элементов строки # {'b', 'c', 'a', 'd'}
# print(set((10, 20, 30, 40))) # {40, 10, 20, 30}
#
#
# print(set([]))  # пустое множество из пустого списка   # set()
# print(set(''))  # пустое множество из пустой строки    # set()
# print(set(()))  # пустое множество из пустого кортежа  # set()

# # ------------------------------------------------------------------>

# Дубликаты при создании множеств
# print({2, 2, 4, 6, 6})          #res: {2, 4, 6}
# print(set([1, 2, 2, 3, 3]))     #res: {1, 2, 3}
# print(set('aaaaabbbbccccddd'))  #res: {'b', 'd', 'a', 'c'}

# # ------------------------------------------------------------------>

# print({1, 2, [5, 6], 7})   # множество не может содержать список    # Error
# print({1, 2, {5, 6}, 7})   # множество не может содержать множество # Error
# print({1, 2, (5, 6), 7}) # res: {1, 2, (5, 6), 7}  res: {1, 2, (5, 6), 7}
#
# print(set(['']))  # res: {''}
# print(set())      # res: set()
# print(set([]))    # res: set()
# print(set(()))    # res: set()
# print(set())    # res: set()
# print({})         # res: {}

# print(set('aaabcccc    11222')) # res: {'b', 'c', ' ', '2', '1', 'a'} # res: 6

# # ------------------------------------------------------------------>

# print(len(set(input())))
# numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
# amount = 0
# for i in range(len(numbers)):
#     amount += 1
# print(amount)
#
# average = max(numbers) / amount
# print(average)


# numbers = {[1,2,3,4,5]}
# print(numbers)

# myset1 = set([1, 2, 3, 4, 5])
# print(myset1) # res: {1, 2, 3, 4, 5} / set
#
# myset2 = set('12345')
# print(myset2) # res: {'3', '1', '4', '2', '5'} / set
# print(myset1 == myset2)

# # ------------------------------------------------------------------>