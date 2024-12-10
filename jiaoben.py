import pyautogui as pag
import time,pyperclip,os
time.sleep(3)
lst=""
name=""
pwd=os.path.dirname(__file__)
for i in range(105):
    pag.hotkey('alt', 'enter',interval=0.1)
    pag.rightClick(911,369,interval=0.1)
    pag.click(990,417,interval=0.1)
    pag.press('enter',interval=0.1)
    now=pyperclip.paste()
    if now==lst:
        print(f"done {i} items, stuck on {name}")
        exit()
    name=now[9:9+36]
    if int(now.split('\n')[-4][6:])==1:
        pag.hotkey('ctrl', 'shift','s',interval=0.1)
        pag.press('enter',interval=0.5)
    else:
        os.system("copy "+os.path.join(pwd,"Ori",name)+" "+os.path.join(pwd,"temp",name[:-3]+"gif"))
        time.sleep(0.5)
    lst=now
    pag.press('right',interval=0.1)