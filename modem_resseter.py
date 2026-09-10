import sys
import ctypes
import tkinter as tk
import subprocess
from datetime import datetime
import time

# Проверка на права админа
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.user32.MessageBoxW(0, "Запустите программу от имени Администратора!", "Критическая ошибка", 0x10 | 0x0)
    sys.exit()

DEVICE_ID = r"USB\VID_0BDA&PID_B82C&MI_02\7&9CF2C2F&0&0002"


def start_reboot():

    current_time = datetime.now().strftime("%H:%M:%S")

    label_title.config(text=f"[{current_time}] Перезагружаю модем...", fg="#e67e22")
    
    window.update()

    try:

        subprocess.run(
            ["pnputil", "/restart-device", DEVICE_ID],
            capture_output=True,
            text=True,
            check=True

        )

        label_title.config(text=f"Успешно перезагружен в {current_time}!", fg="#27ae60")
    except:

        label_title.config(text="Ошибка выполнения команды!", fg="#c0392b")

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
    height=5,
    command=start_reboot
)
btn_start.pack(pady=10) # Укладываем кнопку сразу под надписью

# Главный цикл, который не даёт окну закрыться
window.mainloop()