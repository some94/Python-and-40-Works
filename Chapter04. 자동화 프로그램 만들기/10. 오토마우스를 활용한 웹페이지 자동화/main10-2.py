import pyautogui
import time
import pyperclip

# 네이버 검색창의 좌표로 0.2초 동안 이동(검색창을 왼쪽에 띄웠을 때)
pyautogui.moveTo(382,301,0.2)
# 마우스를 클릭
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

# 엔터키 입력
pyautogui.write(["enter"])
time.sleep(1)