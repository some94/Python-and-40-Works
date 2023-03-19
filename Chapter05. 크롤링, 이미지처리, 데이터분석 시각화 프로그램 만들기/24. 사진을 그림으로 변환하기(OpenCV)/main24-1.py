import numpy as np
import cv2

ff = np.fromfile(r'C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter05. 크롤링, 이미지처리, 데이터분석 시각화 프로그램 만들기\24. 사진을 그림으로 변환하기(OpenCV)\여행사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# sigma_s 값과 sigma_r 값을 조절하여 이미지를 그림화한다.
cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)

cv2.imshow('cartoon view', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()