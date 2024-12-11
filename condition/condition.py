first_number = int(input("первое число: "))
second_number = int(input("второе число: "))
third_number = first_number % second_number
if third_number == 0:
    print("кратно")
else:
    print("не кратно")