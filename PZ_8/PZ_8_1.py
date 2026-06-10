# Вариант 4
# Найдите ключ с минимальным значением в sample_dict

a = {'Physics': 82, 'Math': 65, 'history': 75}
print("Исходный словарь:", a)
min_key = min(a, key=a.get)
print("Ключ с минимальным значением:", min_key)
print()