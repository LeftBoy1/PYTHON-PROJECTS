import pyautogui as gui
import time

message= input("Enter Your Message: ")
number_value = input("Enter the number: ")

time.sleep(2)

for i in range(int(number_value)):
    gui.typewrite(message)
    gui.press('Enter')
