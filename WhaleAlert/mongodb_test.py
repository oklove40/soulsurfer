# from pymongo import MongoClient
import pymongo
import json

def initialDB():
    # DB connection
    conn = pymongo.MongoClient('localhost')
    db = conn.crypto
    
    # 콜렉션 획득, 전역
    global collection
    collection = db.transation

    # db 저장용 데이터 리스트
    global trades
    trades = []

def get_now():
    import datetime
    now =datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

class Trans(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

# db 연결
initialDB()

# 테스트 데이타
api_data = '{"result":"success","cursor":"b9f81e6-b9f81e6-5d087cbf","count":24,"transactions":[{"blockchain":"ethereum-7","symbol":"eth","id":"494993174","transaction_type":"transfer","hash":"2084eca97be1468bfd9f937ad6921ecc6dd083fffe5c612247360e13918400c0","from":{"address":"3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be","owner":"binance","owner_type":"exchange"},"to":{"address":"d551234ae421e3bcba99a0da6d736074f22192ff","owner":"binance","owner_type":"exchange"},"timestamp":1560836993,"amount":6667,"amount_usd":1794742.9,"transaction_count":1},{"blockchain":"ethereum","symbol":"eth","id":"194993240","transaction_type":"transfer","hash":"a41cda979c4bb5829aede4d96eeb9b64a02d3ed77b68bf18e2cf8147cd97a667","from":{"address":"387ad93bfe9957a4eeba0cb2ff9303f6ec0833d0","owner_type":"unknown"},"to":{"address":"540f79e4c0534f33b654f7c59c9a348171245374","owner_type":"unknown"},"timestamp":1560836998,"amount":4777,"amount_usd":1285958.8,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995492","transaction_type":"transfer","hash":"911797e16ceb462122b4a49a4563cd75ecc9ef06be68a61d2d19c89b7f737d7b","from":{"address":"1JDknRvZTi5XdhQB3cgvJ9R8aogUvfbYUB","owner_type":"unknown"},"to":{"address":"1H4o9Mh7HyjPa46z4vtv7J8yzaK5RY4bXR","owner_type":"unknown"},"timestamp":1560837132,"amount":139.24574,"amount_usd":1268318.2,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995497","transaction_type":"transfer","hash":"e233e2e71ad84acdd93ba7d5ff387fd82d09fb9065c98eb118e2b91dd01d8d2a","from":{"address":"1H4o9Mh7HyjPa46z4vtv7J8yzaK5RY4bXR","owner_type":"unknown"},"to":{"address":"1DTm1DipgYM8bWJ3gqQ5dzDb1N56xDtTyZ","owner_type":"unknown"},"timestamp":1560837132,"amount":138.77148,"amount_usd":1263998.6,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995500","transaction_type":"transfer","hash":"9e97ba38034720bcc38b66c83a056077a4161697de0acdd02df46dde612923e5","from":{"address":"1DTm1DipgYM8bWJ3gqQ5dzDb1N56xDtTyZ","owner_type":"unknown"},"to":{"address":"1GoC1B4GWdbnwzpCFNxqDb2zSL9UzQnwrW","owner_type":"unknown"},"timestamp":1560837132,"amount":138.32979,"amount_usd":1259975.5,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995549","transaction_type":"transfer","hash":"94c633c7e10ef3d2204a66aebba966fa303e073285439c80252ff53c64903422","from":{"address":"34PZfthSVVifa1rhWZJD6irZnpGasLJLry","owner_type":"unknown"},"to":{"address":"33iawhCL3N3wjmxw3FmQDGLQSPmz1NLov4","owner_type":"unknown"},"timestamp":1560837132,"amount":91.93263,"amount_usd":837367.4,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995551","transaction_type":"transfer","hash":"5a34eff3c135f2787c510f694f058cdd9b1a2a23531e99fa74d97a4486c270fb","from":{"address":"33iawhCL3N3wjmxw3FmQDGLQSPmz1NLov4","owner_type":"unknown"},"to":{"address":"3HMAs4gEKqkjqB5j9Hc75YDY3km952wPts","owner_type":"unknown"},"timestamp":1560837132,"amount":91.67395,"amount_usd":835011.1,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995553","transaction_type":"transfer","hash":"ce49bb9f1670bf8b36f071d2aae145ff84bb81a42542492f2696f2744a13da73","from":{"address":"3HMAs4gEKqkjqB5j9Hc75YDY3km952wPts","owner_type":"unknown"},"to":{"address":"39GUiZ9621NsNu9VuxgsP1Eu3s5c6EEgr8","owner_type":"unknown"},"timestamp":1560837132,"amount":86.24656,"amount_usd":785575.9,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995555","transaction_type":"transfer","hash":"a49c1ec6f7e2e5d2b0c112f87b71c59246e275a3839db1080830c0fb681cef35","from":{"address":"39GUiZ9621NsNu9VuxgsP1Eu3s5c6EEgr8","owner_type":"unknown"},"to":{"address":"3DGcm4JR8WaNPcqNJckhLoZxsMSBem6pr9","owner_type":"unknown"},"timestamp":1560837132,"amount":85.55928,"amount_usd":779315.75,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995581","transaction_type":"transfer","hash":"30d1dde7c72604e7abbc8b06a29f684713e3646bbc610b37080a985a58216d00","from":{"address":"38ebaesAbaMYsvoq3oVp5gPHTWiUm3VTVP","owner_type":"unknown"},"to":{"address":"366AyYPe7MtzNza1eZdfdWrxGZrJNSFwW2","owner_type":"unknown"},"timestamp":1560837132,"amount":100.95813,"amount_usd":919576.06,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995607","transaction_type":"transfer","hash":"1cf4a18983e8a0d221ed4ff3e67c453eb5e422dec0f512390802d4c12cb4f2af","from":{"address":"366AyYPe7MtzNza1eZdfdWrxGZrJNSFwW2","owner_type":"unknown"},"to":{"address":"38gdNgu1GTDgu7N4z7XfgCuyNjE8YkmHgq","owner_type":"unknown"},"timestamp":1560837132,"amount":99.91216,"amount_usd":910048.8,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995692","transaction_type":"transfer","hash":"46cfccdcd735ec6b0a994c784becc5fceea25d9e37f4565f9c6789d51b493211","from":{"address":"3CkE8MqPv6aLuqkaBgpgmNQYkDU9wSMuNH","owner_type":"unknown"},"to":{"address":"1JJ1ea6rHMrqtHw3oMVWgbenQWxNnqJTSX","owner":"bitfinex","owner_type":"exchange"},"timestamp":1560837132,"amount":122.79,"amount_usd":1118431.4,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995766","transaction_type":"transfer","hash":"4526b67aa7a1a35cd84745f2c5eec552aa7d11d5ad10c4c480f7ca5e72f39f35","from":{"address":"Multiple Addresses","owner":"binance","owner_type":"exchange"},"to":{"address":"3EbSda5tDELTY3hXAgguXanwNuDivqS2ep","owner":"sygnia.io","owner_type":"other"},"timestamp":1560837132,"amount":198.9523,"amount_usd":1812154.9,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194995828","transaction_type":"transfer","hash":"0ea3447a88969e228a529e28beefc23cd6971c3b65adbb1a8f5589d6ea8e9afe","from":{"address":"Multiple Addresses","owner":"poloniex","owner_type":"exchange"},"to":{"address":"37Z43avUa9JX5EyPZG4NpRFGREMp3jdNxT","owner_type":"unknown"},"timestamp":1560837132,"amount":110,"amount_usd":1001933.8,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194996695","transaction_type":"transfer","hash":"000fdcef4f83ef5dd53e432207f24bede978f198ca6e078c8bd8f30418ab4251","from":{"address":"1EEqRvnS7XqMoXDcaGL7bLS3hzZi1qUZm1","owner":"hitbtc","owner_type":"exchange"},"to":{"address":"3JjPf13Rd8g6WAyvg8yiPnrsdjJt1NP4FC","owner_type":"unknown"},"timestamp":1560837132,"amount":70,"amount_usd":637594.25,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194996812","transaction_type":"transfer","hash":"cb05241b32ccb5d500496d8a1411f2b8489f748facb0f03df775284e76f8b037","from":{"address":"1FtYuyMfdBDVS3A7zx8p2pnqE5bZzqAecV","owner_type":"unknown"},"to":{"address":"1NXcGxz6zXkpWsT2m1P2kfqESZLHfbcAwd","owner_type":"unknown"},"timestamp":1560837132,"amount":57.66628,"amount_usd":525252.7,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194996814","transaction_type":"transfer","hash":"d82432fa1c08e5d30caf095e59a1eff1e37b30505e2a584767c4a9173c372f5d","from":{"address":"1ADVyiyg1ABGv1FCSzGF6ksEzD1fCgqoDa","owner_type":"unknown"},"to":{"address":"1Ez8MoGkVDuYiCwm24eCC8CQwtz9gpYPno","owner_type":"unknown"},"timestamp":1560837132,"amount":63.146156,"amount_usd":575166.06,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194999144","transaction_type":"transfer","hash":"348af4e40f68882f1fbb238d39ff045e5eb6b4e0ddbf478981b898193c6c83c9","from":{"address":"1GoC1B4GWdbnwzpCFNxqDb2zSL9UzQnwrW","owner_type":"unknown"},"to":{"address":"1JDknRvZTi5XdhQB3cgvJ9R8aogUvfbYUB","owner_type":"unknown"},"timestamp":1560837197,"amount":133.0635,"amount_usd":1212007.5,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194999151","transaction_type":"transfer","hash":"d81d86396662896516cdfe3b03e22270f92729d36418060159984321f0dc58ac","from":{"address":"3DGcm4JR8WaNPcqNJckhLoZxsMSBem6pr9","owner_type":"unknown"},"to":{"address":"34onoc5R9w5vnRGDJEeVuT2pdLzp4oqbk3","owner_type":"unknown"},"timestamp":1560837197,"amount":85.32009,"amount_usd":777137.1,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194999153","transaction_type":"transfer","hash":"e7b17ac9f563b17b588cdceba45a8bc06cf87aa56636fcb97daf43a9711978cc","from":{"address":"34onoc5R9w5vnRGDJEeVuT2pdLzp4oqbk3","owner_type":"unknown"},"to":{"address":"3QxHQQr6h8wW6BHDQuNooMZtEz861ws71X","owner_type":"unknown"},"timestamp":1560837197,"amount":84.86011,"amount_usd":772947.4,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194999156","transaction_type":"transfer","hash":"024d5e83b3f8a4906f459b35872a57635bd56ae2b05cc9d8bfd2bfb698ba8266","from":{"address":"38gdNgu1GTDgu7N4z7XfgCuyNjE8YkmHgq","owner_type":"unknown"},"to":{"address":"31oD4NTc3tMdVoYMMjEYMcURtWmvK7mLza","owner_type":"unknown"},"timestamp":1560837197,"amount":99.29525,"amount_usd":904429.75,"transaction_count":1},{"blockchain":"bitcoin","symbol":"btc","id":"194999182","transaction_type":"transfer","hash":"c635327454e388a64bbe0a5dc5a79e290e883e81e7016685b750d902509ae3f1","from":{"address":"3Ksm8SYKki9fSWrxHEBC9MDarRH36jMmjG","owner_type":"unknown"},"to":{"address":"3Fms6Qb5M5hgnYAui9JTaQZMXh3i2QhetM","owner_type":"unknown"},"timestamp":1560837197,"amount":82.78302,"amount_usd":754028.25,"transaction_count":1},{"blockchain":"ethereum","symbol":"link","id":"195002270","transaction_type":"transfer","hash":"2426aa55897f95e4eb5e97b1baadc8cfabe51543298a636222c90ae1682a9c87","from":{"address":"b7f9bcc382149fa9078e5221e886d89aa0cfa01d","owner_type":"unknown"},"to":{"address":"780b6df36033c7d6e02872d8efd0a12fa447e5cf","owner_type":"unknown"},"timestamp":1560837255,"amount":292089.4,"amount_usd":577445.8,"transaction_count":1},{"blockchain":"ethereum","symbol":"eth","id":"195002854","transaction_type":"transfer","hash":"b00f4343a3cd5745d8d806d067c910b07cb007ddf435578546929932bd4af95e","from":{"address":"d8a83b72377476d0a66683cde20a8aad0b628713","owner_type":"unknown"},"to":{"address":"eec606a66edb6f497662ea31b5eb1610da87ab5f","owner":"huobi","owner_type":"exchange"},"timestamp":1560837311,"amount":3998,"amount_usd":1071398.1,"transaction_count":1}]}'

# 데이타 정리
api_low_data = str(api_data).replace("'","\"")

# 거래 결과 - deserialize
api_result = Trans(api_low_data)

if api_result.result.__eq__('success'):
    # 데이타 비교
    for i in range(0, api_result.count):
        cnt = len(list(collection.find({'id':api_result.transactions[i]['id']})))
        if cnt == 0:
            api_result.transactions[i]['datetime'] = get_now()
            trades.append(api_result.transactions[i])

    # DB 등록
    # collection.insert(trades)
else:
    print('failed')

# 텔레그램 알림
print('텔레그램 알림')
# print(trades)

# 설치방법
# https://blog.psangwoo.com/coding/2016/12/08/python-telegram-bot-1.html
# 봇만들기
# https://antilibrary.org/2060

# 

import telegram
from telegram.ext import Updater, CommandHandler

my_token = ''

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 826228868
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id=self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class BotWhale(TelegramBot):
    def __init__(self):
        self.token = ''
        TelegramBot.__init__(self, 'SoulSurfer', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('wake up Bot!')
        self.updater.start_polling()
        self.updater.idle()







# 봇선언
bot = telegram.Bot(token = my_token)

# 826228868
# print(bot.id)

# 업데이트 내역
updates = bot.getUpdates()

for u in updates:
    print(u.message)

# for i in range(0, len(trades)):
#     # 가장 최근에 온 메세지의 chat id를 가져옵니다
#     updateCnt = len(bot.getUpdates())

#     if updateCnt == 0 :
#         print(updateCnt)
#         chat_id = updateCnt
#     else:
#         chat_id = bot.getUpdates()[-1].message.chat.id

#     bot.sendMessage(chat_id = chat_id, text="저는 봇입니다.")


