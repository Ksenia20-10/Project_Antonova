import re

# ТЕСТОВЫЙ ТЕКСТ (содержит все нужные случаи)
text = """
abc123def 456 7890
привет МИР мир Ааа БББввв ГГГ
тест1 а2б в3г д4е
Hello world Привет Мир JavaScript
Арбуз яблоко Озеро утка
123 456 789
Пример * со звездочкой
Текст (со скобками) и еще (одни скобки)
<название>Глава 1</название>
<title>Оглавление</title>
<p>Первая глава</p>
пустая строка ниже


<a href="link">ссылка</a>
"""

print("1. Все натуральные числа (возможно, окружённые буквами)")

pattern1 = r'\d+'
print("Найденные числа:", re.findall(pattern1, text))
print()


print("2. Слова, написанные капсом (строго заглавными)")

pattern2 = r'[А-ЯA-Z]+'
print("Найденные капсы:", re.findall(pattern2, text))
print()


print("3. Слова, в которых есть русская буква, а за ней цифра")

pattern3 = r'\b[а-яА-Я]*[а-яА-Я]\d[а-яА-Я]*\b'
print("Найденные слова:", re.findall(pattern3, text))
print()


print("4. Слова, начинающиеся с русской или латинской большой буквы")

pattern4 = r'\b[А-ЯA-Z][а-яa-zA-Z]*\b'
print("Найденные слова:", re.findall(pattern4, text))
print()


print("5. Слова, которые начинаются на гласную")

vowels_russian = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
vowels_latin = 'aeiouyAEIOUY'
pattern5 = rf'\b[{vowels_russian}{vowels_latin}][а-яa-zA-Z]*\b'
print("Найденные слова:", re.findall(pattern5, text))
print()


print("6. Все натуральные числа, не находящиеся на границе слова")

pattern6 = r'(?<![a-zA-Zа-яА-Я])\d+(?![a-zA-Zа-яА-Я])'
print("Найденные числа:", re.findall(pattern6, text))
print()


print("7. Строчки, в которых есть символ *")

for line in text.split('\n'):
    if '*' in line:
        print("Строка:", line.strip())
print()


print("8. Строчки, в которых есть открывающая и потом закрывающая скобки")

pattern8 = r'\(.*\)'
for line in text.split('\n'):
    if re.search(pattern8, line):
        print("Строка:", line.strip())
print()


print("9. Весь кусок оглавления вместе с тегами")

# Допустим, оглавление — это часть между <название> и последним тегом
pattern9 = r'(<[^>]+>.*?</[^>]+>)'
print("Найденные теги с содержимым:", re.findall(pattern9, text, re.DOTALL))
print()


print("10. Только текстовую часть оглавления, без тегов")

pattern10 = r'<[^>]+>([^<]+)</[^>]+>'
print("Текстовые части:", re.findall(pattern10, text))
print()


print("11. Пустые строки")

empty_lines = [i for i, line in enumerate(text.split('\n'), 1) if line.strip() == '']
print(f"Пустые строки найдены на номерах: {empty_lines}")
print()


print("12. Все теги, не включая их содержимое")

pattern12 = r'<[^>]+>'
print("Найденные теги:", re.findall(pattern12, text))