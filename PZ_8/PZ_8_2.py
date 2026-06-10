# Вариант 4. Задача 2
# Дан словарь с четным количеством элементов. Найти суммы значений элементов
# первой и второй половин с использованием функции.
a = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print("Исходный словарь:", a)

def sum_of_halves(dictionary):
    items = list(dictionary.values())
    mid = len(items) // 2
    sum_first = sum(items[:mid])
    sum_second = sum(items[mid:])
    return sum_first, sum_second

first_sum, second_sum = sum_of_halves(a)

print("Сумма первой половины:", first_sum)
print("Сумма второй половины:", second_sum)