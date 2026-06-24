# Вариант 4. Задание 2. Берём задачу из ПЗ №8, Вариант 4:
# "Используя словарь посчитать количество уникальных слов в предложении"
# Добавляем отдельное окно с этой функцией

import tkinter as tk
import math

def calculate():
    try:
        r = float(entry.get())  # получаем радиус
        diam = r * 2             # диаметр
        length = 2 * math.pi * r # длина окружности
        square = math.pi * r ** 2 # площадь

        diam_label.config(text=f"Диаметр: {diam:.2f}")
        length_label.config(text=f"Длина окружности: {length:.2f}")
        square_label.config(text=f"Площадь: {square:.2f}")
    except:
        diam_label.config(text="Ошибка! Введите число")

window = tk.Tk()
window.title("Круг")
window.geometry("300x300")

tk.Label(window, text="Введите радиус:").pack(pady=10)
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Рассчитать", command=calculate).pack(pady=10)

diam_label = tk.Label(window, text="Диаметр: ")
diam_label.pack()

length_label = tk.Label(window, text="Длина окружности: ")
length_label.pack()

square_label = tk.Label(window, text="Площадь: ")
square_label.pack()

window.mainloop()