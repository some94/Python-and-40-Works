import googletrans

translator = googletrans.Translator()

read_file_path =r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter04. 자동화 프로그램 만들기\9. 영어 문서를 한글로 자동번역\영어파일.txt"
write_file_path = r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter04. 자동화 프로그램 만들기\9. 영어 문서를 한글로 자동번역\한글파일.txt"

with open(read_file_path, 'r') as f :
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path,'a', encoding='UTF8') as f:       # 'a' 옵션은 마지막에 추가로 쓰는 모드
        f.write(result1.text + '\n')