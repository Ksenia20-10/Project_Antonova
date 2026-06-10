# Вариант 4. Задание 1. Регистрационная форма
import tkinter as tk
from tkinter import messagebox

def submit_form():
    """Обработчик кнопки отправки"""
    name = entry_name.get()
    surname = entry_surname.get()
    email = entry_email.get()
    gender = gender_var.get()
    course = course_var.get()

    if not name or not surname or not email:
        messagebox.showwarning("Ошибка", "Заполните все поля!")
        return

    messagebox.showinfo("Регистрация",
                        f"Регистрация успешна!\n\n"
                        f"Имя: {name}\n"
                        f"Фамилия: {surname}\n"
                        f"Email: {email}\n"
                        f"Пол: {gender}\n"
                        f"Курс: {course}")


def clear_form():
    """Очистка всех полей"""
    entry_name.delete(0, tk.END)
    entry_surname.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    gender_var.set("Мужской")
    course_var.set("Python")
    messagebox.showinfo("Очистка", "Все поля очищены")

root = tk.Tk()
root.title("Регистрационная форма")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Регистрация", font=("Arial", 20, "bold"),
                       bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
frame.pack(padx=30, pady=10, fill=tk.BOTH, expand=True)

tk.Label(frame, text="Имя:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=20, pady=15, sticky="w")
entry_name = tk.Entry(frame, font=("Arial", 12), width=25)
entry_name.grid(row=0, column=1, padx=20, pady=15)

tk.Label(frame, text="Фамилия:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=20, pady=15, sticky="w")
entry_surname = tk.Entry(frame, font=("Arial", 12), width=25)
entry_surname.grid(row=1, column=1, padx=20, pady=15)

tk.Label(frame, text="Email:", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=20, pady=15, sticky="w")
entry_email = tk.Entry(frame, font=("Arial", 12), width=25)
entry_email.grid(row=2, column=1, padx=20, pady=15)

tk.Label(frame, text="Пол:", font=("Arial", 12), bg="white").grid(row=3, column=0, padx=20, pady=15, sticky="w")
gender_var = tk.StringVar(value="Мужской")
gender_frame = tk.Frame(frame, bg="white")
gender_frame.grid(row=3, column=1, padx=20, pady=15, sticky="w")
tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="Мужской", bg="white").pack(side=tk.LEFT,
                                                                                                    padx=5)
tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="Женский", bg="white").pack(side=tk.LEFT,
                                                                                                    padx=5)
tk.Label(frame, text="Курс:", font=("Arial", 12), bg="white").grid(row=4, column=0, padx=20, pady=15, sticky="w")
course_var = tk.StringVar(value="Python")
course_menu = tk.OptionMenu(frame, course_var, "Python", "Java", "JavaScript", "C++", "HTML/CSS")
course_menu.config(font=("Arial", 10), width=20)
course_menu.grid(row=4, column=1, padx=20, pady=15)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

btn_submit = tk.Button(button_frame, text="Отправить", command=submit_form,
                       font=("Arial", 12), bg="#4CAF50", fg="white", width=12)
btn_submit.pack(side=tk.LEFT, padx=10)

btn_clear = tk.Button(button_frame, text="Очистить", command=clear_form,
                      font=("Arial", 12), bg="#f44336", fg="white", width=12)
btn_clear.pack(side=tk.LEFT, padx=10)
