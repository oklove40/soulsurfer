import Setting
config = Setting.Config("bot.ini", debug=True)

import MessageApi
msgBot = MessageApi.MessageModule(config.mongodb.connString, config.telegram.key, config.whalealert.key)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
updater = Updater(msgBot.token)



# 날짜변환
def timestampToDatetime(timestamp):
    import datetime
    _date = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    return _date

# Start 메세지
def startCommandHandler(bot, update) :
    msg = "Hi. I'm Whale Alert Api Boot! "
    msg += "\n i will send you updates on registration crytocurrency transation in one hour."
    # 설명
    msg += "\n send /s for help"
    # 금액설정
    msg += "\n send /v to minimum value - upper 500000"
    # api call
    msg += "\n send /w to call Api"
    # 코인별
    msg += "\n send /c to Search by coin"
    # 시간별
    msg += "\n send /t to Search by time"
    # 날짜별
    msg += "\n send /d to Search by day"
    # 금액대 그래프
    msg += "\n send /g return view value by graph"

    update.message.reply_text(msg)

# minimum value Setting
def minimumValue(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def minimumCommandHandler(bot, update):
    show_list = []
    show_list.append(InlineKeyboardButton("5 m", callback_data="500000"))
    show_list.append(InlineKeyboardButton("10 m", callback_data="1000000"))
    show_list.append(InlineKeyboardButton("50 m", callback_data="5000000"))
    show_list.append(InlineKeyboardButton("100 m", callback_data="10000000"))
    show_list.append(InlineKeyboardButton("500 m", callback_data="50000000"))
    show_list.append(InlineKeyboardButton("1000 m", callback_data="100000000"))
    show_markup = InlineKeyboardMarkup(minimumValue(show_list, len(show_list) - 1))

    update.message.reply_text("원하는 값을 선택하세요.", reply_markup=show_markup)

def callback_get(bot, update):
    msgBot.min_value = update.callback_query.data
    bot.edit_message_text(format(update.callback_query.data) + "으로 셋팅되었습니다."
        , chat_id=update.callback_query.message.chat_id
        , message_id=update.callback_query.message.message_id)

# apiCall
def apiCallCommandHandler(bot, update):
    newArticle = []
    newArticle = msgBot.apiCheck()

    if len(newArticle) > 0:
        for item in newArticle:
            msg = str(timestampToDatetime(item['timestamp'])) + '\n [' + str(item['blockchain']) + '] USD:' + str(format(item['amount_usd'], ",")) + ' (' + str(format(item['amount'], ",")) + ')'
            update.message.reply_text(msg)
    else:
        update.message.reply_text('없음.')

# 답변
def receivedMessageHandler(bot, update):
    update.message.reply_text(update.message.text + '|' + msgBot.getNow())























# 시작메세지
import telegram
bot = telegram.Bot(msgBot.token)
bot.sendMessage(65708965, '숨쉬는 고래를 찾고 있습니다.')


# 핸들러 등록
# start
updater.dispatcher.add_handler(CommandHandler('s', startCommandHandler))
# minimum Value
updater.dispatcher.add_handler(CommandHandler('v', minimumCommandHandler))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))
# WhaleAlert
updater.dispatcher.add_handler(CommandHandler('w', apiCallCommandHandler))
# 답변
updater.dispatcher.add_handler(MessageHandler(Filters.text, receivedMessageHandler))

# start
updater.start_polling(timeout=3, clean=True)
updater.idle()
