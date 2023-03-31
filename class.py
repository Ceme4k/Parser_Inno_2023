class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Меня зовут {self.name}!\nМне {self.age} лет. "

    def say_hello(self):
        print(f"Привет {self.name}!")


class Pupil(Human):
    def __init__(self, name, age, estimation):
        super().__init__(name, age)
        self.estimation = estimation

    def __str__(self):
        return f"Я - Ученик.\nМеня зовут - {self.name} и мне - {self.age} лет"

    def estimation_pupil(self):
        print(f"Я учусь на '{self.estimation}'")


class Teacher(Pupil):
    def __init__(self, name, age, estimation, work_experience):
        super().__init__(name, age, estimation)
        self.work_experience = work_experience

    def __str__(self):
        return f"Я - Учитель\nМеня зовут - {self.name} и мне {self.age}\n" \
               f"Мои ученики учаться на {self.estimation} и стаж работы у меня {self.work_experience} года"

    def experience_work(self):
        if self.work_experience < 10:
            print("У меня маленький стаж работы! Меньше 10 лет ")
        else:
            print(f"Не переживайте я опытный учитель, мой стаж {self.work_experience} лет")


class Director(Teacher):
    def __init__(self, name, age, estimation, work_experience, salary):
        super().__init__(name, age, estimation, work_experience)
        self.salary = salary

    def __str__(self):
        return f"Я Директор\nМеня зовут {self.name}!\nМне {self.age} лет.\n" \
               f"У моих учителей учаться дети на {self.estimation} и стаж работы у них {self.work_experience} лет\n" \
               f"А моя зарплата - {self.salary} рублей!"

    def salary_director(self):
        print(f"Вы не поверите, но у Директора вот такая зарплата - {self.salary}")


# Экземпляры
vlad = Human("Влад", 15)
print(vlad)
print()
kirill = Pupil("Кирилл", 16, 5)
print(kirill)
print()
rita = Teacher("Рита", 25, 5, 15)
print(rita)
print()
svetlana = Director("Светлана", 45, 5, 25, 75000)
print(svetlana)
print()
