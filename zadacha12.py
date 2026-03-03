from tkinter import *

root = Tk()
root.title("Три блока")
root.geometry("600x300")
# Устанавливаем цвет фона окна (белый)
root.configure(bg="#FFFFFF")

# СОЗДАЕМ КОНТЕЙНЕР (Frame) ДЛЯ РАЗМЕЩЕНИЯ ТРЕХ ФРЕЙМОВ В РЯД
# Это нужно, чтобы управлять их горизонтальным расположением
container = Frame(root, bg="#FFFFFF")
container.pack(expand=True)  # Центрируем контейнер в окне

frame1 = Frame(container, bg='#FF4040', width=180, height=260)
frame1.pack_propagate(False)  # Запрещаем изменение размера фрейма
label = Label(frame1, text="Красный", bg='#FF4040')
label.place(relx=0.5, rely=0.5, anchor='center')
frame1.pack(side='left', padx=10)

frame2 = Frame(container, bg='#4040FF', width=180, height=260)
frame2.pack_propagate(False)
label = Label(frame2, text="Синий", bg='#4040FF')
label.place(relx=0.5, rely=0.5, anchor='center')
frame2.pack(side='left', padx=10)

frame3 = Frame(container, bg='#40FF40', width=180, height=260)
frame3.pack_propagate(False)
frame3.pack(side='left', padx=10)
label = Label(frame3, text="Зеленый", bg='#40FF40')
label.place(relx=0.5, rely=0.5, anchor='center')
frame2.pack(side='left', padx=10)

root.mainloop()