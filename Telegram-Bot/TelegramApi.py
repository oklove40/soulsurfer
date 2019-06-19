from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

class Telegram:
    def __init__(self, name, token):
        self.name = name
        self.updater = Updater(token)

    def sendMsg(self, text):
        self.updater.message.reply_text(text)

    def receivedMessage(self, update):
        self.update.message.reply_text(update.message.text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class WhaleBreath(Telegram):
    def __init__(self):
        self.token = '826228868:AAF-MKYqX-PZfn27URQZRnAM7a6fa0ljHuw'
        Telegram.__init__(self, '고래', self.token)
        self.updater.stop()
    
    def addCommanHandler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))
    
    def addMessageHandler(self, func):
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, func))

    def start(self):
        self.sendMsg('숨쉬는 고래를 찾고 있습니다.')
        self.updater.start_polling()
        self.updater.idle()

