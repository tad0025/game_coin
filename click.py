import pyautogui
import time
# Lặp vô hạn để theo dõi tọa độ chuột
while True:
    x, y = pyautogui.position()  # Lấy tọa độ x và y của chuột
    print(f"Tọa độ x: {x}, Tọa độ y: {y}")
    time.sleep(3)
