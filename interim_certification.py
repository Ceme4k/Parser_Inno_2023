a, b = int(input("Введите число а: ")), int(input("Введите число b: "))
sum_, count = 0, 0
for item in range(a, b + 1):
    if item % 3 == 0:
        sum_ += item
        count += 1
print(sum_ / count)
