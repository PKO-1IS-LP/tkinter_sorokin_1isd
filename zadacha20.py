import tkinter as tk
from tkinter import font

class SimpleForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Данные")
        self.root.geometry("380x320")
        self.root.configure(bg="#ECF0F1")
        self.root.resizable(False, False)
        
        # Центрируем окно
        self.center_window()
        
        # Создаем основной контейнер
        self.create_widgets()
        
    def center_window(self):
        """Центрирование окна на экране"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 380) // 2
        y = (screen_height - 320) // 2
        self.root.geometry(f"380x320+{x}+{y}")
    
    def create_widgets(self):
        """Создание всех элементов формы"""
        
        # Основной фрейм для формы
        form_frame = tk.Frame(self.root, bg="#ECF0F1")
        form_frame.pack(pady=30)
        
        # Поля для ввода
        labels = ["Имя:", "Возраст:", "Город:"]
        self.entries = []
        
        for i, label_text in enumerate(labels):
            # Создаем фрейм для каждой строки
            row_frame = tk.Frame(form_frame, bg="#ECF0F1")
            row_frame.pack(pady=10, fill="x")
            
            # Метка (выравнивание по правому краю)
            label = tk.Label(
                row_frame,
                text=label_text,
                font=("Arial", 14),
                fg="#2C3E50",
                bg="#ECF0F1",
                width=10,  # ширина 100px примерно
                anchor="e"  # выравнивание по правому краю
            )
            label.pack(side="left", padx=(0, 10))
            
            # Поле ввода
            entry = tk.Entry(
                row_frame,
                font=("Arial", 14),
                width=20,
                bg="white",
                relief="solid",
                borderwidth=1
            )
            entry.pack(side="left")
            self.entries.append(entry)
        
        # Фрейм для кнопки
        button_frame = tk.Frame(self.root, bg="#ECF0F1")
        button_frame.pack(pady=20)
        
        # Большая кнопка сохранения
        save_button = tk.Button(
            button_frame,
            text="Сохранить",
            font=("Arial", 18, "bold"),
            bg="#2980B9",
            fg="white",
            width=20,  # примерно 200px
            height=2,  # примерно 50px
            relief="raised",
            borderwidth=2,
            cursor="hand2",
            command=self.save_data
        )
        save_button.pack()
        
        # Добавляем эффект при наведении
        save_button.bind("<Enter>", lambda e: save_button.configure(bg="#3498DB"))
        save_button.bind("<Leave>", lambda e: save_button.configure(bg="#2980B9"))
    
    def save_data(self):
        """Обработка сохранения данных"""
        # Получаем введенные данные
        name = self.entries[0].get()
        age = self.entries[1].get()
        city = self.entries[2].get()
        
        # Здесь можно добавить логику сохранения
        print(f"Сохранено: Имя={name}, Возраст={age}, Город={city}")
        
        # Показываем всплывающее окно (опционально)
        self.show_success_message(name, age, city)
    
    def show_success_message(self, name, age, city):
        """Показ сообщения об успешном сохранении"""
        message = f"Данные сохранены:\nИмя: {name}\nВозраст: {age}\nГород: {city}"
        
        # Создаем всплывающее окно
        popup = tk.Toplevel(self.root)
        popup.title("Успех")
        popup.geometry("250x150")
        popup.configure(bg="white")
        
        # Центрируем всплывающее окно
        popup.transient(self.root)
        popup.grab_set()
        
        # Сообщение
        label = tk.Label(
            popup,
            text=message,
            font=("Arial", 10),
            bg="white",
            justify="left"
        )
        label.pack(pady=20)
        
        # Кнопка OK
        ok_button = tk.Button(
            popup,
            text="OK",
            command=popup.destroy,
            bg="#2980B9",
            fg="white",
            width=10
        )
        ok_button.pack(pady=10)
    
    def run(self):
        """Запуск приложения"""
        self.root.mainloop()

# Создаем и запускаем приложение
if __name__ == "__main__":
    app = SimpleForm()
    app.run()