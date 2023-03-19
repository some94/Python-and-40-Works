import numpy as np
import cv2

ff = np.fromfile(r'C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter05. 크롤링, 이미지처리, 데이터분석 시각화 프로그램 만들기\24. 사진을 그림으로 변환하기(OpenCV)\여행사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

def onChange(pos):
    pass
# 트랙 윈도우 생성
cv2.namedWindow("Trackbar Windows")
# 트랙의 최소 최대값 설정. 트랙이 움직일 때 마다 동작하는 함수 지정
cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onChange)
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onChange)
# 트랙의 기본 위치 지정
cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)

while True:

    if cv2.waitKey(100) == ord('q'):    # OpenCV에서 킷값을 입력받는다. 100mS 동안 기다리다가 값이 없으면 timeout으로 21줄의 코드를 종료하고 다음 코드를 실행한다.
        break   # q의 킷값이 입력되면 break로 while문을 종료한다.

    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0

    print("sigma_s_value:", sigma_s_value)
    print("sigma_r_value:", sigma_r_value)

    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)

    cv2.imshow("Trackbar Windows", cartoon_img)

cv2.destroyAllWindows()
