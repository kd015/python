import pyautogui
import time
time.sleep(4)
count = 0
while count <= 501:
    pyautogui.typewrite("Fire!! HMN" + str(count))
    pyautogui.press("enter")
    count = count + 1