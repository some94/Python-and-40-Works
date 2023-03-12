import pyautogui
import pyperclip
import time
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('pic1.png')
print(picPosition)

if  picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic2.png')
    print(picPosition)

if  picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic3.png')
    print(picPosition)

# 이미지에서 찾은 좌표의 중간 좌표값을 찾는다
clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)    # 더블 클릭

pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다~~")
pyautogui.hotkey("ctrl", "v")
time.sleep(1.0)

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)