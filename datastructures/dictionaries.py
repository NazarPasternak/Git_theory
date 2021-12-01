# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# for i in users:
#     for key in i:
#         print(key)



#                   python3 dictionaries.py
# # ------------------------------------------------------------------>

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

# for i in capitals:
#     for key in i:
#         print(key, i[key])
# -------------------------------------->
# Methods of dict(): keys(), values(), items():

# for key in capitals.keys():
#     print(key)
# -------------------------------------->
# for key in capitals.values():
#     print(key)
# -------------------------------------->
# for key, values in capitals.items():
#     print(key,'-', values)
# res:
# Россия - Москва
# Англия - Лондон
# Чехия - Прага
# Бразилия - Бразилиа
# -------------------------------------->
# items() - method

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# for i in capitals.items():
#     print(i)
# res: typle
# ('Россия', 'Москва')
# ('Англия', 'Лондон')
# ('Чехия', 'Прага')
# ('Бразилия', 'Бразилиа')

# -------------------------------------->
# Распаковка ключей словаря:

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# print(*capitals, sep='\n')
# res:
# Россия - Москва
# Англия - Лондон
# Чехия - Прага
# Бразилия - Бразилиа

                          # python3 dictionaries.py
# # ------------------------------------------------------------------>
# Сортировка словаря - функции sorted()

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

# lambda function:
# for key, value in sorted(capitals.items(), key = lambda x: x[1]):
#     print(value)

# sorted() function:
# for key in sorted(capitals):
#     print(key)

# res:
# Англия
# Бразилия
# Россия
# Чехия
                          # python3 dictionaries.py
# # ------------------------------------------------------------------>
# n = int(input())
# my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
#            '7': 'seven', '8': 'eight', '9': 'nine'}
# print(*my_dict, end=' ')
# for i in str(n):
#     for key in my_dict:
#         if key == i:
#             print(my_dict[key], end=' ')
#
#
# print(*[my_dict[key] for key in input()])

# -------------------------------------->
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# print(*sorted([i['name'] for i in users if i['phone'][-1] == '8']))

# если разжевать :)
# list_new = []
# for i in users:
#     if i['phone'][-1] == '8':
#         list_new.append(i['name'])
# print(*sorted(list_new))

# -------------------------------------->
# new_list = []
# for i in users:
#     if i['emails'] == '':
#         new_list.append(i['name'])
# print(*sorted(new_list))

                          # python3 dictionaries.py
# # ------------------------------------------------------------------>
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
#         print(result)
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# print(result[num])

# -------------------------------------->
# method get()
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# print(result)
#
# # res: {9: 1, 8: 1, 32: 2, 1: 5, 10: 4, 23: 3, 4: 2, 2: 6}

# python3 dictionaries.py
# -------------------------------------->

# info = {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# info['address'] = '95 Broadway Av.'
# print(info)
# last_elem = info.popitem()
# print(last_elem)

# -------------------------------------->



