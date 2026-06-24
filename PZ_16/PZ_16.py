# Вариант 4. Блок заданий
# 1. Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
# методы для определения дня недели, проверки на високосный год и определения
# количества дней в месяце.

# 2. Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.

# Блок 1. Класс Календарь
class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def weekday(self):
        """Определение дня недели"""
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
        """Проверка на високосный год"""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self):
        """Определение количества дней в месяце"""
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == 2 and self.is_leap_year():
            return 29
        return month_days[self.month - 1]


# Блок 2. Классы Животное, Собака, Кошка
class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def info(self):
        print(f"Вид: {self.species}, Возраст: {self.age}")


class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

    def info(self):
        print(f"Вид: {self.species}, Возраст: {self.age}, Порода: {self.breed}")


class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

    def info(self):
        print(f"Вид: {self.species}, Возраст: {self.age}, Порода: {self.breed}")


# Проверка работы классов
if __name__ == "__main__":
    print("=" * 50)
    print("РАБОТА С КЛАССОМ КАЛЕНДАРЬ")
    print("=" * 50)

    c = Calendar(2026, 6, 24)
    print(f"Дата: {c.day}.{c.month}.{c.year}")
    print(f"День недели: {c.weekday()}")
    print(f"Високосный год: {c.is_leap_year()}")
    print(f"Дней в месяце: {c.days_in_month()}")

    print("\n" + "=" * 50)
    print("РАБОТА С КЛАССАМИ ЖИВОТНЫХ")
    print("=" * 50)

    dog = Dog("Собака", 5, "Немецкая овчарка")
    cat = Cat("Кошка", 3, "Британская")

    dog.info()
    cat.info()