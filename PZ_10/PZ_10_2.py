# Вариант 4
# 2. Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего
# регистра на нижний.
content = None

try:
    with open('text18-4.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    used_encoding = 'utf-8'
except:
    try:
        with open('text18-4.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        used_encoding = 'utf-8'
    except:
        try:
            with open('text18-4.txt', 'r', encoding='latin-1') as file:
                content = file.read()
            used_encoding = 'latin-1'
        except:
            print("Ошибка: не удалось прочитать файл text18-4.txt")
            exit()

print(f"\nФайл прочитан в кодировке: {used_encoding}")
print("\nСодержимое файла text18-4.txt \n")
print(content)

letters_count = 0
for char in content:
    if char.isalpha():
        letters_count += 1

print(f"\nКоличество букв в файле: {letters_count}")

lowercase_content = content.lower()

with open('text18-4_new.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(lowercase_content)

print("\nСоздан новый файл 'text18-4_new.txt' (все буквы в нижнем регистре)")
print("\n Содержимое нового файла \n")
print(lowercase_content)