# python3 egor_10_12.py

def initialization_list():
    print('Insert data into the list')
    a, b, c = int(input()), input(), input()
    return a,b,c

def convert_cort_into_list(kort):
    return list(kort)

def add_element_at_list(x, z):
    print('Please insert the number you want to list:')
    z = int(input())
    x.insert(0, z)
    print(z)

def add_element_at_the_end(x):
    print('Please insert the number you want to add to list:')
    r = int(input())
    x.append(r)
    print(x)

def show_data(x):
    print(*x)

def delete_data(x):
    my_list = x.clear()
    print(my_list)

def amount_list(x):
    numbers_of_elements = len(x)
    return numbers_of_elements

def spisok_na_pustotu(x):
    if len(x) == 0:
        print('List is empty')
    else:
        print(x)

def del_first_elem(x):
    del x[0]
    return x

def last_el(x):
    del x[-1]
    return x

e = initialization_list()
print(e)
x = convert_cort_into_list(e)
print(x)

add_element_at_list(x, 12)























