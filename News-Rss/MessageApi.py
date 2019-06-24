# 메세지 관련 API 모음
import pymongo
import configparser
import json
import time
import json
import requests

class MessageModule:
    def __init__(self, connString, token, api_key):
        self.token = token.replace('"','')
        self.api_key=api_key.replace('"','')
        self.connString = connString.replace('"','')
        self.min_value = '500000' #   '10000000'
        self.trades = []
        self.collection = []
        self.initialDB()

    def setMinValue(self, min_value):
        self.min_value = min_value

    def sendMsg(self, text):
        print(text)

    def initialDB(self):
        try:
            # DB connection
            conn = pymongo.MongoClient(self.connString)
            # crypto = conn.crypto
            coinNess = conn.coinNess
            
            # 콜렉션 획득, 전역
            # self.collection = crypto.transation
            self.collection = coinNess.alarmList
        except Exception as identifier:
            pass

    def getNow(self):
        import datetime
        now =datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

    def one_hour_later_timestamp(self, secound):
        return round(time.time()) - secound

    def apiCall(self):
        # 초기화
        self.trades = []
        start = str(self.one_hour_later_timestamp(3500))
        url = 'https://api.whale-alert.io/v1/transactions?api_key='+self.api_key+'&min_value='+self.min_value+'&start='+start+'&cursor=2bc7e46-2bc7e46-5c66c0a7'
        
        try:
            res = requests.get(url)
            # print(res.text)
        except Exception as identifier:
            print(identifier)
            pass

        return json.loads(str(res.text).replace("'","\""))

    def apiCheck(self):
        self.rtnObj = self.apiCall()

        count = int(self.rtnObj['count'])
        if count > 0:
            transactions = self.rtnObj['transactions']

            for j in range(0, count):
                low_data = str(transactions[j]).replace("'from'","'frm'").replace("'","\"")
                # transaction = Trans(low_data)
                # transaction = self.__dict__(json.loads(low_data))
                transaction = json.loads(low_data)

                # 데이타 비교
                cnt = len(list(self.collection.find({'id':transaction['id']})))
                if cnt == 0:
                    transaction['datetime'] = self.getNow()
                    self.trades.append(transaction)
                    # self.collection.insert(transaction)

        # DB 등록
        if len(self.trades) > 0:
            self.collection.insert(self.trades)

        return self.trades

class Trans(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)
