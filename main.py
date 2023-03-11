print("Hello World")

age = int(input(""))
print(f"")

month = int(input("Введите порядковый номер месяца - "))
if month == 12 or month == 1 or month == 2:
    print("Этот месяц относиться к Зимнему сезону")
elif month == 3 or month == 4 or month == 5:
    print("Этот месяц относиться к Вессенему сезону")
elif month == 6 or month == 7 or month == 8:
    print("Этот месяц относиться к Летнему сезону")
elif month == 9 or month == 10 or month == 11:
    print("Этот месяц относиться к Осеннему сезону")
else:
    print("Не корректный ввод данных!")

year_of_birth = int(input("Введите Год вашего рождения - "))
age = 2023 - year_of_birth
print(f"Ващ возраст - {age}")

one_number = float(input())
two_number = float(input())
three_number = float(input())
if one_number > 10 and two_number > 10 and three_number > 10:
    print("Успех")
else:
    print("Не успех")

year = float(input("Введите возраст - "))
if year < 18:
    print("Извини, ты еще мал!")
elif 18 <= year <= 24:
    print("Ты молод и красив!")
elif 24 < year <= 40:
    print("У тебя есть шансы на успех!")
else:
    print("Ладно, что там у тебя?")

x = int(input(""))
y = int(input(""))
max_number = 0
if x > y:
    max_number = x
elif x == y:
    max_number = "Числа одинаковые"
else:
    max_number = y
print("Самое большое -", max_number)
