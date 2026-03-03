import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.title("Результат")
root.geometry("420x260")
root.configure(bg="white")
root.resizable(False, False)  # Запрещаем изменение размера окна

# Центрируем окно на экране
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 420) // 2
y = (screen_height - 260) // 2
root.geometry(f"420x260+{x}+{y}")

# Создаем Canvas для круглого фона
canvas = tk.Canvas(root, width=420, height=260, bg="white", highlightthickness=0)
canvas.pack()

# Создаем большой круглый фон
circle_radius = 80
circle_x = 210  # центр по горизонтали
circle_y = 100  # центр по вертикали

# Рисуем круг
canvas.create_oval(
    circle_x - circle_radius, 
    circle_y - circle_radius,
    circle_x + circle_radius, 
    circle_y + circle_radius,
    fill="#228B22",  # Зеленый цвет
    outline=""
)

# Добавляем текст "ГОТОВО!" на круг
canvas.create_text(
    circle_x, 
    circle_y,
    text="ГОТОВО!",
    font=("Impact", 30),
    fill="white",  # Белый текст на зеленом фоне
    anchor="center"
)

# Добавляем нижний текст
canvas.create_text(
    210,  # центр по горизонтали
    230,  # отступ сверху 20px от круга (примерно)
    text="Ваши данные успешно сохранены!",
    font=("Arial", 18),
    fill="#555555",
    anchor="center"
)

# Альтернативный вариант с использованием Label (если нужны отдельные виджеты)
# Для демонстрации я покажу оба подхода

# Запускаем главный цикл
root.mainloop()