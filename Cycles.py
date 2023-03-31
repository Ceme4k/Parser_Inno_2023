question = int(input("Введите число - "))
sum = 1
count = 1
while count != question:
    count += 1
    sum *= count
print(f"Факториал {question} или 5! = {sum}")
