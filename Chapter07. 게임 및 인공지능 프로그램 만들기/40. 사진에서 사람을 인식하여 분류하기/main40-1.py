from glob import glob

img_path = r'C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter07. 게임 및 인공지능 프로그램 만들기\40. 사진에서 사람을 인식하여 분류하기\원본이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

print(img_list)