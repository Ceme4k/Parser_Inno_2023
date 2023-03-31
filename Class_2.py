class Math:
    def __init__(self, number):
        self.number = number

    def __add__(self, other_number):
        print("Происходит сложение:")
        return self.number + other_number

    def __sub__(self, other_number):
        print("Происходит вычитание:")
        return self.number - other_number

    def __mul__(self, other_number):
        print("Происходит умножение:")
        return self.number * other_number

    def __truediv__(self, other_number):
        print("Происходит деление:")
        return self.number / other_number

    def __floordiv__(self, other_number):
        print("Происходит целочисленное деление:")
        return self.number // other_number

    def __mod__(self, other_number):
        print("Происходит вычесление остатока от деления:")
        return self.number % other_number

number = Math(float(input("Введите число - ")))
other_number = float(input("Введите число "))
print(number + other_number)
print(number - other_number)
print(number / other_number)
print(number // other_number)
print(number * other_number)
print(number % other_number)