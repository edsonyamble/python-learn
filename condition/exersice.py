# Домашнее задание:
# I)
# Напишите программу, которая определяет наибольшее и наименьшее из двух чисел, введенных пользователем.
# II)
# Напишите программу, которая проверяет является ли введенное пользователем число четным.
# III)
# Напишите программу, которая, получает на вход 2 числа (большее и меньшее). Определить, кратно ли первое число второму. Вывести на экран сообщение об этом, а также остаток от деления, если первое число не кратно второму.
#
# x = int(input("number 1: "))
# y = int(input("number 2: "))
# print(x,y)
# if x > y :
#     print("x больше y")
# else:
#     print("x меньше y")
# x = int(input("number : "))
# if x % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")
#
# x = int(input("number 1: "))
# y = int(input("number 2: "))
# z = x % y
# if z == 0:
#     print("x кратно y")
# else:
#     print("x не кратно y")
# print("остаток",z)
# Домашнее задание:
# I)
# Напишите программу, которая, получает на вход три числа. Выведите сумму наибольшего и наименьшего из трёх чисел.
# II)
# Напишите программу, определяющую является ли введённый пользователем год високосным.
# III)
# Напишите программу, которая запрашивает у пользователя месяц его рождения в формате от 1 до 12.
# Необходимо определить и вывести время года.
# Формат вывода (пользователь должен увидеть):
# Вы родились осенью
# или
# Вы родились летом
# или
# Вы родились зимой
# или
# Вы родились весной
# Для решения задания используйте конструкцию match/case.
# a = int(input("number 1: "))
# b = int(input("number 2: "))
# c = int(input("number 3: "))
# d = max(a,b,c)
# e = min(a,b,c)
# print(d,e)
# year = int(input("year: "))
# if year % 4 == 0 and year % 100 != 0 :
#     print("високосный")
# else:
#     print("не високосный")
# month = int(input("month: "))
# match month:
#     case 1 | 2 | 12:
#         print("вы родились зимой")
#     case 3 | 4 | 5:
#         print("вы родились летом")
#     case 6 | 7 | 8:
#         print("вы родились осенью")
#     case 9 | 10 | 11:
#         print("вы родились весной")
#         print("нет такого месяца")
