# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint

number_of_coins = int(input("Введите количество монет: "))

list_1 = [randint(0,1) for _ in range(1, number_of_coins+1) ]
print(list_1)

count_1 = 0
count_0 = 0

for i in list_1:
    if i == 1:
        count_1 += 1
    else:
        count_0 += 1

if count_0 > count_1:
    print(count_0)
else:
    print(count_1)