import pyautogui as py
import time
x = input("Informe o que voce deseja falar: ")
py.click(x = 760, y = 1050)
time.sleep(5)
py.click(x = 760, y = 900)
for z in range(10):
    py.write(x)
    py.press("enter")
