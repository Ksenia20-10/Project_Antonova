try:
    n = float(input ("Введите число : "))
    if n % 2 == 0:
        print(n // 4)
    else:
        print(n * 5)
except ValueError:
    print( 'Неверный ввод. Попробуйте снова')