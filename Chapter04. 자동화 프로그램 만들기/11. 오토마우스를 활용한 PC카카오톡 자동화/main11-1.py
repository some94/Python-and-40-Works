import pyautogui
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# pic1.png 파일과 동일한 그림을 찾아 좌표를 출력
picPosition = pyautogui.locateOnScreen('pic1.png')
print(picPosition)

if  picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic2.png')
    print(picPosition)

if  picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic3.png')
    print(picPosition)