# Вариант 4. Задание 1
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Элементы, умноженные на первый максимальный элемент:

numbers = [-15, 3, 8, -4, 12, 10, -7, 5]

f1 = open("numbers_4.txt", "w", encoding="UTF-8")
f1.write(" ".join(map(str, numbers)))
f1.close()

f1 = open("numbers_4.txt", "r", encoding="UTF-8")
data = f1.read()
f1.close()

num_list = list(map(int, data.split()))

max_first = max(num_list)

min_elem = min(num_list)

multiplied = [x * max_first for x in num_list]

f2 = open("result_4.txt", "w", encoding="UTF-8")
f2.write("Исходные данные: " + " ".join(map(str, num_list)) + "\n")
f2.write("Количество элементов: " + str(len(num_list)) + "\n")
f2.write("Минимальный элемент: " + str(min_elem) + "\n")
f2.write("Элементы, умноженные на первый максимальный элемент (" + str(max_first) + "): " + " ".join(map(str, multiplied)) + "\n")
f2.close()

print("Создан файл: result_4.txt")
print()