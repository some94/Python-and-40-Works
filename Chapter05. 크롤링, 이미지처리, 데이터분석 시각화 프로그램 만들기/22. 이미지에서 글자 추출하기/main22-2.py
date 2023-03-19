import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
languages = pytesseract.get_languages(config='') # 사용 가능한 언어 출력
print(languages)