# li = [x for x in range(9)]

# set_ = {x**11 for x in range(9)}

# dict_ = {x: y for x, y in zip([1, 2, 3], [1, 4, 9])}

# dict_ = list(zip([1, 2, 3, 2], [1, 4, 9], ['123', '1', '3', 3, 'e']))

# print(dict_)


# a = frozenset('481223')

# # print(a)

# # a.add('14')

# print(a)

# Задание:
# Программа, которая создаёт словарь пользователя.
# Постоянно Српашивает у пользователя ключ
# Спрашивает у пользователя значение
# Имеет возможность вывода словаря на консоль

# 1
# di = {}

# while input("Введите 0 для просмотра словаря: ")!= "0":
#     key = input("Введите ключ: ")
#     item = input("Введите значение: ")
#     di[key] = item
# print(di)


# 2
# user_dict = {}

# while input("Введите stop для просмотра словаря: ") != "stop":
#     user_value = input("Введите значение: ")
#     user_key = input("Введите ключ: ")

#     user_dict[user_key] = user_value

# print(user_dict)

# Именованные кортежи

from collections import namedtuple

# tuple_ = (1, 2, 3)

# class Car_2:
#     def __init__(self, color, price, coast, black) -> None:
#         self.color = color
#         self.price = price
#         self.coast = coast
#         self.black = black

# с2 = Car_2('Красный', 'Матиз', '2', True)


# Tankist = namedtuple('Tankist', 'name exp beer_cup')


# class Tankist_New():

#     tank = 2
#     computer = 1
#     head = 1

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def to_shot(self):
#         print(f'Стреляю за ФК Балтику!')


# oleg = Tankist_New('Олег', 42)
# alex = Tankist_New('Алекс', 34)
# # print(dir(oleg))
# # print('----------------------------')
# # print(dir(alex))

# oleg.tank = 4
# print('После добавления танка')
# print(oleg.tank)
# print(oleg.__class__.tank)


# print(oleg.tank)
# print(alex.tank)


# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#           'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#           'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#           'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#           'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#           'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}


# email_list = {mail: name_list for mail, name_list in zip(sorted(emails), emails.values())}
