import TelegramApi

# 이하 핸들러들
# 1. 메세지 받는 핸들러
def msg(bot, update):
    bot.receivedMessage(update)
    # update.message.reply_text('메세지 받는 핸들러')

# 2. 사진 받는 핸들러
# def photo(bot, update):
def photo(bot, update):
    update.message.reply_text('사진 받는 핸들러')

# 3. 파일 받는 핸들러
def file(bot, update):
    update.message.reply_text('파일 받는 핸들러')

# 4. 명령어 받는 핸들러
def cmd(bot, update):
    update.message.reply_text('명령어 받는 핸들러')

bot = TelegramApi.WhaleBreath()

# 핸들러 등록
# 1. 메세지 받는 핸들러
bot.addMessageHandler(msg)

# 2. 사진 받는 핸들러
bot.addMessageHandler(photo)

# 3. 파일 받는 핸들러
bot.addMessageHandler(file)

# 4. 명령어 받는 핸들러
bot.addCommanHandler('help', cmd)

# 시작
bot.start()
