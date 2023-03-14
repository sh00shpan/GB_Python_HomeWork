# Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

dlina_shock = int(input("Vvedite dlinu: "))
shirina_shock = int(input("Vvedite shirinu: "))
skolko_otlomit = int(input("Skolko otlomit'?: "))

result = False

if dlina_shock == skolko_otlomit or shirina_shock == skolko_otlomit:
    result = True

#if dlina_shock > skolko_otlomit or shirina_shock > skolko_otlomit:
if skolko_otlomit % dlina_shock == 0 or skolko_otlomit % shirina_shock == 0:
    result = True

if result == False:
    print("НЕТ")
else:
    print("ДА")