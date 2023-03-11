from gtts import gTTS

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

# 문자열을 한글로 변환하여 tts 변수에 바인딩
tts = gTTS(text=text, lang='ko')
# 현재 폴더에 hi.mp3의 파일 이름으로 저장
tts.save(r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter03. 기초 프로그램 만들기\3. 텍스트를 음성으로 변환하기\hi.mp3")
