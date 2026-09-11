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

is_auto_active = False

def single_reboot():

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

def auto_reboot():
    global is_auto_active

    if not is_auto_active:
        is_auto_active = True
        btn_auto.config(text="Авто: ВКЛ", bg="#c0392b") # Меняем кнопку авторежима на красную
        label_title.config(text="Автоматический режим запущен", fg="#2ecc71")
        auto_loop_process() # Запускаем цикл автоматических сбросов
    else:
        is_auto_active = False
        btn_auto.config(text="Авто: ВЫКЛ", bg="#95a5a6") # Меняем обратно на серую
        label_title.config(text="Автоматический режим остановлен", fg="#2c3e50")

def auto_loop_process():
    """Сам циклический процесс, который крутится через будильник"""
    if not is_auto_active:
        return 

    
    single_reboot()
    
   
    current_time = datetime.now().strftime("%H:%M:%S")
    label_title.config(text=f"Авто-мониторинг. Последний сброс: {current_time}", fg="#27ae60")
    
        # 5000 = 5 секунд
    window.after(5000, auto_loop_process) 
    
# Создание главного окна программы
window = tk.Tk()
window.title("Modem Resetter+") # Заголовок окна
window.geometry("600x600")     # Базовый размер окна (ширина x высота)

# Добавление текстовой надписи
label_title = tk.Label(
    window, 
    text="Управление модемом готово", 
    font=("Arial", 14, "bold"),
    fg="#2c3e50" # Цвет текста
)
label_title.pack(pady=40) # Надпись разместится сверху, с отступом 40 пикселей вниз

buttons_frame = tk.Frame(window)

buttons_frame.pack(pady=10)


# Добавление интерактивной кнопки
btn_single = tk.Button(
    buttons_frame, 
    text="Перезагрузить сейчас", 
    font=("Arial", 11),
    bg="#2ecc71", # Зеленый цвет кнопки
    fg="white",   # Белый текст
    width=25,
    height=5,
    command=single_reboot
)
btn_single.pack(side=tk.LEFT,padx=10) # Укладываем кнопку сразу под надписью

btn_auto = tk.Button(
    buttons_frame, 
    text="Авто: ВЫКЛ", 
    font=("Arial", 11),
    bg="#95a5a6", # Стартовый серый цвет
    fg="white",   
    width=15,
    height=2,
    command=auto_reboot
)
btn_auto.pack(side=tk.LEFT, padx=10)

# Главный цикл, который не даёт окну закрыться
window.mainloop()