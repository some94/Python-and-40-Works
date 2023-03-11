import qrcode

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path = r'C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter03. 기초 프로그램 만들기\4. QR코드 생성기\\' + qr_data + '.png'
qr_img.save(save_path)