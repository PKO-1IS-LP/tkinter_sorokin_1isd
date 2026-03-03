from tkinter import *

root = Tk()
root.title("Действие")
root.geometry("360x240")

# Устанавливаем цвет фона окна (белый)
root.configure(bg="#4CAF50")

# Создаем контейнер (фрейм) для кнопок
container = Frame(root)
container.pack(expand=True)  # Центрируем фрейм в окне

# Создаем кнопку
item = "НАЧАТЬ ИГРУ"  # Определяем переменную item для текста кнопки
start = Button(
    container,  # Исправлено: container вместо container
    text=item,
    width=35,
    height=4,
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#4CAF50",
    relief=RAISED,
    bd=6
)
start.pack(pady=9)  # Добавляем отступы между кнопками

root.mainloop()  # Исправлено: mainloop() вместо mainloop()