#!/usr/bin/env python
# coding: utf-8

# In[10]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL='https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# In[11]:


from selenium.webdriver.common.keys import Keys # 키 입력을 위한 라이브러리
from selenium.webdriver.common.by import By # CSS선택을 위한 라이브러리

elem = driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input ")
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)


# In[15]:


import time
elem = driver.find_element(By.TAG_NAME, "body") # 바디 부분을 찾는다
for i in range(60): # 페이지 다운 키를 60회 누른다.
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

try: # [결과더보기] 버튼이 있다면 누른다.
    driver.find_element(By.CSS_SELECTOR, '#islmp > div > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input').click()

    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# 

# In[17]:


links=[]
images = driver.find_elements(By.CSS_SELECTOR, "#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img") # 이미지의 원소를 모두 찾는다

for image in images:
    if image.get_attribute('src') is not None: # 이미지에서 링크 주소가 있다면 조건이 참. 링크 주소는 src에 저장되어 있음
        links.append(image.get_attribute('src'))

print(' 찾은 이미지 개수:',len(links))


# In[18]:


import urllib.request # 사진을 다운로드 받기 위해 request 라이브러리를 불러온다.

for k,i in enumerate(links): # links의 리스트를 enumerate하여 반복한다. k값은 번호, i값은 links리스트의 원소값이다.
    url = i
    urllib.request.urlretrieve(url, "C:\\Users\\ehdgn\\PycharmProjects\\파이썬과 40개의 작품들\\Chapter05. 크롤링, 이미지처리, 데이터분석 시각화 프로그램 만들기\\19. 구글 이미지 크롤링\\사진다운로드\\"+str(k)+".jpg")

print('다운로드 완료하였습니다.')

