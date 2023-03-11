import pyautogui
import time
import pyperclip

# 왼쪽 화면의 네이버 검색창 좌표
pyautogui.moveTo(382,301,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

# 날씨 창의 왼쪽 상단 좌표
start_x = 39
start_y = 316
# 날씨 창의 우측 하단 좌표
end_x = 876
end_y = 830

pyautogui.screenshot('서울 날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
