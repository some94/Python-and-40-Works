import imaplib
import email
from email import policy

# 문자열을 인코딩
def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = '아이디'
pw = '비밀번호'
imap.login(id, pw)

# 받은 메일함에서 메일을 읽는다
imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-5:]     # 최신 5개의 메일만 읽는다.

# 최신 메일부터 출력하여 반복(reversed로 최신 메일부터 확인)
for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    print('='*70)
    print('FROM:', email_message['From'])
    print('SENDER:', email_message['Sender'])
    print('TO:', email_message['To'])
    print('DATE:', email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('SUBJECT:', subject)
    print('='*70)

imap.close()
imap.logout()