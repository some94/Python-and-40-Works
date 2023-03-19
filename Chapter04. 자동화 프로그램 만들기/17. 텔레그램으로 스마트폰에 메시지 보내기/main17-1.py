import telegram

token = '6147427824:AAFPVq5MxIjsHeyvJVQ_17FhaulBjh6BXzc'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)