import speech_recognition as sr

try:
    while True :
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.listen(source)
        try:
            stt = r.recognize_google(audio, language='ko-KR')
            print("음성변환: " + stt)
            if "안녕" in stt:     # 음성인식된 글자 중 "안녕"이 있다면
                print("네 안녕하세요")
            elif "날씨" in stt:   # 음성인식된 글자 중 "날씨"가 있다면
                print("정말 날씨가 좋네요")
            
        except sr.UnknownValueError:
            print("오디오를 이해할수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인: {e}")

except KeyboardInterrupt:
    pass