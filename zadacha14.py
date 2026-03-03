from tkinter import *

# Создаем главное окно
root = Tk()
root.title("Профиль")
root.geometry("400x500")

# Устанавливаем цвет фона окна
root.configure(bg='#F0F4F8')

# Создаем метку с именем
label_name = Label(
    root,
    text="Александр Иванов",
    font=("Georgia", 29, "bold"),
    fg="#1A3C5A",
    bg="#F0F4F8"
)
label_name.pack(pady=30)  # Добавляем отступы через pack

# Создаем метку с ником
label_nickname = Label(
    root,
    text="@sasha_code",
    font=("Courier", 18),
    fg="#666666",
    bg="#F0F4F8"
)
label_nickname.pack(pady=(0, 20))  # Отступ снизу 20px

# Добавляем Frame 300×180 с белым фоном и чёрной рамкой
info_frame = Frame(
    root,
    width=300,
    height=180,
    bg="white",
    bd=2,  # толщина рамки
    relief="solid"  # тип рамки - сплошная линия
)
info_frame.pack()
# Фиксируем размер frame (чтобы не сжимался под содержимое)
info_frame.pack_propagate(False)

# Создаем Label внутри frame (после создания frame)
label = Label(info_frame, 
text="Python Developer", 
bg='#2E8B57',
font=("Arial", 20, "bold")
)
label.place(relx=0.5, rely=0.5, anchor='center')

# Запускаем главный цикл обработки событий
root.mainloop()