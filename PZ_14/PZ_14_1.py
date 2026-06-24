# Вариант 4. Задание 1. Регистрационная форма
# Форма регистрации пользователя (по образцу)
# Практическое занятие №14

import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    # Собираем данные из формы
    name = name_entry.get()
    password = password_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    hobbies = [hobby for hobby, var in hobby_vars.items() if var.get()]
    country = country_var.get()
    city = city_var.get()
    about = about_text.get("1.0", tk.END).strip()
    example = example_entry.get()

    # Проверка обязательных полей
    if not name or not password:
        messagebox.showwarning("Ошибка", "Заполните имя и пароль!")
        return

    # Сообщение с результатом
    result = f"""Данные сохранены:
Имя: {name}
Возраст: {age}
Пол: {gender}
Увлечения: {', '.join(hobbies) if hobbies else 'нет'}
Страна: {country}
Город: {city}
О себе: {about}
Ответ на пример: {example}"""
    messagebox.showinfo("Успех", result)

def clear_form():
    # Очищаем все поля
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("")
    for var in hobby_vars.values():
        var.set(False)
    country_var.set("")
    city_var.set("")
    about_text.delete("1.0", tk.END)
    example_entry.delete(0, tk.END)

# Создаём окно
window = tk.Tk()
window.title("Форма регистрации пользователя")
window.geometry("500x700")
window.configure(bg="#f0f0f0")

# Заголовок
title = tk.Label(window, text="Форма регистрации пользователя", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# Рамка для формы
frame = tk.Frame(window, bg="white", bd=2, relief=tk.GROOVE)
frame.pack(padx=30, pady=10, fill=tk.BOTH, expand=True)

# === Поля ввода ===

# Ваше имя
tk.Label(frame, text="Ваше имя:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(20, 5))
name_entry = tk.Entry(frame, font=("Arial", 11), width=40)
name_entry.pack(padx=20, pady=(0, 10), fill=tk.X)

# Пароль
tk.Label(frame, text="Пароль:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(5, 5))
password_entry = tk.Entry(frame, font=("Arial", 11), show="*", width=40)
password_entry.pack(padx=20, pady=(0, 10), fill=tk.X)

# Возраст
tk.Label(frame, text="Возраст:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(5, 5))
age_entry = tk.Entry(frame, font=("Arial", 11), width=40)
age_entry.pack(padx=20, pady=(0, 10), fill=tk.X)

# Пол
tk.Label(frame, text="Пол:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(5, 5))
gender_var = tk.StringVar()
gender_frame = tk.Frame(frame, bg="white")
gender_frame.pack(anchor=tk.W, padx=20, pady=(0, 10))
tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="Мужской", bg="white").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="Женский", bg="white").pack(side=tk.LEFT, padx=5)

# Ваши увлечения
tk.Label(frame, text="Ваши увлечения:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(5, 5))
hobby_vars = {
    "Музыка": tk.BooleanVar(),
    "Видео": tk.BooleanVar(),
    "Рисование": tk.BooleanVar()
}
hobby_frame = tk.Frame(frame, bg="white")
hobby_frame.pack(anchor=tk.W, padx=20, pady=(0, 10))
for hobby, var in hobby_vars.items():
    tk.Checkbutton(hobby_frame, text=hobby, variable=var, bg="white").pack(side=tk.LEFT, padx=5)

# Ваша страна
tk.Label(frame, text="Ваша страна:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(5, 5))
country_var = tk.StringVar()
country_combo = ttk.Combobox(frame, textvariable=country_var, values=["Россия", "Беларусь", "Казахстан", "Украина", "Другая"], width=37)
country_combo.pack(padx=20, pady=(0, 10), fill=tk.X)

# Ваш город
tk.Label(frame, text="Ваш город:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(5, 5))
city_var = tk.StringVar()
city_entry = tk.Entry(frame, font=("Arial", 11), width=40)
city_entry.pack(padx=20, pady=(0, 10), fill=tk.X)

# Кратко о себе
tk.Label(frame, text="Кратко о себе:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(5, 5))
about_text = tk.Text(frame, font=("Arial", 11), height=4, width=40)
about_text.pack(padx=20, pady=(0, 10), fill=tk.X)

# Решите пример
tk.Label(frame, text="Решите пример (2 + 2 = ?):", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=(5, 5))
example_entry = tk.Entry(frame, font=("Arial", 11), width=40)
example_entry.pack(padx=20, pady=(0, 10), fill=tk.X)

# Кнопки
button_frame = tk.Frame(frame, bg="white")
button_frame.pack(pady=(10, 20))

cancel_btn = tk.Button(button_frame, text="Отменить ввод", bg="#f44336", fg="white", font=("Arial", 10), command=clear_form)
cancel_btn.pack(side=tk.LEFT, padx=10)

submit_btn = tk.Button(button_frame, text="Данные подтверждаю", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=submit_form)
submit_btn.pack(side=tk.LEFT, padx=10)

# Запуск
window.mainloop()