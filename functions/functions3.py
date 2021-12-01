                     python3 functions.py
------------------------------------------------------------------>
....................Methods an functionsof Lists.................



def list_check(operation, l=list()):  # аргументами
    if operation == 1:
        print("Input the amount of nums:")
        amount = int(input())
        for i in range(amount):
            print("Input", i, "number")
            num = int(input())
            l.append(num)
        return l  # возвращает исполнение функции


    if operation == 2: #метод extend() расширяет один список другим списком.
        new_list = [i for i in range(10)]
        new_list. extend(l)
        return new_list


    if operation == 3:
        print("Input the index and number:", l)
        index = int(input())
        number = int(input())
        print('Number', number, 'filled-in on the possittion', index)
        l.insert(index, number)
        return l

    if operation == 4:
        print('Input first element')
        element = int(input())
        index = l.index(element)
        print("The searched index of the element is", index)
        return index

    if operation ==5:
        print('Input what element you wnat to remove')
        el_remove = int(input())
        l.remove(el_remove)
        print('Element was successfully removed')
        return l

    if operation == 6:
        print('Insert index of element you want to remove')
        pop_index = int(input())
        storage_elem = l.pop(pop_index)
        print('Removed element')
        return storage_elem
        return l

    if operation == 7:
        print('Insert the element you want to count')
        element_numb = int(input())
        x = l.count(element_numb)
        print('Amount of elements')
        return x

    if operation == 8:
        print('Insert returned list')
        l.reverse()
        print('Returned list')
        return l

    if operation == 9:
        print('Return new List')
        new_list = l.copy()
        return new_list

    if operation == 10:
        print('Remove all elem form list')
        l.clear()
        print('Empty list')
        return l

    if operation == 11:
        print('Insert what element to delete')
        del_index = int(input())
        del l[del_index]
        return l

     #    max
    if operation == 12:
        print('Select the maximal value')
        max_element = max(l)
        print('The max number from list:')
        print(l)
        print('max_element:', max_element)

        # min
    if operation == 13:
        print('Select the minimal value')
        min_element = min(l)
        print('The min number from list:')
        print(l)
        print('min_element:', min_element)

        # len
    if operation == 14:
        print('Select the number of elements')
        len_elements = len(l)
        print('The length of the lsit id:', len_elements)
        print(l)
        print('Number of elements in a list:', len_elements)

        # list
    if operation == 15:
        print('Increment input elements from tuple into list')
        num1 = int(input())
        num2 = int(input())
        num3 = int(input())
        num4 = int(input())
        my_tuple = (num1, num2, num3, num4)
        # print(my_tuple)
        list_tuple = list(my_tuple)
        print('Initial data list:', l)
        print('Incremented elements from tuple:', list_tuple)


print("Input the operation")
op = int(input())
l = [2, 5, 215, 51, 2 , 5 , 15, 2]
# [0 1 2 3 4]   # пользуемся списочным выражением для генерации последовательности
print("Main list before:", l)

res = list_check(op, l)
print("The resulted list after using the function:", res)








                     python3 functions.py
------------------------------------------------------------------>
...................TUPLES METHODS AND FUNCTIONS......................


def tuple_check(operation, tuple_numb):

    if operation == 1:
        print('Insert element number:')
        elem_num = input()
        if elem_num in tuple_numb:
            position = tuple_numb.index(elem_num)
            print('Index of the element number:', elem_num)
            print('Number', elem_num, 'has index:', position)
        else:
            print('Element number', elem_num, 'not in tuple')


    if operation == 2:
        print('Count similar element')
        # argument = int(input())
        argument = input()
        if type(argument) == int:
            sim_elem = tuple_numb.count(argument)
            print('Number', argument, 'has', sim_elem, 'similar elements')
        elif type(argument) == str:
            sim_elem = tuple_numb.count(argument)
# Functions
        # len
    if operation== 3:
        print('Count amount of elements in a tuple:')
        len_tuple = len(tuple_numb)
        print(len_tuple)

        # max
    if operation == 4:
        print('Select the maximum value:')
        max_tuple = max(tuple_numb)
        print('The max number:', max_tuple, 'in tuple_numb')
        print(max_tuple)

        # min
    if operation == 5:
        print('Select the the minimum value:')
        min_tuple = min(tuple_numb)
        print('The min number:', min_tuple, 'in tuple_numb')
        print(min_tuple)

        # sum
    if operation == 6:
        print('Calculate the sum of the values:')
        sum_tuple = sum(tuple_numb)
        print('Total amount of elements:',sum_tuple, 'in the' )
        print(sum_tuple)


print('Input the operation')
operation = int(input())
tuple_numb = (5, 6, 7, 8, 9, 5, 10, 11,)
tuple_sting = ('Alex', 'Smith')
# ............

res = tuple_check(operation, tuple_numb)
print('The result after using function:', res)



                     python3 functions.py
------------------------------------------------------------------>
....................Methods an functions of Dictionaries.................

def list_check(operation, data = dict()):  # аргументами
    if operation == 1:

def dictionaries(operation, l = dict()):
    if operation ==1:

data = dict('')

list_check()


print('')
dictionary_list = {'Name': 'Alex', 'Surname': 'Cross', 'Age': 28, 'Occupatiuon':  }
res = dictionary_list(operation, dictionary_list)









     9/13/2021 LESSON F. vc6fdf ,,DUNCTIONS - 3 hours

                     python3 functions.py
------------------------------------------------------------------>

def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*        *')
    print('*' * 10)


draw_box()


                     python3 functions.py
------------------------------------------------------------------>

def triangle():
    for i in range(11):
        print('*' * i)

triangle()
                     python3 functions.py
------------------------------------------------------------------>
def triangle(fill, base):
    for i in range(base):
        print(fill * base)


triangle('?', 8)


                     python3 functions.py
------------------------------------------------------------------>
..........FUNCTION..........

def print_fio(surname, name, middle_name, age, position, sex, car, address, salary):
    print('Surname', name)
    print('Name', name)
    print('Middlename', middle_name)
    print('Age:', age)
    print('Sex', sex)
    print('Car:', car)
    print('Address:', address)
    print('Salary', salary)

    new_list = [surname, name, middle_name, age, sex, car, address, salary]
    print('Created list:', new_list)
    # tuple
    mytuple = tuple(new_list)
    print('Created tuple:', mytuple)

print('Fill in please the surname:')
surname = input()
print('Fill in please name:')
name = input()
print('Fill in please the middle name:')
middle_name = input()
print('Fill in please age:')
age = int(input())
print('Fill in please position:')
position = input()
print('Fill in please sex:')
sex = input()
print('Fill in please a car:')
car = input()
print('Fill in please an address:')
address = input()
print('Fill in please salary:')
salary = int(input())

print_fio(surname, name, middle_name, age, position, sex, car, address, salary)


                     python3 functions.py
------------------------------------------------------------------>

def print_digit_sum(num):
    n = [int(digit) for digit in num]
    print(sum(n))

l = list(input())
print_digit_sum(l)

                     python3 functions.py
------------------------------------------------------------------>


from math import *

def square(a, b):
    return sqrt(a**2 + b**2)

print('Please input a and b:')
a = int(input())
b = int(input())
print(square(a, b))


                     python3 functions.py
------------------------------------------------------------------>

from math import sqrt

def distance(x1, x2, y1, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


print(distance(4, 4, 4, 4))

                     python3 functions.py
------------------------------------------------------------------>


def  compute_average(numbers_list):
    average_numb = sum(numbers_list) / len(numbers_list)
    return average_numb

l = [i for i in range(1, 10)]
print(compute_average(l))

                     python3 functions.py
------------------------------------------------------------------>


def merge(list1, list2):
    result = list1 + list2   # создаем результирующий список
    result.sort()            # сортируем список встроенным методом sort()
    return result            # возвращаем отсортированный список

list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = merge(list1, list2)  # вызываем функцию слияния двух отсортированных списков
print(list3)


                     python3 functions.py
------------------------------------------------------------------>

def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return True
    return False

print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))

                     python3 functions.py
------------------------------------------------------------------>
..............NEW VARIANT




def print_fio(surname, name, middle_name, age, position, sex, car, address, salary):

    new_dict = {'surname': surname, 'name': name, 'middle_name': middle_name, 'position': position, 'sex': sex,
                'car': car, 'address': address, 'salary': salary}
    return new_dict

    # new_list = [surname, name, middle_name, age, sex, car, address, salary]
    # print('Created list:', new_list)
    # # tuple
    # mytuple = tuple(new_list)
    # print('Created tuple:', mytuple)


print('Fill in please the surname:')
surname = input()
print('Fill in please name:')
name = input()
print('Fill in please the middle name:')
middle_name = input()
print('Fill in please age:')
age = int(input())
print('Fill in please position:')
position = input()
print('Fill in please sex:')
sex = input()
print('Fill in please a car:')
car = input()
print('Fill in please an address:')
address = input()
print('Fill in please salary:')
salary = int(input())


dict_info = print_fio(surname, name, middle_name, age, position, sex, car, address, salary)
print(dict_info)


                     python3 functions.py
------------------------------------------------------------------>









