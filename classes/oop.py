########################################################################################################################
#CLASS WORK 9/21/2021
#FILES....
# ------------------------------------------------------------------>


# 1. Method read:
# file2 = open('test.txt', 'r+', encoding='utf-8')
# content = file2.read()
# print(content)
# file2.close()


# 2. Method readline:
# file2 = open('test.txt', 'r+', encoding= 'utf-8')
# for i in range(3):
#     language = file2.readline()
#     print(language)
# file2.close()

# 3.Method readlines which makes list from envisioned of the file
# file2 = open('test.txt', 'r+', encoding='utf-8')
# language = file2.readlines()
# print(language)
# file2.close()
# print(type(language))
# print(language[0])
# print(sorted(language))

# # ------------------------------------------------------------------>
# Create file1 and make a function that connect two lists with functuion zip
#
# file1 = open('test.txt', 'r', encoding='utf-8')
#
# def transformation(file):
#     resulted_list = list(map(str.strip, file.readlines())) #because we need to rid of from '\n'
#     return resulted_list
# #res: ['Python', 'Java', 'Javascript', 'C#', 'C', 'C++', 'PHP', 'R', 'Objective-C']
#
#
# languages_list = transformation(file1)
# print(languages_list)
#
#
# file2 = open('creator.txt', 'r', encoding='utf-8')
# creators_list = transformation(file2)
# print(creators_list)

# # ------------------------------------------------------------------>

# def connect_lists(list_1, list_2):
#     res_dict = dict(zip(list_1, list_2))
#     return res_dict
#
#
# resulted_dict = connect_lists(creators_list, languages_list)   # dictionary
# print("Resulted dictionary:", resulted_dict)
#
#
# def check_dict_methods(operation, dictionary = dict()):
#
#     # operation = input('Make your choice: ')
#     # if operation not in '1234567891011':
#     #     continue
#
#     if operation == 1:
#         print('Copy similar dictionary')
#         new_dict = dictionary.copy()
#         return new_dict
#
#     elif operation == 2:
#         print('Return key from dictionary:')
#         key = input()
#         return dictionary.get(key[1])
#
#     elif operation == 3:
#         print('Return key, value:')
#         return dictionary.items()
#
#     elif operation == 4:
#         print('Output all values data:')
#         return dictionary.values()
#
#     elif operation == 5:
#         print('Output all keys:')
#         return dictionary.keys()
#
#
#     elif operation == 6:
#         print('Take last key value as tuple')
#         return dictionary.popitem() # takes out a last value in tuple  from the dict
#
#     elif operation == 7:
#         print('Add some data key:')
#         return dictionary.setdefault('C++')
#
#     elif operation == 8:
#         print('')
#         return dictionary
#
#
#     elif operation == 10:
#         print("Clearing the dict")
#         return dictionary.clear(2)
#
#
#
#
# print('Input number of operation')
# operation = int(input())
#
# print(check_dict_methods(operation, resulted_dict))
# operation = int(input())


# l =[]
#
# with open('customers.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)
#     for j in file:
#         l.append(file)
# with open('example.txt' , 'w', encoding='utf-8') as file2:
#     file2.write("Helllooooo!!")
#
# if file.closed and file2.closed:
#     print("Both files are closed")



########################################################################################################################
# 9/22/2021 CLassWork
# Kontekstniy meneger - 17.3
#
# with open('creator.txt', 'r', encoding='utf-8') as creator:
#     for i in creator:
#         print(i) # i here is string!!! not an index.
#
#
# with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
#     input_file.read

# import random
#
# print('Please fill in a string:')
# s = input()
# list1.append(s)


# list1 = []
# print('How many lines do you want to input?')
# number_of_string = int(input())
# for i in range(number_of_string):
#     print('Please input:', i, 'string')
#     s = input()
#     list1.append(s)
#
# print('Our list:', list1)
# new_set = set(list1)
# print('Unique values in our set:', new_set)
#
# with open('creator.txt', 'r', encoding='utf-8') as input_file, open('test.txt', 'w', encoding='utf-8') as output_file:
#     output_file.writelines(new_set)
#
# # ..............................................>
#
# def create_our_list():
#     list1 = []
#     print('How many lines do you want to fill input?')
#     number_of_string = int(input())
#     for i in range(number_of_string):
#         print('Please input:', i, 'string')
#         s = input()
#         list1.append(s)
#     new_set = set(list1)
#     return new_set
#
# def print_info(new_set):
#     print('The unique values of the data_structure:', new_set)
#
#
# def work_with_file(new_set):
#     with open('creator.txt', 'r', encoding='utf-8') as input_file, open('test.txt', 'w',
#                encoding='utf-8') as output_file:
#         output_file.writelines(new_set)
#

# data = create_our_list()
# print_info(create_our_list())
# work_with_file(create_our_list())




########################################################################################################################
# Home Work
# DICTIONARIES
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
# names = list(sorted([users['name'] for users in users if users['phone'][-1] == '-8']))
# print(*names, sep=' ')

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

# for i in capitals:
#     for key in i:
#         print(key, i[key])

# for key in capitals.keys():
#     print(key)
# for key in capitals.values():
#     print(key)
# or this:
# for key, values in capitals.items():
#     print(key,'-', values)




# for values in capitals:
#     print(capitals[values])

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

# for i in capitals:
#     for key in sorted(i):
#         print(key, i[key])
# for i in c
# res:capitals:
# #     for key, values in sorted(i.items(), key = lambda x: x[1]):
# #         print(key, values)
# Бразилиа
# Лондон
# Москва
# Прага
#
# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# for item in capitals.item():
#     print(item)
                          # python3 dictionaries.py
# # ------------------------------------------------------------------>
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
# # names = list(sorted(users[m]))
# for i in users:
#     if i['phone'][-1] == '8':
#         print(i['name'], end=' ')

#
# for key in sorted(capitals):
#     print(key)

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

# # ------------------------------------------------------------------>
#
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

# print(*sorted([i['name'] for i in users if i['phone'][-1] == '8']))

# print(*sorted([i['name'] for i in users if i['email'][0]=='']))

# если разжевать :)
# list_new = []
# for i in users:
#     if i['phone'][-1] == '8':
#         list_new.append(i['name'])
# print(*sorted(list_new))

# -------------------------------------->
# new_list = []
# for i in users:
#     if i['email'] == '':
#         new_list.append(i['name'])
# print(*sorted(new_list))


# -------------------------------------->

# CLASS WORK9/24/2021
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # 1.
# for i in a:
#     if i <= 21 and i != 13:
#         print(i, end=' ')

# 2.
# new_list = []
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             new_list.append(a[i])
# print(new_list)

# 3
# data = input().split(',')
# for i in range(len(data)):
#     print(data[i])

# 4
# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
# Выведите первый и последний элемент списка + первый и последний елемент  кортежа
# print('Please input data with coma in:')
# n = input().split(',')
#
# new_list = []
# new_tuple = tuple()
# for i in range(len(n)):
#     new_list.append(int(n[i]))
# print('Output list:', new_list)
# new_tuple = tuple(new_list)
# print('Output tuple:', new_tuple)
# print(type(new_list[0]))
# print(type(new_tuple[0]))

# 5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# new_a = set(a)
# print(new_a)
# new_b = set(b)
# print(new_b)
# dif = new_a - new_b
# print(dif)
# print(set(a)- set(b))

# 6

# def create_our_list():
#     list1 = []
#     print('How many lines do you want to fill input?')
#     number_of_string = int(input())
#     for i in range(number_of_string):
#         print('Please input:', i, 'string')
#         s = input()
#         list1.append(s)
#     new_set = set(list1)
#     return new_set
#
# def print_info(new_set):
#     print('The unique values of the data_structure:', new_set)
#
#
# def work_with_file(new_set):
#     with open('creator.txt', 'r', encoding='utf-8') as input_file, open('test.txt', 'w',
#                encoding='utf-8') as output_file:
#         output_file.writelines(new_set)
#

# data = create_our_list()
# print_info(create_our_list())
# work_with_file(create_our_list())

# print('Please input name of file and type of mode:')
# name_of_file = input()
# mode = input()
#
# def file_name(name_of_file, mode):
#     new_list = []
#     with open(name_of_file, mode, encoding='utf-8') as new_file:
#         if mode == 'r':
#             new_list = new_file.read()
#         # return new_list
#         elif mode == 'w':
#             print('Input what do you want to write into the file:')
#             data = input()
#             new_file.write(data)
#         return new_list
#
#
# print(file_name(name_of_file, mode))


# -------------------------------------->
#
# num = int(input())
# count = 0
# while 0 < num < 6:
#     if num == 5:
#         count += 1
#     num = int(input())
# print(count)

# -------------------------------------->
#
# def divider(num):
#     n_list = []
#     for i in range(1, num + 1):
#         if num % i ==0:
#             n_list.append(i)
#     return n_lis
#
# print(divider(int(input())))


# # ------------------------------------------------------------------>
# Class 9/26/2021 ClASS, OPP

# class Person():
#     def __init__(self, name , surname):          # __init__ : конструктор с параметрами    # initialize
#         self.name = name
#         self.surname = surname
#         self.age = 25
#         self.high_ed = True
#
#     def print_info(self):                        # наш собственный метод
#         print("Name:", self.name, "Surname:" , self.surname, "age "+ str(self.age))
#
#
# Frank = Person('Frank', 'Cross')     # class instance
# Frank.print_info()
# Frank.age = 55      # установили возраст
# print(Frank.age , Frank.high_ed)
# Frank.print_info()

# # ------------------------------------------------------------------>


# class Car():
#     def __init__(self, model, year, engine, transmission, color, package, price):  # Konstruktor  s parametrami
#         self.model = model
#         self.year = year
#         self.engine = engine
#         self.transmission = transmission
#         self.color = color
#         self.package = package
#         self.price = price
#
#     def Type_of_car(self):
#         print('Model\'s car:', self.model, 'Year:', self.year, 'Engine', self.engine,  )


# # ------------------------------------------------------------------>

# class Person():
#     def __init__ (self, name, surname, date_of_birth, marriage_status, sex, credit_score, years_salary, mortgage, house):
#         self.name = name
#         self.surname = surname
#         self.date_of_birth = date_of_birth
#         self.marriage_status = marriage_status
#         self.sex = sex
#         self.credit_score = credit_score
#         self.years_salary = years_salary
#         self.mortgage = mortgage
#         self.house = house
#
#     def print_client(self):
#         print('Name:', self.name, 'Surname:', self.surname, "date of birth:",self.date_of_birth,
#               'mar_status',self.marriage_status, 'sex:', self.sex, 'Credit Score:', self.credit_score,
#               'years_salary',self.years_salary,
#               'Mortgage:', self.mortgage,
#               'House:',self.house , sep = '\n')
#
#
# Alex = Person('Alex','Cross', 1980, 'Married', 'Male', 850, 120.00, 700,00)
# Nick = Person('Nick', 'Pride', 1999, 'Married', 'Male',780, 85,000, 'rent')
#
# print(Nick.name)
# print(Nick.sex)
#
# Nick.print_client()

# # ------------------------------------------------------------------>

# class Car():
#     """"Created the car class"""
#     def __init__(self, model, year):
#         """Initialization of the model and year"""
#         self.model = model                                 # initialization of out variable / polya klassa
#         self.year = year
#         self.speed_meter = 0
#
#     def the_car_name(self):                                # sozdaem method
#         """Returns the car value"""
#         data_Frame = str(self.year) + '  ' + self.model            # sozdali peremennuyu i peredali 2 polya
#         return data_Frame.capitalize()
#
#     def read_speed_meter(self):
#         """Print the value of speed"""
#         print('Пробег:' + str(self.speed_meter) +'miles')
#
#     def increase_speed_meter(self, miles): # miles - argument
#         """Increase """
#         if miles>0:
#             self.speed_meter += miles # pole v klasse
#         else:
#             print("НЕ СКИДЫВАЙ ПРОБЕГ!")
#
# # Nasliduemos
# class EL_CAR(Car):                                        # sozdaem Pohidnuy class or Docherniy
#     """OUR CONFIG FOR EL CAR"""
#     def __init__(self, model, year, battery ):
#         """Initialization from parental class"""
#         super().__init__(model, year)
#         self.battery = battery
#         self.distance = 100
#
#     def battery_info(self):
#         """Print battery info"""
#         print("We have power "+ str(self.battery) + ' wat')
#
#     """Переопределение родительского метода"""
#     def increase_speed_metr(self):                        # pereopredili z batkivskogo klasu method...
#         print("Increased on " +  str(self.distance))
#
#                                                           #Ekzemplyar klasa
# Tesla = EL_CAR('Y', 2021 , 250)
#
# # main()          # void
# # x = main()      # return something
#
# print(Tesla.the_car_name())
# Tesla.battery_info()
# Tesla.increase_speed_metr()
# Tesla.the_car_name()






# # ------------------------------------------------------------------>
# Homework 9/29/2021 by Classes, OOP, Get(), Setter()
# Egor's Variant!

# class Human():
#     acc_credit_score = 750                     # sozdaem staticheskiy atribut v klase
#
#     def __init__(self, name, surname, age, education, occupation, salary, actual_credit_score):
#         self.name = name                       #polya klasa (initialization)
#         self.surname = surname
#         self.age = age
#         self.education = education
#         self.occupation = occupation
#         self.salary = salary
#         self.actual_credit_score = actual_credit_score
#
#
#     def print_information(self, ):
#         print('Name:', self.name, 'Surname:', self.surname, 'Age:', self.age, 'Education:', self.education,
#               'Occupation:', self.occupation, 'Actual_Credit_Score:', self.actual_credit_score, 'Salary:', self.salary)
#
#
#     def credit_score_of_client(self):
#         if self.actual_credit_score > Human.acc_credit_score:           # мы обратилась к атрибуту класса!!!!
#             print('The credit score of a current client is:', str(self.actual_credit_score), 'points')
#             return True
#         else:
#             print('Credit score is lower than average')
#             return False
#
#     def salary_info(self):
#         if self.salary >= 85000.0:
#             print('Income is acceptable')
#             return True
#         else:
#             print('Income is too low to be required for mortgage')
#             return False
#
#     def mortgage_approval(self):
#         if self.salary_info() == True and self.credit_score_of_client()==True:
#             print('Mortgage is approved')
#         else:
#             print('Mortgage is restricted, based on income and credit score data')
#
    # def mortgage_approval(self, res1, res2):  # Second option variant desicion
    #     if res1 == True and res2 == True:
    #         print('Mortgage is approved')
    #     else:
    #         print('Mortgage is restricted, based on income and credit score data')
#
#
# class Student(Human):
#     def __init__(self, name, surname, age, eduction, occupation, acc_credit_score,
#                 actual_credit_score):
#         super().__init__(name, surname, age, eduction, occupation, acc_credit_score, actual_credit_score)
#         self.actual_credit_score = actual_credit_score
#         # self.mortgage_approval = mortgage_approval
#
# class Employee(Human):
#     def __init__(self, name, surname, age, eduction, occupation, acc_credit_score,
#                 credit_score_of_client, salary, mortgage_approval, actual_credit_score):
#         super().__init__(name, surname, age, eduction, occupation, acc_credit_score, actual_credit_score)
#         self.credit_score_of_client = credit_score_of_client
#         self.salary = salary
#         self.mortgage_approval = mortgage_approval
#
# class Retired_person(Human):
#     def __init__(self, name, surname, age, education, occupation, acc_credit_score,
#                 credit_score_of_client, salary, mortgage_approval, actual_credit_score):
#         super().__init__(name, surname, age, education, occupation, acc_credit_score, actual_credit_score)
#         self.credit_score_of_client = credit_score_of_client
#         self.salary = salary
#         self.mortgage_approval = mortgage_approval
#
#
# Client1 = Student('John', 'McCalkin', 25, 'False', 'False',90000, 760)
# Client1.print_information()
# Client1.mortgage_approval()

# res1 = Client1.salary_info()
# print(res1)
# res2 = Client1.credit_score_of_client()
# print(res2)
# Client1.mortgage_approval(res1, res2)


# # ------------------------------------------------------------------>

# class Cafe:                 # parental classes
#     number_of_clients = 0           # атрибуты
#     check_is_opened = True
#     count_of_meat_supl = 0
#
#     def __init__(self, supply_meat):
#         self.supply_meat = supply_meat      # polya
#         Cafe.count_of_meat_supl +=1
#
#     def check_working_time(self, time):
#         if time > 22 or time < 8:
#             print('Cafe is closed')
#             Cafe.check_is_opened = False
#             return Cafe.check_is_opened
#         else:
#             print('Cafe is opened')
#             return Cafe.check_is_opened
#
#     def Client_hi(self, client):
#         print('Hello client', client)
#         Cafe.number_of_clients += 1
#
#
# Tuesday = Cafe('10 kg')
# print(Tuesday.check_working_time(12))
# print(Tuesday.check_working_time(23))
#
#
# print(Cafe.)
# Tuesday.Client_hi('Nick')


# # ------------------------------------------------------------------>

# class Cafe:                 # parental classes
#     number_of_clients = 0           # атрибуты
#     check_is_opened = True
#     count_of_meat_supl = 0
#
#     def __init__(self, supply_meat):
#         self.supply_meat = supply_meat      # polya klassa / initialization
#         Cafe.count_of_meat_supl += 1
#
#     def check_working_time(self, time):
#         if time > 22 or time < 8:
#             print('Cafe is closed')
#             Cafe.check_is_opened = False
#             return Cafe.check_is_opened
#         else:
#             print('Cafe is opened')
#             return Cafe.check_is_opened
#
#     def client_add(self, client):
#         print("Welcome," + str(client))
#         Cafe.number_of_clients+=1
#
# Tuesday = Cafe('10 kg')
# Tuesday = Cafe(200)
# print("The amount of clients before: ",Cafe.number_of_clients)
# #
# Tuesday.check_working_time(23)
# Tuesday.client_add('Alex, Alisia')
#
# Tuesday.client_add('Vasya')
# Tuesday.client_add('Sasha')
# print("The amount of clients after: ",Cafe.number_of_clients)


# # ------------------------------------------------------------------>
# Class Work 9/30/2021

# class Computer():
#     count = 0
#     check_sold = True
#
#     def __init__(self, weight, battery_capability, ram):
#         self.weight = weight
#         self.battery_capability = battery_capability
#         self.ram = ram
#         self.processor = '2Gb'
#         self.display = 15.6
#         self.memory_row = '1Tb'
#         Computer.count += 1
#
#     # Pereprusvoyem display do value
#     def set_display_size(self, value):
#         if (type(value) == float or type(value) == int) and value > 12.0 and value <= 17.5:
#             self.display = value
#         else:
#             raise ValueError
#
#     def set_memory_raw(self,capability):
#         if 500 <= capability < 1000 and type(capability) == int:
#             self.memory_row = capability.capitalize()
#         else:
#             print('ValueError')
#
#
#     def display_info(self):
#         print('Weight:', self.weight, 'Battery:', self.battery_cappability, 'Ram:', self.ram, 'Processor:', self.processor,
#         'Display:', self.display, 'Memory_raw:', self.memory_row)
#
#     def amount_of_computers(self):
#         # return Computer.count
#         print('Amount of computers are sold:', Computer.count)
#
#     def sold(self):
#         print('Computer is sold:', Computer.check_sold)
#
## Object of Clasiv:
# MacBook = Computer('2lb', '500MB', '16Gb' )
# MacBook.display_info()
# MacBook.amount_of_computers()
# MacBook.sold()
#
# Asus = Computer('5lb', '1000MB', '8GB')
# Asus.display = 17.3
# Asus.memory_row = '500MB'
# Asus.display_info()
# Asus.set_memory_raw()
# Asus.display_info()


# # ------------------------------------------------------------------>
# Getter(), Setters()


class Person:
    def __init__(self, name, surname):
        self.__name = name  # устанавливаем имя
        self.__surname = surname
        self.__age = 1  # устанавливаем возраст

    def display_info(self):
        print("Имя:", self.__name, "\nВозраст:", self.__age)

    """
    Created property and setter for getting / initialization of data which is encapsulated
    """

# ....................>
    @property # getter...
    def name(self):
        return self.__name

    @name.setter # setter....
    def name(self, new_name):
        self.__name = new_name
        print("Your new name is", new_name)

#     # ....................>
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter                             # in or
#     def surname(self, new_surname):
#             self.__surname = new_surname
#             print("The new surname was successfully set:" , new_surname)
#
#     # ....................>
#     """
#     Created property and setter in order to get/set data which is encapsulated
#     """
#     # ....................>
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
# # ....................>
#
# Dariya = Person('Dariya', 'Bilod')
# print("Data before")
# Dariya.display_info()
# print("Darias age:",Dariya.age)
# print(Dariya.name)
# print(Dariya.surname)
# print("Data after:")
#
# Dariya.age = 18
# Dariya.name = 'Alla'
# Dariya.surname = 'Queen'
#
# Dariya.display_info()



# ------------------------------------------------------------------>
# CLass Work 10/1/2021

# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите

# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.
#
# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке

# I have done little different.


# class Alphabet():
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#
#     def print_alph(self):
#         print('Out letters are:', self.letters)
#
#     def letters_num(self):
#         return len(self.letters)
#
# """Created under class Alphabet"""
# class EngAlphabet(Alphabet):
#     Eng_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # Atribut Clasa - Publik
#
#     __letters_num = len(Eng_alphabet)          # private atribut
#
#
#     @staticmethod
#     def chech(ob1):
#         return len(ob1)
#
#     def __init__(self):
#         super().__init__('En', EngAlphabet.Eng_alphabet)
#
#     def is_en_letter(self, letter):
#         if letter in EngAlphabet.Eng_alphabet:
#             letter_index = EngAlphabet.Eng_alphabet.index(letter)
#             print('Your letter is in our list:', letter, 'and index is:', letter_index)
#             return letter_index, letter
#         else:
#             print('Go Fuck yourself tghere is no that letter in a list!!!')
#             return 0
#
#     @property
#     def letters_num(self):
#         return EngAlphabet.letters_num  #
#
#     @letters_num.setter
#     def letters_num(self, new_len):
#         EngAlphabet.__letters_num = new_len
#         print("the value has been changed")
#
#     def example(self):
#         return EngAlphabet.Eng_alphabet[:4]
#
#
# print(EngAlphabet.chech('stroka'))
#
#
#
# language = EngAlphabet()
# print(language.Eng_alphabet)
# print(language.letters_num)
# language.print_alph()# 2nd option - more correct
# print(language.is_en_letter('f'))
# x = language.is_en_letter('F')
# print("The letter:", x)
# print(language.example())
#
#
# a = 'Make Amerika Great Again'
# List_of_Books = Alphabet('Erland', a.split())     # 'asfafasf'.split()
#
# List_of_Books.print()
# print(List_of_Books.letter_num())



# # ------------------------------------------------------------------>



# class Soda():
#     def __init__(self, choose):
#         self.choose = choose
#
#     def show_my_drink(self):
#         if self.choose == True:
#             print('Soda')
#         else:
#             print('Simple drink')
#
#
# choose = False
# drink = Soda(choose)
# drink.show_my_drink()
#
# drink.show_my_drink()


# # ------------------------------------------------------------------>
# # ------------------------------------------------------------------>

# Homework 10/2/2021
"""
1) Сделать 1 класс + 3 классса наследника по 3 статических атрибута + 3 метода
В классе минимум 6 полей (2 из них приват, 4 паблик)
В классах наследниках + 2 поля других , минимум 1 переопределённый метод
Статик метод 1 + Класс метод один
+атрибут value , при создание объекта класса ( в конструкторе) увеличивается его значение
Те поля которые приватные - пишешь гетеры сеттеры
2) Найти видосы по статик и классовым методам
"""















