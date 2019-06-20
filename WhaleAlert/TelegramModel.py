import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# print(trades)

# 설치방법
# https://blog.psangwoo.com/coding/2016/12/08/python-telegram-bot-1.html
# 봇만들기
# https://antilibrary.org/2060
# https://steemit.com/kr-dev/@maanya/30

# 
# 826228868
# u.message.chat_id : 65708965

my_token = ''

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 65708965
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)
    
    def receivedMessage(self, update) :
        self.core.sendMessage(chat_id = self.id, text=update.message.text)
        # self.core.message.reply_text("got text")
        # self.core.message.reply_text(update.message.text)
        
    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class BotWhale(TelegramBot):
    def __init__(self):
        self.token = ''
        TelegramBot.__init__(self, '고래', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def add_msg_handler(self, func):
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, func))

    def start(self):
        self.sendMessage('숨쉬는 고래를 찾고 있습니다.')
        self.updater.start_polling()
        self.updater.idle()
