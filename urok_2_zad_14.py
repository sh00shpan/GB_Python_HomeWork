# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number_n = int(input("Введите число: ")) 
stepen = 1
while stepen <= number_n:
   print(stepen)
   stepen = 2*stepen
   
