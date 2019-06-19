import telegram
from telegram.ext import Updater, CommandHandler

# 텔레그램 알림
print('텔레그램 알림')
# print(trades)

# 설치방법
# https://blog.psangwoo.com/coding/2016/12/08/python-telegram-bot-1.html
# 봇만들기
# https://antilibrary.org/2060
# https://steemit.com/kr-dev/@maanya/30

# 826228868:AAF-MKYqX-PZfn27URQZRnAM7a6fa0ljHuw
# 826228868
# u.message.chat_id : 65708965

my_token = '826228868:AAF-MKYqX-PZfn27URQZRnAM7a6fa0ljHuw'

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 65708965
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)
    
    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class BotWhale(TelegramBot):
    def __init__(self):
        self.token = '826228868:AAF-MKYqX-PZfn27URQZRnAM7a6fa0ljHuw'
        TelegramBot.__init__(self, '고래', self.token)
        self.updater.stop()

    def start(self):
        self.sendMessage('고래가 잠에서 깨어납니다.')
        self.updater.start_polling(timeout=3, clean=True)
        self.updater.idle()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))
