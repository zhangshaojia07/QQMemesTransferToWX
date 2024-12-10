import pyautogui as pag
import time
time.sleep(5)
for i in range(97):
    pag.hotkey('ctrl','c')
    pag.click(1469,984)
    pag.hotkey('ctrl','v')
    pag.press('enter')
    time.sleep(2)
    pag.rightClick(1809,833)
    pag.click(1809,833)
    pag.click(536,30)
    pag.press('down')