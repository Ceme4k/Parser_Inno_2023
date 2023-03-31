def check_uniq(list_):
    if len(list_) == len(set(list_)):
        print("Все элементы списка уникальные!")
    else:
        print("Элементы списка не уникальные!")
