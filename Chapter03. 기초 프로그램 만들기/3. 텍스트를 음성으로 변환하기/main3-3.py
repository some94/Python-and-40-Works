from gtts import gTTS
from playsound import playsound
import os

# 경로를 .py파일의 실행 경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '나의텍스트.txt'
# 파일을 f의 이름으로 오픈. 한글로 작성된 파일이므로 'rt', UTF8형식으로 인코딩
with open(file_path, 'rt', encoding='UTF8') as f:       # with는 파일을 열고 종료되면 자동으로 파일을 닫음
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save("myText.mp3")

playsound("myText.mp3")