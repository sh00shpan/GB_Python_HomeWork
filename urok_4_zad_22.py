# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint

n_user = int(input("Введите количество элементов в 1 массиве: "))
m_user = int(input("Введите количество элементов в 2 массиве: "))

user_list_n = [randint(1,20) for _ in range(1, n_user+1)]
user_list_m = [randint(1,20) for _ in range(1, m_user+1)]


def dubl_nums_in_lists(array_1, array_2):
    new_list = []
    for element in array_1:
        if element in array_2:
            print(element)
            new_list.append(element)
    print(set(new_list))


print(user_list_n)
print(user_list_m)
dubl_nums_in_lists(user_list_n, user_list_m)