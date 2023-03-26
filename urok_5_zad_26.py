# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

user_number_a = int(input("Введите число A: "))
user_number_b = int(input("Введите число B: "))

def stepen_chisla (chislo, stepen):
    if stepen == 1:
        return chislo
    
    if stepen > 1:
        return (chislo *stepen_chisla(chislo, stepen-1))
    
    
print(stepen_chisla(user_number_a, user_number_b))
