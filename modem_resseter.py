import sys
import ctypes
import tkinter as tk

# Проверка на права админа
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.user32.MessageBoxW(0, "Запустите программу от имени Администратора!", "Критическая ошибка", 0x10 | 0x0)
    sys.exit()

# Создание главного окна программы
window = tk.Tk()
window.title("Modem Resetter") # Заголовок окна
window.geometry("600x600")     # Базовый размер окна (ширина x высота)

# Добавление текстовой надписи
label_title = tk.Label(
    window, 
    text="Автоматический перезапуск модема", 
    font=("Arial", 14, "bold"),
    fg="#2c3e50" # Цвет текста
)
label_title.pack(pady=20) # Надпись разместится сверху, с отступом 20 пикселей вниз

# Добавление интерактивной кнопки
btn_start = tk.Button(
    window, 
    text="Запустить мониторинг", 
    font=("Arial", 11),
    bg="#2ecc71", # Зеленый цвет кнопки
    fg="white",   # Белый текст
    width=25,
    height=5
)
btn_start.pack(pady=10) # Укладываем кнопку сразу под надписью

# Главный цикл, который не даёт окну закрыться
window.mainloop()