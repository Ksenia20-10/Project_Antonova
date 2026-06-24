# 1. В последовательности на n целых чисел умножить элементы до n-1 на элемент n.
# Вариант 4. Задание 1
from functools import reduce

A = [3, 5, 2, 8, 1, 4, 6]
print("Исходная последовательность:", A)

n = len(A)

if n >= 1:
    # Функциональный подход: map и lambda
    last_element = A[-1]
    result = list(map(lambda x: x * last_element, A[:-1]))

    print("Последний элемент (n):", last_element)
    print("Результат (элементы до n-1, умноженные на элемент n):", result)
else:
    print("Последовательность пуста")

print()