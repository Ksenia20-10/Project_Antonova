#1. В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
# Вариант 4

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
print('\n'.join(map(lambda row: str(row), matrix)))

size = len(matrix)
new_matrix = [
    [matrix[i][j] * 2 if i != j else matrix[i][j] for j in range(size)]
    for i in range(size)
]

print("\nМатрица после преобразования:")
print('\n'.join(map(lambda row: str(row), new_matrix)))
