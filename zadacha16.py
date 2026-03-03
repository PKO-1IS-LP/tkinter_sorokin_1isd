from tkinter import *

root = Tk()
root.title("Загрузка")
root.geometry("500x200")  # Еще уменьшил высоту
root.configure(bg='white')

# Верхний Label
month_label = Label(
    root,
    text="Март 2026",
    font=("Arial", 22, "bold"),
    fg="#0066CC",
    bg='white'
)
month_label.pack(pady=(10, 20))

# Фрейм-контейнер для ряда квадратов
squares_container = Frame(root, bg='white')
squares_container.pack(pady=(10, 0))

# Дни недели и числа
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
numbers = ["14", "15", "16", "17", "18", "19", "20"]

# Создаем 7 квадратных фреймов 70x90 px
for i in range(7):
    square = Frame(
        squares_container,
        width=70,
        height=90,
        bg='#FFFFFF',
        bd=1,
        relief="solid"
    )
    square.pack(side="left", padx=2)
    square.pack_propagate(False)
    
    # Определяем цвет для субботы и воскресенья (индексы 5 и 6)
    text_color = 'red' if i >= 5 else 'black'
    
    # День недели (верхний Label)
    day_label = Label(
        square,
        text=days[i],
        font=("Arial", 14, "bold"),
        bg='#FFFFFF',
        fg=text_color
    )
    day_label.pack(pady=(5, 0))
    
    # Число дня (нижний Label)
    number_label = Label(
        square,
        text=numbers[i],
        font=("Arial", 28),
        bg='#FFFFFF',
        fg=text_color
    )
    number_label.pack(expand=True)

root.mainloop()