import googletrans

translator = googletrans.Translator()

read_file_path = r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter04. 자동화 프로그램 만들기\9. 영어 문서를 한글로 자동번역\영어파일.txt"

# 파일에서 줄별로 읽어 readlines에 리스트 형태로 바인딩
with open(read_file_path, 'r') as f :
    readLines = f.readlines()

# 리스트 형태로 저장된 readLines에서 한 줄씩 한글로 변환하여 출력
for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
