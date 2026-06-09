# Вариант 4. Задание 2.
#2. Составить генератор (yield), который выводит из строки только буквы.

# Генератор, который выводит из строки только буквы
def only_letters(text):
    for char in text:
        if char.isalpha():  # проверяем, является ли символ буквой
            yield char


# Пример использования
test_string = "Hello123! Как дела? Привет42 Мир"
print("Исходная строка:", test_string)

# Собираем результат из генератора
letters_list = list(only_letters(test_string))
print("Только буквы:", "".join(letters_list))

# Или можно вывести по одной букве через цикл
print("Буквы по одной (через генератор):")
for ch in only_letters(test_string):
    print(ch, end=" ")
print()

# Дополнительный пример
print("\nДругой пример:")
string2 = "Python3.13 - лучший! Язык №1"
print("Строка:", string2)
print("Только буквы:", "".join(only_letters(string2)))