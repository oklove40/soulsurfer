import configparser
import telegram
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

class TelegramModule:
    def __init__(self, name, telegram, Updater):
        self.name = name
        self.id = 65708965
        self.core = telegram
        self.updater = Updater

    def sendMsg(self, text):
        self.core.sendMessage(chat_id=self.id, text=text)    

    def receivedMessage(self, update):
        update.message.reply_text(update.message.text)

    def start(self):
        # self.sendMsg('숨쉬는 고래를 찾고 있습니다.')
        self.updater.start_polling()
        self.updater.idle()
        
    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()
