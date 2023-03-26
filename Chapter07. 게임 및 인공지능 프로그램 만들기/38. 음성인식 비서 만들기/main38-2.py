import speech_recognition as sr

try:
    while True :
        r = sr.Recognizer()
        # 마이크에서 음성 받기
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.listen(source, offset=1, duration=3)      # 1초후 시작해서 3초간 음성 녹음
        try:
            print("음성변환: " + r.recognize_google(audio, language='ko-KR'))
        except sr.UnknownValueError:
            print("오디오를 이해할수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인: {e}")

except KeyboardInterrupt:
    pass