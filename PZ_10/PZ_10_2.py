# Вариант 4
# 2. Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего
# регистра на нижний.

# Проверяем, существует ли файл text18-4.txt
# Если нет, создаём пример

try:
    f = open("text18-4.txt", "r", encoding="UTF-8")
    f.close()
except FileNotFoundError:
    # Создаём пример файла
    f = open("text18-4.txt", "w", encoding="UTF-8")
    f.write("Привет Мир\n")
    f.write("Как Дела?\n")
    f.write("Это Тестовый Файл\n")
    f.write("Для Проверки\n")
    f.close()
    print("Создан пример файла text18-4.txt")

# Читаем исходный файл
f = open("text18-4.txt", "r", encoding="UTF-8")
lines = f.readlines()
f.close()

print("\n=== Задача 2 ===")
print("Содержимое файла text18-4.txt:")
print("-" * 30)

# Выводим содержимое и считаем буквы
total_letters = 0

for line in lines:
    print(line.rstrip())
    # Считаем только буквы (русские и английские)
    for ch in line:
        if ch.isalpha():
            total_letters += 1

print("-" * 30)
print("Количество букв в файле:", total_letters)

# Создаём новый файл с буквами в нижнем регистре
f_new = open("text18-4_new.txt", "w", encoding="UTF-8")

for line in lines:
    f_new.write(line.lower())

f_new.close()

print("\nСоздан файл: text18-4_new.txt (все буквы в нижнем регистре)")