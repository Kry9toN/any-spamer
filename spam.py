import pyautogui
import time

word = open('bigtext.txt', 'r')
def spam():
    for text in word:
        time.sleep(.1)
        pyautogui.typewrite(text)
        pyautogui.press('enter')

if __name__ == "__main__":
    print('Spam starting in 10 sec')
    print('Now open apps like WA/IG on browser now')
    time.sleep(10)
    print('Spamming....')
    spam()
