import threading
import time

# 1초마다 "쓰레드1 동작"을 출력하는 함수
def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

# 쓰레드 설정
t1 = threading.Thread(target=thread_1)
# 쓰레드를 데몬쓰레드로 설정하여 메인 동작이 실행될 때만 쓰레드를 실행하도록 한다.
t1.daemon = True
t1.start()

# 메인 코드로 "메인 동작"을 2초마다 출력
while True:
    print("메인 동작")
    time.sleep(2.0)