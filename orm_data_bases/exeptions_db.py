# python3 exeptions_db.py

#                               exeptions_db.py
# ------------------------------------------------------------------>
"""
Ошибки (номера строк через пробел): !!!
"""


def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
except ArithmeticError:
    print('Was occured arithmetic Error in line 27')

print("Среднее геометрическое = {:.2f}".format(c))
