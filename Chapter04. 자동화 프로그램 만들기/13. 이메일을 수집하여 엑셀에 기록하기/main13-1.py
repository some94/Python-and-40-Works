import re

test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

#정규표현식으로 이메일 형식 추출
results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string)

print(results)