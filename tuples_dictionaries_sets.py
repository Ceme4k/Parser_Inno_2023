a = [1, 2, 3, 4, 5, 6]
for item in range(len(a) - 1, -1, -1):
    if a[item] % 2 == 0:
        a[item] = a[item] // 2
    else:
        a.pop(item)
print(a)
