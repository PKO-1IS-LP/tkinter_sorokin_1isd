from tkinter import *
root = Tk()
root.title("Меню")
root.geometry("280x420")

# Устанавливаем цвет фона окна (светло-желтый)
root.configure(bg='#2F2F2F')

# Создаем контейнер для вертикального размещения кнопок
container = Frame(root, bg="#FFFFFF")
container.pack(expand=True)

# Создаем 5 кнопок и размещаем их вертикально
# Список названий кнопок
menu_items = ["Главная", "Профиль", "Друзья", "Сообщения", "Настройки"]

for item in menu_items:
    button = Button(
        container,
        text=item,
        width=22,
        height=2,
        font=("Arial", 16, "bold"),
        bg="#E0E0E0",
        relief=RAISED
    )
    button.pack(pady=9)  # Добавляем отступы между кнопками

root. mainloop()