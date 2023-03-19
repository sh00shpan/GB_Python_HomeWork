# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

n_user = int(input("Введите количество элементов в массиве: "))
x_number_search = int(input("Введите число для поиска: "))
user_list = [randint(1,11) for _ in range(1, n_user+1)]
counter=0

for i in user_list:
    if i==x_number_search:
        counter+=1

print(user_list)
print(f"Число {x_number_search} встречается {counter} раз")


