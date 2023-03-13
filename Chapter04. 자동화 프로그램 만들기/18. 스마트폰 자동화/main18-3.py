from ppadb.client import Client
import time

def adb_connect():
    client = Client(host="127.0.0.1", port=5037)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('No devices')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')

    return device, client

device, client = adb_connect()

device.shell('input keyevent 64')
time.sleep(2.0)
# 주소창으로 이동하여 터치
xyPosition = "423 136"
device.shell(f'input tap {xyPosition}')
time.sleep(2.0)
# url 입력
url = "www.naver.com"
device.shell(f'input text {url}')
time.sleep(2.0)
# 엔터키 입력 명령어
device.shell('input keyevent 66')
time.sleep(2.0)
# 폴더에 캡쳐한 사진 저장
result = device.screencap()
with open(r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter04. 자동화 프로그램 만들기\18. 스마트폰 자동화\screen.png", "wb") as fp:
    fp.write(result)