 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no


user_number = int(input("Введите 6значное число: "))
sum1 = 0
sum2 = 0

if len(str(user_number)) == 6:

    while (user_number>999):
        sum1 += user_number%10
        user_number = user_number//10
    print(sum1)

    while(user_number!=0):
        sum2 += user_number%10
        user_number = user_number//10
    print(sum2)

    if sum1 == sum2:
        print("суммы равны - ДА")
    else:
        print("Суммы не равны - НЕТ")

else:
    print("Введите 6 значное число")