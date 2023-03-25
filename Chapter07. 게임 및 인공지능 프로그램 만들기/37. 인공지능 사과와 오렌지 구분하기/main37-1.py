import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

model_path = r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter07. 게임 및 인공지능 프로그램 만들기\37. 인공지능 사과와 오렌지 구분하기\converted_keras\keras_model.h5"
labels_path = r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter07. 게임 및 인공지능 프로그램 만들기\37. 인공지능 사과와 오렌지 구분하기\converted_keras\labels.txt"
image_path = r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter07. 게임 및 인공지능 프로그램 만들기\37. 인공지능 사과와 오렌지 구분하기\검증용사진\oranges-2533198_1920.jpg"

# teachable machine 기본 코드
model = tensorflow.keras.models.load_model(model_path)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

image = Image.open(image_path)
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array

prediction = model.predict(data)
print(prediction)
# labels.txt 파일에서 결과 이름을 불러오기
with open(labels_path, 'rt', encoding='UTF8') as f : 
    readLines = f.readlines()
# 0번쨰 값일 확률이 크다면 labels.txt 에서 읽은 0번째 값을 출력
if prediction[0,0] > prediction[0,1] :
    print(readLines[0])
else:
    print(readLines[1])