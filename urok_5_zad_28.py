# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

user_number_a = int(input("Введите число A: "))
user_number_b = int(input("Введите число B: "))

def sum_rekurs (a, b, z=0):
    if z == a:
        return b
    return sum_rekurs(a, b, z + 1) + 1

print(sum_rekurs(user_number_a, user_number_b))

