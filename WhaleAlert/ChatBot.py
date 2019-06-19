import sys
import TelegramModel

# 텔레그램 알림
print('텔레그램 알림')

def proc_rolling(bot, update):
    bot.sendMessage('굴리라우!')
    sound = firecracker()
    bot.sendMessage(sound)
    bot.sendMessage('다 굴렀음.')

def proc_received(bot, update):
    print(update.message.text)
    TelegramModel.TelegramBot().sendMessage('test')
    bot.receivedMessage(update)
    # bot.sendMessage('got text')
    # bot.sendMessage(update.message.text)

def proc_stop(bot, update):
    bot.sendMessage('끝')
    bot.stop()

def firecracker():
    return '굴러간다~~~~ 소오리'

bot = TelegramModel.BotWhale()

# 명령어 등록
bot.add_handler('rolling', proc_rolling)
bot.add_handler('stop', proc_stop)
bot.add_msg_handler(proc_received)

# bot.sendMessage('test')

# 시작
bot.start()
