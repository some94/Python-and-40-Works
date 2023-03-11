import  qrcode

file_path = 'qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    # readlines로 파일을 읽어 줄 별로 리스트 형태로 반환
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)
