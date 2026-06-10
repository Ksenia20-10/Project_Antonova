# Вариант 4. Задание 3
# Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

print("=== Задача 3: Номера горячих линий ЕГЭ/ГИА ===")

ege_gia_lines = re.findall(r"Горячая линия.*?(?:ЕГЭ|ГИА).*?(8\(\d{3}\)\d{3}-\d{2}-\d{2})", content)

print(f"Найдено горячих линий по ЕГЭ/ГИА: {len(ege_gia_lines)}")
for phone in ege_gia_lines:
    print(f"  - {phone}")

print()

print(f"1. Добавлений фразы: {count_after}")
print(f"2. Телефонов на '03': {len(phones_ending_03)}")
print(f"3. Телефонов на '50': {len(phones_ending_50)}")
print(f"4. Телефонов по ЕГЭ/ГИА: {len(ege_gia_lines)}")