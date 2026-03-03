import tkinter as tk
from tkinter import font

class ColorPalette:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Палитра")
        self.root.geometry("500x400")
        self.root.configure(bg="#F5F5F5")
        self.root.resizable(False, False)
        
        # Центрируем окно
        self.center_window()
        
        # Цвета для палитры (4x3)
        self.colors = [
            ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"],
            ["#FFEEAD", "#D4A5A5", "#9B59B6", "#3498DB"],
            ["#E74C3C", "#2ECC71", "#F1C40F", "#34495E"]
        ]
        
        # Создаем основной фрейм для сетки
        main_frame = tk.Frame(self.root, bg="#F5F5F5")
        main_frame.pack(expand=True, padx=50, pady=40)
        
        # Создаем сетку 3x4 (строки x колонки)
        self.create_grid(main_frame)
        
    def center_window(self):
        """Центрирование окна на экране"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 500) // 2
        y = (screen_height - 400) // 2
        self.root.geometry(f"500x400+{x}+{y}")
    
    def is_light_color(self, hex_color):
        """Определяем, светлый ли цвет (для выбора цвета текста)"""
        # Преобразуем HEX в RGB
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Вычисляем яркость по формуле (ITU-R BT.601)
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        
        # Возвращаем True для светлых цветов (яркость > 128)
        return brightness > 128
    
    def get_text_color(self, bg_color):
        """Определяем цвет текста на основе фона"""
        return "black" if self.is_light_color(bg_color) else "white"
    
    def create_grid(self, parent):
        """Создание сетки из цветных фреймов"""
        
        # Размер каждого фрейма
        frame_width = 100
        frame_height = 80
        
        for row in range(3):  # 3 строки
            for col in range(4):  # 4 колонки
                # Получаем цвет для текущей ячейки
                color = self.colors[row][col]
                
                # Создаем фрейм
                frame = tk.Frame(
                    parent,
                    width=frame_width,
                    height=frame_height,
                    bg=color,
                    relief="solid",
                    borderwidth=1
                )
                frame.grid(row=row, column=col, padx=0, pady=0)
                frame.grid_propagate(False)  # Запрещаем изменение размера
                
                # Определяем цвет текста
                text_color = self.get_text_color(color)
                
                # Создаем Label с HEX-кодом
                label = tk.Label(
                    frame,
                    text=color,
                    font=("Arial", 12),
                    bg=color,
                    fg=text_color
                )
                label.place(relx=0.5, rely=0.5, anchor="center")
    
    def run(self):
        """Запуск приложения"""
        self.root.mainloop()

# Создаем и запускаем приложение
if __name__ == "__main__":
    app = ColorPalette()
    app.run()