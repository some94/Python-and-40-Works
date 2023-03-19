import numpy as np
import cv2
# 얼굴과 눈을 찾기 위한 OpenCV 알고리즘이 적용된 파일 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# OpenCV에서 한글경로의 파일을 읽지 뫃새 numpy로 파일을 읽어옴
ff = np.fromfile(r'C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter05. 크롤링, 이미지처리, 데이터분석 시각화 프로그램 만들기\23. 사진에 얼굴만 찾아 모자이크 처리(OpenCV)\샘플사진.jpg', np.uint8)
# imdecode로 numpy의 이미지 파일을 OpenCV 이미지로 불러옴
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# 이미지의 크기를 조절
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 이미지에서 얼굴을 찾기 위해 회색조 처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 여러 개의 얼굴을 찾음. 1.2는 감도, 5는 최소 이격 거리를 나타냄. 두 값을 조절하여 감도 조절 가능
faces = face_cascade.detectMultiScale(gray, 1.2,5)
for (x,y,w,h) in faces: # 얼굴을 찾아 파란색으로 네모 표시함
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes: # 눈을 찾아 녹색 네모 표시함
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()