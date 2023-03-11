import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter03. 기초 프로그램 만들기\6. 압축파일 암호 푸는 프로그램\암호 123.zip')
for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd=passwd.encode())
            print(f"비밀번호는 {passwd} 입니다.")
            break
        except:
            pass