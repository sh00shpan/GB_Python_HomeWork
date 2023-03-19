# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import randint

n_user = int(input("Введите количество элементов в массиве: "))
x_number_search = int(input("Введите число для поиска: "))

user_list = [randint(1,11) for _ in range(1, n_user+1)]

temp_min_number=0
final_min_number=0

temp_max_number=11
final_max_number=11

for i in user_list:
    if i > temp_min_number and i < x_number_search:
        temp_min_number = i
    if i < temp_max_number and i > x_number_search:
        temp_max_number = i

final_min_number = temp_min_number
final_max_number = temp_max_number    

print(user_list)
print(f"У числа {x_number_search} ближайшие по величине {final_min_number} и {final_max_number}")
