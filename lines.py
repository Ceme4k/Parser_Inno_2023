print("Это приложение, которое выевляет слово является полендромом или нет")
lines = input("Введите слово или число - ").lower()
if lines == lines[::-1]:
    print("Да, это палендромом!")
else:
    print("Нет, это не является палендромом!")


# СТРОКИ И МЕТОДЫ

# Возможности при работе со строками

# 1. Перебор строки
# for item in "Slovo":
#     print(item)

# 2. Объединение строк (Конкатенация)
# "slo" + "vo" = "slovo"

# 3. Нахождение длины строки
# len_str = len("slovo")

# 4. Умножение строки на число
# "slovo" * 3 = "slovoslovoslovo"

# 5. Проверка вхождения в строку
# if "sl" in "slovo":
#     print('Слово содержит sl')

# Индексация
# s = "slovo and tlwew"
# s1 = s[9]
# print(s1) #v

# s = "slovo and tlew"
# s1 = s[-2]
# print(s1) #e

# s = "slovo"
#
# print(s[1] * 3 + s[-2] * 2)
# lll + vv = lllvv

# Cрезы

# s = "slovj"
# [начало:конец:шаг]
# print(s[2:4]) # ov
# print(s[:4]) # slov
# print(s[2:]) # ovj
# print(s[::2]) # soj
# print(s[::-1]) # jvols

# f-строки
# name = 'Andrey'
# print(f"Привет, {name}")

# Методы
# объект.метод(аргументы)

# Методы конвертации регистра строк

# Большие буквы - верхний регистр
# Маленькие буквы - нижний регистр

# .lower() - Переводит в нижний регистр

# user_str = input('Введите слово').lower()
# print(user_str)

# .upper() - Переводит в верхний регистр

# .swapcase() - Смена регистра

# print("GbEkIgT".swapcase())

# .title - Начинает каждое слово с большой буквы
# print('hello world'.title())

# .capitalize() - Первую букву делает заглавной
# user_str = 'приTWEGет'
# print(user_str.capitalize())


# Методы замены и поиска в строке

# .count() - Считает кол-во символов
# print('Привет'.count('п'))

# .startswith() - Проверка начала строки
# print("Привет".startswith('Ок'))

# .endswith() - Проверка конца строки
# print("Привет".endswith('ивет'))

# .find() - Поиск символа в слове
# print('Heeello'.find('Pe')) # -1
# print('Heeello'.find('e')) # 1

# .index() - Поиск символа в слове
# print('Heeello'.index('Pe'))

# .strip() - Обрезание пробелов
# print('  Heeello  '.strip())

# .lstrip() - Обрезание пробелов слева
# print('  Heeello  '.lstrip())

# .rstrip() - Обрезание пробелов справа
# print('  Heeello  уцйкцйвыф'.rstrip())

# .replace('Что меняем', "На что меняем")
# print('Heeello  уцй'.replace('уцй', 'Красотища'))

# Листы []

# list_user = ["refrg", "refrg", 124, True]
# list_user2 = list(range(12))
# print(list_user2)

# print(list_user[2])

# Списковые включения
# элемент = [выражение for элемент in последовательность]

# sqar_list = []

# for item in [1, 2, 3]:
#     sqar_list.append(item**2)

# sqar_list = [x**2 for x in [1, 2, 3]]
# print(sqar_list)


# Методы

# .append() - Добавляет элемент в лист

# .remove() - Удаляет элемент по значению
# list_old = [1, '3', '1']
# list_old.remove(1)
# print(list_old)

# .pop() - Удаляет элемент по индексу
# list_old = ['Ghbdtn', '124', '143']
# list_old.pop(1)
# list_old.pop(1)
# print(list_old)
