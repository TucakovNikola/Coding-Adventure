import pyautogui, time

from pyautogui import sleep
time.sleep(5)

count = 0


for count in range (1):
    time.sleep(5)
    f = open("FU.txt", "r")

    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("Enter")
    count = count + 1
    print(count)


#f = open("VLM.txt", "r")
#if f.mode == "r":
#    contents = f.read()
#   print(contents)Fuck you

