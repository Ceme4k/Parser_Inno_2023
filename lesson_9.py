# Итерируемый объект - объект, который можно поделить
# и "побегать" по нему

# Итератор - объект, "делящий" элемент на части для
# "пробега" по нему


# str_ = 'Привет'

# for item in str_:
#     print(item * 2)

# for item in str_:
#     print(item * 2)

# def test(n):
#     while n > 1:
#         n -= 1
#         yield n

# t = test(10)

# for item in t:
#     print(item)


# a = [x**2 for x in [1, 2, 3]]

# b = (x**2 for x in [1, 2, 3])

# print(next(b))
# print(next(b))
# print(next(b))

# test_gen = (x for x in (range(10)))

# test_gen += 1

# test_list = list(test_gen)


# for i in test_list:
#     print(i)


# str_ = 'Привет'

# iter_str = iter(str_)

# class Rabotyaga:
#     def __init__(self, name, age, work) -> None:
#         self.name = name
#         self.age = age
#         self.work = work

#     def __iter__(self):
#         self.list_attr = [self.name, self.age, self.work]
#         self.index = -1
#         return self

#     def __next__(self):
#         self.index += 1
#         if self.index >= len(self.list_attr):
#             raise StopIteration

#         return self.list_attr[self.index]


# oleg = Rabotyaga('Олег', 43, "Танкист")

# for item in oleg:
#     print(item)


import time

list_ = [1, 1, 2, 3, 4, 3, 2, 6, 5]  # False

list_2 = [1, 2, 3, 4, 5]  # True

start = time.time()


def check_uniq(list_num):
    return len(list_num) == len(set(list_num))


for _ in range(1000000):
    check_uniq(list_)

end = time.time() - start

print('Код выполнен за - ', end)

"--------------------------------------------"

start = time.time()


def check_uniq2(list_num):
    check_item = list_num[0]
    for index in range(len(list_num)):
        for item in range(len(list_num)):
            if item == index:
                continue
            elif check_item == list_num[item]:
                return False
        check_item = list_num[index]
    return True


# for item in range(1000000):
#     check_uniq2(list_)

print(check_uniq2(list_2))

end = time.time() - start

print('Код выполнен за - ', end)
