# Вариант 4. Задание 2. Берём задачу из ПЗ №8, Вариант 4:
# "Используя словарь посчитать количество уникальных слов в предложении"
# Добавляем отдельное окно с этой функцией

def open_word_counter():
    """Открывает окно для подсчёта уникальных слов"""

    word_window = tk.Toplevel(root)
    word_window.title("Подсчёт уникальных слов")
    word_window.geometry("500x400")
    word_window.configure(bg="#f0f0f0")

    tk.Label(word_window, text="Подсчёт уникальных слов в предложении",
             font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

    tk.Label(word_window, text="Введите предложение:", font=("Arial", 11), bg="#f0f0f0").pack(pady=5)

    text_input = tk.Text(word_window, height=5, width=55, font=("Arial", 10))
    text_input.pack(pady=5)

    result_text = tk.Text(word_window, height=10, width=55, font=("Arial", 10), state="disabled", bg="#e8e8e8")
    result_text.pack(pady=10)

    def count_words():
        sentence = text_input.get("1.0", tk.END).strip()
        if not sentence:
            messagebox.showwarning("Ошибка", "Введите предложение!")
            return

        import re
        words = re.findall(r'\b\w+\b', sentence.lower())

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert("1.0", f"Всего слов: {len(words)}\n")
        result_text.insert("2.0", f"Уникальных слов: {len(word_count)}\n\n")
        result_text.insert("3.0", "Слова и их количество:\n" + "-" * 30 + "\n")

        for word, count in sorted(word_count.items()):
            result_text.insert(tk.END, f"{word}: {count}\n")

        result_text.config(state="disabled")

    btn_count = tk.Button(word_window, text="Посчитать", command=count_words,
                          font=("Arial", 11), bg="#2196F3", fg="white", width=15)
    btn_count.pack(pady=5)

btn_task2 = tk.Button(root, text="Подсчёт уникальных слов", command=open_word_counter,
                      font=("Arial", 11), bg="#FF9800", fg="white", width=20)
btn_task2.pack(pady=10)

root.mainloop()