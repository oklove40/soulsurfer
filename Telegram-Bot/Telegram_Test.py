from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
import local

config = local.Config("bot.ini", debug=True)
my_token = config.telegram.key

import MessageApi
msgBot = MessageApi.MessageModule(config.mongodb.connString, config.telegram.key, config.whalealert.key)

# real path to dirname
dir_now = os.path.dirname(os.path.abspath(__file__))

print('start telegram chat bot')

# message reply function
def receivedMessage(bot, update) :
    # update.message.reply_text("got text")
    update.message.reply_text(update.message.text)

# help reply function
def helpCommand(bot, update) :
    update.message.reply_text("뭘 도와줄까?")

# photo reply function
def get_photo(bot, update) :
    file_path = os.path.join(dir_now, 'from_telegram.png')
    photo_id = update.message.photo[-1].file_id  # photo 번호가 높을수록 화질이 좋음
    photo_file = bot.getFile(photo_id)
    photo_file.download(file_path)
    update.message.reply_text('photo saved')

# file reply function
def get_file(bot, update) :
    file_id_short = update.message.document.file_id
    file_url = os.path.join(dir_now, update.message.document.file_name)
    bot.getFile(file_id_short).download(file_url)
    update.message.reply_text('file saved')

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


updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, receivedMessage)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('help', helpCommand)
updater.dispatcher.add_handler(help_handler)

photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

# WhaleAlert
updater.dispatcher.add_handler(CommandHandler('w', apiCallCommandHandler))

updater.start_polling(timeout=3, clean=True)
updater.idle()


