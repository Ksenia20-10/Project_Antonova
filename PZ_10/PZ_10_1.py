# Вариант 4. Задание 1
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Элементы, умноженные на первый максимальный элемент:

import random

numbers = [random.randint(-50, 50) for _ in range(20)]

with open('data_1.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(map(str, numbers)))


with open('data_1.txt', 'r', encoding='utf-8') as f:
    numbers_str = f.read()
    numbers_list = list(map(int, numbers_str.split()))

count = len(numbers_list)
min_element = min(numbers_list)

first_max = max(numbers_list)
first_max_index = numbers_list.index(first_max)

multiplied_elements = [x * first_max for x in numbers_list]

with open('data_1_result.txt', 'w', encoding='utf-8') as f:
    f.write("Исходные данные:\n")
    f.write(' '.join(map(str, numbers_list)) + "\n\n")
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Минимальный элемент: {min_element}\n")
    f.write(f"Первый максимальный элемент: {first_max}\n")
    f.write(f"Элементы, умноженные на первый максимальный элемент:\n")
    f.write(' '.join(map(str, multiplied_elements)) + "\n")

print(f"\nРезультаты сохранены в файл 'data_1_result.txt'")
print(f"Количество элементов: {count}")
print(f"Минимальный элемент: {min_element}")
print(f"Первый максимальный элемент: {first_max}")
print(f"Элементы, умноженные на {first_max}: {multiplied_elements[:5]}...")  # показываем первые 5