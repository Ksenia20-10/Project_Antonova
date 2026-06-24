# Вариант 4. Задание 2.
#2. Составить генератор (yield), который выводит из строки только буквы.

def only_letters(text):
    for char in text:
        if char.isalpha():
            yield char

test_string = "Hello123! Как дела? Привет42 Мир"
print("Исходная строка:", test_string)

letters_list = list(only_letters(test_string))
print("Только буквы:", "".join(letters_list))

