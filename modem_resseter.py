import subprocess
import time
from datetime import datetime
import ctypes
import sys

# Проверка, запущен ли скрипт с правами Администратора Windows
if not ctypes.windll.shell32.IsUserAnAdmin():
    print("==========================================================")
    print("КРИТИЧЕСКАЯ ОШИБКА: Нет прав Администратора!")
    print("Программа управления модемом требует повышенных привилегий.")
    print("Пожалуйста, перезапусти VS Codium или консоль от Администратора.")
    print("==========================================================")
    input("\nНажми Enter для выхода...")
    sys.exit()

# ID модема из диспетчера устройств (win x - Диспетчер устройство - Сетевые Адаптеры)
DEVICE_ID = r"USB\VID_0BDA&PID_B82C&MI_02\7&9CF2C2F&0&0002"
# Интервал перезапуска в секундах
DELAY_SECONDS = 300

print("=== Скрипт автоматического перезапуска USB-модема запущен ===")

while True:
    current_time = datetime.now().strftime("%H:%M:%S") # Для указания времени на каждую итерацю (перезапуск модема)
    print(f"[{current_time}] Аппаратный перезапуск USB-модема...")
    
    # Запускаем команду pnputil через командную строку Windows
    try:
        result = subprocess.run(
            ["pnputil", "/restart-device", DEVICE_ID], 
            capture_output=True, 
            text=True, 
            check=True
        )
        print(f"[{current_time}] Перезапуск завершен успешно.")
    except subprocess.CalledProcessError as e:     # Вывод ошибки в случае сбоя
        print(f"[{current_time}] Ошибка при перезапуске: {e.stderr}")
    
    print(f"Ожидание {DELAY_SECONDS // 60} минут...\n")
    time.sleep(DELAY_SECONDS) # Таймер 