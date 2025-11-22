word = input("Введи слово, которое хочешь заключить в рамку: ")

horizontal = input("Введи символ для горизонтальных линий: ")
vertical = input("Введи символ для вертикальных линий: ")

if not horizontal or not vertical:
    print("Некорректный ввод. Пожалуйста, укажите символы для рамки")
else:
   line = horizontal * (len(word) + 4)
   print(line)
   print(f"{vertical} {word} {vertical}")
   print(line)
