# импортируем модуль tkinter
from tkinter import *

# создаем главное окно
root = Tk()
# создаем заголовок для окна
root.title("Заголовок приложения")
root.iconbitmap(default="")
# создаем размеры для окна
root.geometry("500x200")

# Устанавливаем цвет фона окна (светло-желтый)
root.configure(bg='#FFFACD')
# создаем лейбл для вывода текстового сообщения
# Создаем метку с текстом "HELLO WORLD!"
# Параметры:
#   text = "HELLO WORLD!" - сам текст
#   font = ("Impact", 48, "bold") - шрифт Impact, размер 48, жирный
#   fg = "#800080" - цвет текста фиолетовый
#   bg = "#FFFACD" - фон метки такой же, как у окна (чтобы не было пятна)
label = Label(
    root,
    text="HELLO WORLD!",
    font=("Impact", 48, "bold"),
    fg="#800080",
    bg="#FFFACD"
)
label.pack(expand=True) # Размещаем метку по центру окна
label2 = Label(
    root,
    text="Это мой первый яркий текст",
    font=("Comic Sans MS", 24, "bold"),
    fg="#C71585",  # Medium Violet Red
    bg="#FFFACD"
)
# размещаем лейбл с помощью метода pack
label2.pack() # Размещаем метку по центру окна

# вызов главного окна с помощью метода mainloop
root.mainloop()