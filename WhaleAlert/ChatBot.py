import sys
import TelegramModel

def proc_rolling(bot, update):
    bot.sendMessage('굴리라우!')
    sound = firecracker()
    bot.sendMessage(sound)
    bot.sendMessage('다 굴렀음.')

def proc_stop(bot, update):
    bot.sendMessage('끝')
    bot.stop()

def firecracker():
    return '굴러간다~~~~ 소오리'


bot = TelegramModel.BotWhale()

# 명령어 등록
bot.add_handler('rolling', proc_rolling)
bot.add_handler('stop', proc_stop)

# 시작
bot.start()

