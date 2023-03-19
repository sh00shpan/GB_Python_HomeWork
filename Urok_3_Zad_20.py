# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

list_1_point = ("A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т")
list_2_point = ("D, G, Д, К, Л, М, П, У")
list_3_point = ("B, C, M, P, Б, Г, Ё, Ь, Я")
list_4_point = ("F, H, V, W, Y, Й, Ы")
list_5_point = ("K, Ж, З, Х, Ц, Ч")
list_8_point = ("J, X, Ш, Э, Ю")
list_10_point = ("Q, Z, Ф, Щ, Ъ")

word_to_points = input("Введите слово: ")
word_list = list(str.upper(word_to_points))
#print(word_list)
points_result = 0

for i in word_list:
    for j in list_1_point:
        if i == j:
            points_result+=1
    
    for j in list_2_point:
        if i == j:
            points_result+=2

    for j in list_3_point:
        if i == j:
            points_result+=3

    for j in list_4_point:
        if i == j:
            points_result+=4

    for j in list_5_point:
        if i == j:
            points_result+=5

    for j in list_8_point:
        if i == j:
            points_result+=8

    for j in list_10_point:
        if i == j:
            points_result+=10

print(f"Количество очков {points_result}")