from tkinter import *

root = Tk()
root.title("Загрузка")
root.geometry("500x180")
root.configure(bg='white')  # Устанавливаем белый фон окна

# Создаем центральный фрейм для вертикального выравнивания
center_frame = Frame(root, bg='white')
center_frame.pack(expand=True)  # expand=True позволяет центрировать содержимое

# Большой Label с текстом "Загрузка файлов..."
label = Label(
    center_frame, 
    text="Загрузка файлов...",
    font=("Verdana", 24),
    fg="#333333",
    bg='white'  # Белый фон для соответствия окну
)
label.pack(pady=(0, 10))  # Небольшой отступ снизу

# Основной фрейм-контейнер для полосы загрузки
main_frame = Frame(
    center_frame,
    width=400,
    height=40,
    bg="#E0E0E0",
    bd=1,
    relief="solid"  # Делаем рамку видимой
)
main_frame.pack()
main_frame.pack_propagate(False)  # Запрещаем изменение размера фрейма

# Фрейм прогресса (ярко-голубой)
progress_frame = Frame(
    main_frame,
    width=240,
    height=36,
    bg="#00BFFF"
)
progress_frame.pack(side="left")  # Размещаем слева
progress_frame.pack_propagate(False)  # Запрещаем изменение размера

root.mainloop()