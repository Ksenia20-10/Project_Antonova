try:
    n = float(input ("Введите число : "))
    if 10 <= n <= 99:
        print(n // 4)
    else:
        print(n * 5)
except ValueError:
    print('Неверный ввод. Попробуйте снова')