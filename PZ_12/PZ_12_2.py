# 2. Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
# Вариант 4.
matrix2 = [
    [-5, -2, -3],
    [-1, -4, -6],
    [-7, -8, -9]
]

print("Исходная матрица:")
for row in matrix2:
    print(row)

has_positive = any(element > 0 for row in matrix2 for element in row)

print("\nРезультат проверки наличия положительных элементов:")
print(has_positive)