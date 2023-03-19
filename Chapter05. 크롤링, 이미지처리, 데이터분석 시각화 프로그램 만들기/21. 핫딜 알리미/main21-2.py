from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import telegram
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

send_message_list = []  # 보낸 메시지를 기록하는 리스트

while True:
    try:
        driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
        driver.implicitly_wait(time_to_wait=10)
        titles = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
        urls = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')

        message = ""
        for i in range(len(titles)):
            if "김치" in titles[i].text:
                message = titles[i].text + "\n" + urls[i].get_attribute('href')
                if message not in send_message_list: # 이미 보낸 메시지와 동일한 메시지는 전송하지 않음
                    print(message)
                    send_message_list.append(message)
                    token = "" # 텔레그램 봇 토큰
                    id = "" # 텔레그램 봇 ID
                    bot = telegram.Bot(token)
                    bot.sendMessage(chat_id=id, text=message)

        time.sleep(60.0 * 5) # 5분에 한 번씩만 실행

    except KeyboardInterrupt:
        break