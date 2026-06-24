# Вариант 4. Задание 1
# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
# фразу «Министерства образования Ростовской области», посчитать количество
# произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
# «50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re


with open("hotline.txt", "r", encoding="utf-8") as f:
    text = f.read()

new_text, count = re.subn(r'(Горячая линия)', r'\1 Министерства образования Ростовской области', text)

with open("hotline_modified.txt", "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Добавлений: {count}")

phones_03 = re.findall(r'\d{1,4}-\d{3}-\d{3}-\d{2}-03', text)
phones_50 = re.findall(r'\d{1,4}-\d{3}-\d{3}-\d{2}-50', text)

print(f"Номеров телефонов, заканчивающихся на 03: {len(phones_03)}")
print(f"Номеров телефонов, заканчивающихся на 50: {len(phones_50)}")

print("\nНомера горячих линий, связанных с ЕГЭ/ГИА:")

lines = text.split('\n')
ege_gia_phones = []

for line in lines:
    if 'ЕГЭ' in line or 'ГИА' in line:
        phone = re.search(r'\d{1,4}-\d{3}-\d{3}-\d{2}-\d{2}', line)
        if phone:
            ege_gia_phones.append(phone.group())

if ege_gia_phones:
    for phone in ege_gia_phones:
        print(f"  - {phone}")
else:
    print("  Номера не найдены")

print(f"\nВсего найдено номеров, связанных с ЕГЭ/ГИА: {len(ege_gia_phones)}")