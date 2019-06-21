from telegram.ext import Updater

class TelegramApi:
    def __init__(self, Updater):
        self.updater = Updater

    def start(self):
        self.updater.start_polling()
        self.updater.idle()

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()