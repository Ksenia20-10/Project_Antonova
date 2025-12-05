# Задача 3
print("\n" + "=" * 50)
print("ЗАДАЧА 3: Перестановка между min и max")
test_list2 = [3, 7, 2, 8, 1, 4, 6, 5]
print(f"Исходный список: {test_list2}")
print(f"Min: {min(test_list2)} на позиции {test_list2.index(min(test_list2))}")
print(f"Max: {max(test_list2)} на позиции {test_list2.index(max(test_list2))}")
result_list = reverse_between_min_max(test_list2.copy())
print(f"Результат: {result_list}")

print("\n" + "=" * 50)
print("Все задачи решены!")