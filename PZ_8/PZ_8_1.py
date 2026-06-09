# Вариант 4
# Найдите ключ с минимальным значением в sample_dict

sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}

# Исходный словарь
print("Исходный словарь:", sample_dict)

# Находим ключ с минимальным значением
min_key = min(sample_dict, key=sample_dict.get)
print("Ключ с минимальным значением:", min_key)
print()