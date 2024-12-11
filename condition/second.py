# name = input()
# if name :
#     print(name)
# else:
#     print("no name")
# a = True
# b = False
# if a :
#     if b :
#         print(1)
#     else:
#         print(2)
# else:
#     if b:
#         print(3)
#     else:
#         print(4)
# a = int(input())
# if 10 < a < 20 :
#     print(a)
# else:
#     print("no")
# # and умножение multiplication or сложение addition  not отрицание negation
# a = int(input())
# if a == 10 or a == 20 or a == 30:
#     print(10,20,30)
# elif a > 10 and a < 100:
#     print(10,100)
# else:
#     print(a)
# pass permet de ne rien faire
#
# a = int(input())
# if a == 10 or a == 20 or a == 30:
#     print(10,20,30)
# elif a > 10 :
#     pass
# else:
#     print(a)
# a = int(input())
# if a > 10 :
#     number = a
# else:
#     number = 100
# print(number)
# тернарный оператор сокращенная условная конструкция
# a = int(input())
# number = a if a < 10 else  100
# print(number)
# operator match
print ("1 : комедия")
print ("2 : драма")
print ("3 : мультфильм")
genre = int(input("выберите жанр"))
match genre:
    case 1 :
        print("комедия")
    case 2:
        print("драма")
    case 3:
        print("мультфильм")
    case _:
        print("нет такого жанра")
# mais dans match and