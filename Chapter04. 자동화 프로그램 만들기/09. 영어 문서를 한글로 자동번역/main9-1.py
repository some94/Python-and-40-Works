import googletrans

translator = googletrans.Translator()

str1 = "행복하세요"
# dest에 번역될 문자 입력. src는 번역할 문자의 언어 설정
result1 = translator.translate(str1, dest='en', src='auto')
print(f"행복하세요 => {result1.text}")

str2 = "I am happy"
result2 = translator.translate(str2, dest='ko', src='en')
print(f"I am happy => {result2.text}")
