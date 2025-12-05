# Задача 2
print("\n" + "=" * 50)
print("ЗАДАЧА 2: Последний локальный максимум")
test_list = [1, 3, 2, 5, 4, 6, 1, 7, 3]
print(f"Тестовый список: {test_list}")
max_index = find_last_local_maximum(test_list)
print(f"Последний локальный максимум на позиции: {max_index}")
if max_index != -1:
    print(f"Значение: {test_list[max_index]}")