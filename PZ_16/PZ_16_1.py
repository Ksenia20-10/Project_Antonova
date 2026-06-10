# Вариант 4. Блок заданий 1. Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
# методы для определения дня недели, проверки на високосный год и определения
# количества дней в месяце.

# Блок 2. Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.

# Блок 1
class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def weekday(self):
        y = self.year
        m = self.month
        d = self.day
        if m < 3:
            m += 12
            y -= 1
        K = y % 100
        J = y // 100
        h = (d + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7
        days = ["Суббота", "Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        return days[h]

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == 2 and self.is_leap_year():
            return 29
        return month_days[self.month - 1]

# Блок 2
class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

if __name__ == "__main__":
    print(" КАЛЕНДАРЬ ")
    c = Calendar(2026, 6, 10)
    print(f"{c.day}.{c.month}.{c.year} -> {c.weekday()}, дней в месяце: {c.days_in_month()}")

    print("\n ЖИВОТНЫЕ ")
    d = Dog("Собака", 4, "Овчарка")
    k = Cat("Кошка", 3, "Сиамская")
    print(f"{d.species}, возраст {d.age}, порода {d.breed}")
    print(f"{k.species}, возраст {k.age}, порода {k.breed}")