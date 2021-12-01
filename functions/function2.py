# 9/1/2021
#                       python3 function2.py
# ------------------------------------------------------------------>
# FUNCTION
#
# def covert_to_miles(distance):
#     x = distance * 0.6214
#     print('The miles distance is:')
#     return x
#
#
# print('Please fill in distance in km')
# distance = int(input())
# print(covert_to_miles(distance))
#
#                       python3 function2.py
# ------------------------------------------------------------------>
# FUNCTION

# def covert_to_miles_gallons(cort):
#     new_list = list(cort)
#     new_list[0] = new_list[0]/3.8
#     new_list[1] = new_list[1]*0.6214
#     print("Gallons:---------------------Miles:")
#     return new_list
#
#
# def get_distance_liters():
#     print('Please fill in distance in km and liters')
#     distance, liters = int(input()), int(input())                       # local vars
#     return liters,distance
#
#
# litters_distance = get_distance_liters()                    # присваеваем переменной кортеж, который получили с функции
# miles_gallons = covert_to_miles_gallons(litters_distance)       # присваеваем переменной
# print(miles_gallons)



# print(covert_to_miles_gallons(get_distance_liters()))           # в convert_to_miles передаём результат get_distance_litters и печатаем


#                       python3 function2.py
# ------------------------------------------------------------------>

# def find_all_symbol(target, symbol):
#     new_list = []
#
#     for i in range(len(target)):
#         if symbol == target[i]:
#             new_list.append(i)
#     return new_list
#
#
# stroka = 'Make America Great Again!'
# print(find_all_symbol(stroka, 'a'))

# print(covert_to_miles_gallons(get_distance_liters()))

#                       python3 function2.py
# ------------------------------------------------------------------>


# def marge(list1, list2):
#     result = list1 + list2
#     res_sort = result.sort()
#     result.sort()
#     return result
#
# list1 = [i**2 for i in range(5) if i % 2 != 0]
# list2 = [i**3 for i in range(15) if i % 2 == 0]
#
# l1 =  [15,1515,124,515,16,711,153]
# l1.sort()
# l2 =  [11,151515,66,73,7,99,11,1]
# l2.sort()
#
# print(marge(l1, l2))


#                       python3 function2.py
# ------------------------------------------------------------------>

# Write the program which takes two lists and create from dictionaries from
# them. First list is a key, and second are values.
#  Note use method zip

# l1: 'parameters': 'bank provider', cvc code', 'one_provider', 'expiration_date'
# 'status', 'country of origin', 'debt', 'loan', 'name, 'surname'

# l2: any values

# function 1 - initialize first list
# function 2 - initialize the second list
# function3 - zips them
# function4 -

#                       python3 function2.py
# ------------------------------------------------------------------>

# def initialize_keys():
#     print('Please input bank provider information:')
#     bank_provider = input()
#     cvc_code = int(input())
#     one_provider = input()
#     experation_date = int(input())
#     status = input()
#     country_of_orgin = input()
#     type_of_card = input()
#     loan = int(input())
#     name = input()
#     surname = input()
#
#     list1 = list()
#     list1.append(bank_provider)
#     list1.append(cvc_code)
#     list1.append(one_provider)
#     list1.append(experation_date)
#     list1.append(status)
#     list1.append(country_of_orgin)
#     list1.append(type_of_card)
#     list1.append(loan)
#     list1.append(name)
#     list1.append(surname)
#     list1.append(status)
#
#
# def initialize_values():
#     print('Please provide values:')


# print('Please input bank provider:')
# parameters: ['bank provider', cvc code', 'one_provider', 'expiration_date'
# 'status', 'country of origin', 'debt', 'loan', 'name, 'surname']
#                       python3 function2.py
# ------------------------------------------------------------------>
#
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# if 'Франция' in capitals:
#     print('Столица Франции - это', capitals['Франция'])
#
# print('Россия'['Москва'])
# key['Россия']['Москва']
#
#
#                           FUNCTION  9/16/2021
#
#                     python3 function2.py
# ------------------------------------------------------------------>
#
# def square(x, pow = 2):
#     return x**pow
#
# print(square(9))
# print(square(9, pow=3))

#                     python3 function2.py
# ------------------------------------------------------------------>