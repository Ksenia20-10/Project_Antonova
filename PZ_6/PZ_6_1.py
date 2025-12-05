# Задача 1
print("=" * 50)
print("ЗАДАЧА 1: Геометрическая прогрессия")
A, D = 2, 3
progression = geometric_progression(A, D)
print(f"Первый член: {A}, знаменатель: {D}")
print(f"Прогрессия: {progression}")
print(f"Проверка: 10-й член = {A}*{D}^9 = {A * (D**9)}")