n = int(input("Введите количество ваших дел - "))
spisok = []
for _ in range(n):
    spisok.append(input("Дело - "))

with open("text.txt", "w", encoding="UTF-8") as var:
    for item in spisok:
        var.write(item + "\n")
