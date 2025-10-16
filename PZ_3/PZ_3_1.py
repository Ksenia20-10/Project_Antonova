try:
    a = int(input("Введите число A: \n"))
    b = int(input("Введите число B: \n"))
    if a > 2 and b < 3:
        print("Справедливы неравенства a > 2 and b < 3")
    else:
        print("Несправедливы неравенства a > 2 and b < 3")
except ValueError:
    print('Неверный ввод. Попробуйте снова')