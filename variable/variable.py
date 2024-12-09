# x = 10
# y = 10
# n = 20
# print(id(x))
# print(id(y))
# id permet de voir id de variable
# a = [1, 2, 3]
# b = a
# b[1] = 'hello'
# print(a,b)
 # тип в пайтон есть изменимое и не изменяемое  если ты меняешь в изменимое
 # valu  в обекте то оно изменится  во всем
# если ты меняешь в  не изменимое то измение будет  тольуо где оно было
# создано
# a =3
# c = a
# w = c
# c = 5
# print(a,c,w)

# тип str
# name = 'hello'
# text = '''
# edson
# the future
# best developper python
# in the world '''
# print(text)

# тип int
# age = 10000
# age_2= 10_000_000 # permet de metre des espaces et
# # que le code soit plus lisible
# print(age,age_2)
# тип float
# pi = 3.14
# print(pi)
# тип complex
# z = 3 + 4j
# print(type(z))
# type permet de savoir le type de la variable
# a = 10
# b = 20
# print(a / b )
# # on aura un arrondi
# print(a // b )
# # on aura un entier
# pour travailler avec math function on import math
# import math
# a = 5
# b = 2
# print(math.sqrt(a))
# print(math.pow(a,b))
# print(math.factorial(5))
# тип bool
# is_true = True
# changer de type
# int(),str(),float(),bool()
# a = "23"
# b = 10
# print (a + str(b))
# function input permet de demander a l utilisateur une information
# age = input("quel age avez vous: ")
# print("mon age ",age,"ans")
# age = input("quel age avez vous")
# print(age)
# age = input("quel age avez vous: ")
# print("l annee  ", 2024 - int(age))
# Домашнее задание:
# I)
# Напишите программу, которая запрашивает число и организовывает следующий вывод:
# Введенное число: X, число меньше на 5: X-5, число большее на 12.5: X+12.5
# II)
# Напишите программу, которая:
# 1)	Запрашивает у пользователя его имя и сохраняет введенное значение в переменную my_name;
# 2)	Запрашивает у пользователя год рождения и сохраняет в переменную year_of_birth;
# 3)	Вычисляет возраст и сохраняет его в переменную с именем age;
# 4)	Выводит на экран тип переменных my_name, year_of_birth, age;
# 5)	Выводит сообщение "Hello my name is: my_name, My age: age".
# III)
# Напишите программу, которая, получает на вход число, обозначающее количество минут,
# которые прошли с начала дня. Необходимо, на основании этого числа, организовать вывод
# в формате ЧЧ:ММ, которое показывает, сколько времени прошло с начала дня в часах и минутах.
# age = input("Введенное число: ")
# print("x",age)
# age_2 = input("число меньше на 5: ")
# print(int(age_2) - 5)
# age_3 = input("число большее на 12.5: ")
# print(int(age_3) + 12.5)
# my_name = input ("Ваше имя: ")
# year_of_birth = input ("Ваш год рождения: ")
# age = 2024 - int(year_of_birth)
# print(type(my_name))
# print(type(year_of_birth))
# print(type(age))
# print("Hello my name is: ",my_name,"\nMy age: ",age,end=".")
minutes_passed = int(input("Введите количество минут: "))
hours = minutes_passed // 60
minutes = minutes_passed % 60
print(f"{hours}:{minutes}")
# print("HH:",hours,"MM:",minutes)
