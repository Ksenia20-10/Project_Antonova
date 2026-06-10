# Вариант 4. Задание 2
# Сколько номеров телефонов заканчивается на «03», «50».

phones = re.findall(r"8\(\d{3}\)\d{3}-\d{2}-\d{2}", content)

print(f"Всего найдено номеров: {len(phones)}")

phones_ending_03 = [p for p in phones if p.endswith("03")]
print(f"Номера, заканчивающиеся на '03': {len(phones_ending_03)}")
for p in phones_ending_03:
    print(f"  - {p}")

phones_ending_50 = [p for p in phones if p.endswith("50")]
print(f"Номера, заканчивающиеся на '50': {len(phones_ending_50)}")
for p in phones_ending_50:
    print(f"  - {p}")

print()