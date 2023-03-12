import smtplib
from email.mime.text import MIMEText

send_email = "구글 아이디@gmail.com"
send_pwd = "구글앱 비밀번호"

recv_email = "받는 이메일 주소@hanmail.net"

smtp_name = "smtp.gmail.com"
smtp_port = 587

text = """
파이썬으로 구글 메일 전송하기
파이썬과 40개의 작품들
Chapter14. 구글 및 네이버 이메일 보내기 및 대량 이메일 전송
main14-2.py
"""
msg = MIMEText(text)

msg['Subject'] ="파이썬으로 메일 전송"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()