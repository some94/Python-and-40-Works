import telegram

token = "6147427824:AAFPVq5MxIjsHeyvJVQ_17FhaulBjh6BXzc"
id = "777426908"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")