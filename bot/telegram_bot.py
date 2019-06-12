import telegram

_token = ''

bot = telegram.Bot(token = _token)

#for i in bot.getUpdates():
#    print(i.message)
bot.sendMessage(chat_id = 875324979, text = "테스트 메시지")
