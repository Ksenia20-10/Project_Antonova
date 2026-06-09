# 2. Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
# Вариант 4.
# Исходная матрица (можно взять ту же или новую)
matrix2 = [
    [-5, -2, -3],
    [-1, -4, -6],
    [-7, -8, -9]
]

print("Исходная матрица:")
for row in matrix2:
    print(row)

# Проверяем, есть ли положительные элементы
has_positive = False  # предположим, что нет

for row in matrix2:
    for element in row:
        if element > 0:
            has_positive = True
            break
    if has_positive:
        break

# Выводим результат
print("\nРезультат проверки наличия положительных элементов:")
print(has_positive)  # TRUE или FALSE

# Для наглядности - ещё один пример с положительными числами
print("\n--- Дополнительный пример ---")
matrix3 = [
    [-1, -2, -3],
    [-4, 5, -6],
    [-7, -8, -9]
]

print("Матрица:")
for row in matrix3:
    print(row)

has_positive2 = any(element > 0 for row in matrix3 for element in row)
print("Есть положительные элементы:", has_positive2)