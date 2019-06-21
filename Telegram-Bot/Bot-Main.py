import MessageApi
import TelegramApi
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import Setting
# config = Setting.Config("bot.ini", debug=True)

# 시작
import local
config = local.Config("bot.ini", debug=True)

msgBot = MessageApi.MessageModule(config.mongodb.connString, config.telegram.key, config.whalealert.key)
# msgBot.sendMsg('test')

# 핸들러용 메소드들
# help
def helpCommandHandler(bot, update) :
    update.message.reply_text("최소금액설정: /s")
    update.message.reply_text("금액설정: /g")
    update.message.reply_text("코인: /c")
    update.message.reply_text("api call: /w")

# Start 메세지
def startCommandHandler(bot, update) :
    msg = "Hi. I'm Whale Alert Api Boot! "
    msg += "\n i will send you updates on registration crytocurrency transation in one hour."
    msg += "\n send /s to activate bot"
    msg += "\n send /v to minimum value - upper 500000"
    msg += "\n send /h to help"
    msg += "\n send /a to call Api"

    update.message.reply_text(msg)

# 최소 금액설정
def setMinValueCommandHandler(bot, update) :
        msgBot.setMinValue('100000')

# apiCall
def apiCallCommandHandler(bot, update):
    newArticle = []
    newArticle = msgBot.apiCheck()

    if len(newArticle) > 0:
        for item in newArticle:
            msg = '[' + str(item['blockchain']) + ']' + str(item['amount_usd']) + '(' + str(item['amount']) + ') : ' + str(item['timestamp'])
            update.message.reply_text(msg)
    else:
        update.message.reply_text('없음.')

# 답변
def receivedMessageHandler(bot, update):
    update.message.reply_text(update.message.text + '|' + msgBot.getNow())

# bot = telegram.Bot(msgBot.token)
updater = Updater(msgBot.token)

# teleBot = TelegramApi.TelegramModule('WhaleAlert', bot, updater)

# 핸들러들
# help
updater.dispatcher.add_handler(CommandHandler('h', helpCommandHandler))
# start
updater.dispatcher.add_handler(CommandHandler('s', startCommandHandler))
# WhaleAlert
updater.dispatcher.add_handler(CommandHandler('w', apiCallCommandHandler))
# 답변
updater.dispatcher.add_handler(MessageHandler(Filters.text, receivedMessageHandler))

updater.start_polling()
updater.idle()
