# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

user_number = int(input("Введите число: "))
sum = 0

while (user_number!=0):
    sum += user_number%10
    user_number = user_number//10

print(sum)
