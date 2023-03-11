# 마우스와 키보드를 자동으로 제어하기 위함
import pyautogui
# 클립보드에 값을 복사 or 붙여넣기 용도, 검색에 필요한 한글을 사용하기 위함
import time

while True:
    print(pyautogui.position())     # 마우스의 좌표 출력
    time.sleep(0.1)