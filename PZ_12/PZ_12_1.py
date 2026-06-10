#1. В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
# Вариант 4

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Исходная матрица:")
for row in matrix:
    print(row)

size = len(matrix)

for i in range(size):
    for j in range(size):
        if i != j:
            matrix[i][j] *= 2

print("\nМатрица после преобразования:")
for row in matrix:
    print(row)

print()
