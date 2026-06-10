# Вариант 4. Задание 1
# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
# фразу «Министерства образования Ростовской области», посчитать количество
# произведённых добавлений.

import re

hotline_content = """Горячая линия: 8(800)123-45-67
Телефон доверия: 8(495)123-45-67
Горячая линия ЕГЭ: 8(800)555-03-50
Горячая линия ГИА: 8(800)555-12-03
Справки: 8(812)987-65-43
Горячая линия по вопросам ЕГЭ: 8(800)777-88-50
Горячая линия: 8(800)111-22-33
Консультация: 8(495)999-88-03
Горячая линия ЕГЭ: 8(800)444-55-03
"""

with open("hotline.txt", "w", encoding="UTF-8") as f:
    f.write(hotline_content)

print(" Создан файл hotline.txt ")
print()

with open("hotline.txt", "r", encoding="UTF-8") as f:
    content = f.read()

count_before = len(re.findall(r"Горячая линия", content))
print(f"Количество фраз 'Горячая линия' до добавления: {count_before}")

new_content = re.sub(
    r"(Горячая линия)",
    r"\1 Министерства образования Ростовской области",
    content
)

count_after = len(re.findall(r"Горячая линия Министерства образования Ростовской области", new_content))
print(f"Количество добавлений: {count_after}")

with open("hotline_new.txt", "w", encoding="UTF-8") as f:
    f.write(new_content)

print("Создан файл: hotline_new.txt")
print()
