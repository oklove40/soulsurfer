# pip install feedparser

# rss 주소
# https://kr.coinness.com/newsflash.rss

# Rss 리드
# import feedparser

# urls = ('https://kr.coinness.com/newsflash.rss')

# def craw_rss(url):
#     data = feedparser.parse(url)
#     print(data)
#     print(data.feed['title'])
    
#     for feed in data.entries:
#         print('title : ' + feed.title)
#         print('link : ' + feed.link)
#         print('description : ' + feed.description)
#         print('pubDate : ' + feed.pubDate)


# def main():
#     for url in urls:
#         craw_rss(url)

# if __name__ == "__main__":
#     main()


# pip install beautifulsoup4
# pip install lxml
# pip install datefinder
import requests
from bs4 import BeautifulSoup
import datefinder

# 이미지 합치기
# https://rednooby.tistory.com/101
# pip install ipython[all]
# pip install pillow
# from IPython.display import Image
# from PIL import Image as PILImage
# import os

class coinness:
    def __init__(self, title, keyDate, description, link, oriLink, html, type, imgs, imageName):
        self.title = title
        self.keyDate = keyDate
        self.description = description
        self.link = link
        self.oriLink = oriLink
        self.html = html
        self.type = type    #   1:자금흐름보기, 2:시황 전문 보기, 3:실시간 암호화폐 자금 흐름, 4:이 시각 핫 코인, 5:데일리 리포트, 6:저녁 시황, 7:저녁 뉴스 브리핑
        self.imgs = imgs
        self.imageName = imageName

coinnessList = []
imgs = []

def main():
    url = 'https://kr.coinness.com/newsflash.rss'
    rss = requests.get(url)
    soup = BeautifulSoup(rss.text, 'lxml-xml')

    for feed in soup.select('item'):
        # print(feed.title.text, feed.link.text, feed.pubDate.text)
        keyDate = list(datefinder.find_dates(feed.pubDate.text.replace('0800','8')))[0]
        oriLink = feed.link.text

        # 자금흐름보기
        valueTransactionView = feed.description.text.find('자금흐름보기')
        if valueTransactionView > 0:
            link = feed.description.text[valueTransactionView + 8:]

            # 페이지 크롤링
            html = requests.get(link)

            bs = BeautifulSoup(html.text, 'html.parser')
            tags = bs.findAll('img', attrs={'alt': 'image.png'})

            imgs = []
            for tag in tags :
                imgs.append(tag['src'])

            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, link, oriLink, '', 1, imgs, ''))
            
        # 시황
        valueSituration = feed.description.text.find('시황 전문 보기')
        if valueSituration > 0:
            link = feed.description.text[valueSituration + 10:]
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, link, oriLink, '', 2, [], ''))

        # 데일리 리포트
        daily = feed.title.text.find('데일리 리포트')
        if daily > 0:
            cnt = feed.description.text.find('전문보기')
            link = feed.description.text[cnt + 7:]

            # 페이지 크롤링
            html = requests.get(link)

            bs = BeautifulSoup(html.text, 'html.parser')
            tags = bs.findAll('img', attrs={'alt': 'image.png'})

            imgs = []
            for tag in tags :
                imgs.append(tag['src'])
            
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, link, oriLink, '', 5, imgs, ''))

        # 암호화폐 자금 흐름
        valueTransaction = feed.title.text.find('실시간 암호화폐 자금 흐름')
        if valueTransaction > 0:
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, '', oriLink, '', 3, [], ''))

        # 이 시각 핫 코인
        hotCoin = feed.title.text.find('이 시각 핫 코인')
        if hotCoin > 0:
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, '', oriLink, '', 4, [], ''))

        # 저녁 시황
        night = feed.title.text.find('저녁 시황')
        if night > 0:
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, '', oriLink, '', 6, [], ''))

        # 오전 시황
        morning = feed.title.text.find('오전 시황')
        if morning > 0:
            cnt = feed.description.text.find('전문보기')
            link = feed.description.text[cnt + 7:]
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, link, oriLink, '', 9, [], ''))

        # 저녁 뉴스 브리핑
        nightBriefing = feed.title.text.find('저녁 뉴스 브리핑')
        if nightBriefing > 0:
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, '', oriLink, '', 7, [], ''))

        # 아침 뉴스 브리핑
        morningBriefing = feed.title.text.find('아침 뉴스 브리핑')
        if morningBriefing > 0:
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, '', oriLink, '', 8, [], ''))

        # 대량 이체
        bigTrade = feed.title.text.find('대량 이체')
        if bigTrade > 0:
            coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, '', oriLink, '', 10, [], ''))

import MessageApi
import Setting
_configValue = Setting.Config("bot.ini", debug=True)
msgBot = MessageApi.MessageModule(_configValue.mongodb.connString, _configValue.telegram.key, _configValue.whalealert.key)
alertList = []

import datetime

# Telegram 알림
def sendTelegram():
    import telegram

    bot = telegram.Bot(msgBot.token)
    for item in coinnessList:
        cnt = len(list(msgBot.collection.find({'keyDate':str(item.keyDate)})))
        if cnt == 0:
            if item.type == 2 or item.type == 9:
                alertList.append(
                    {
                        '_id' : TimestampMillisec64(item.type)
                        , 'title': item.title
                        , 'keyDate': str(item.keyDate)
                        , 'description': item.description
                        , 'link': item.link
                        , 'oriLink': item.oriLink
                        , 'html': item.html
                        , 'type': item.type
                        , 'imgs': item.imgs
                        , 'imageName': item.imageName
                    }
                )
                bot.sendMessage(65708965, item.title + '\n\n' + item.description)
            elif item.type == 3 or item.type == 4 or item.type == 6 or item.type == 7 or item.type == 8 or item.type == 10:
                alertList.append(
                    {
                        '_id' : TimestampMillisec64(item.type)
                        , 'title': item.title
                        , 'keyDate': str(item.keyDate)
                        , 'description': item.description
                        , 'link': item.link
                        , 'oriLink': item.oriLink
                        , 'html': item.html
                        , 'type': item.type
                        , 'imgs': item.imgs
                        , 'imageName': item.imageName
                    }
                )
                bot.sendMessage(65708965, item.title + '\n\n' + item.description + '\n\n 원문보기 : ' + item.oriLink)
            elif item.type == 1 or item.type == 5:
                alertList.append(
                    {
                        '_id' : TimestampMillisec64(item.type)
                        , 'title': item.title
                        , 'keyDate': str(item.keyDate)
                        , 'description': item.description
                        , 'link': item.link
                        , 'oriLink': item.oriLink
                        , 'html': item.html
                        , 'type': item.type
                        , 'imgs': item.imgs
                        , 'imageName': item.imageName
                    }
                )
                bot.sendMessage(65708965, item.title + '\n\n')
                for img in item.imgs:
                    bot.sendPhoto(65708965, img)

def getNow():
    now =datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def TimestampMillisec64(type):
    mil = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) + type
    return mil

def interval():
    print(getNow())

    main()
    if len(coinnessList) > 0:
        sendTelegram()
    if len(alertList) > 0:
        msgBot.collection.insert(alertList)
        # for item in alertList:
        #     print(item.title)

    # 초기화
    alertList.clear()

# 인터벌처리
import threading

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

if __name__ == "__main__":
    print('start!')
    interval()

    setInterval(interval, 300)

















# print(getNow())
# print(TimestampMillisec64(0))

# interval()

# # apiCall
# from telegram.ext import Updater, CommandHandler

# def apiCallCommandHandler(bot, update):
#     update.message.reply_text('없음.')

# updater = Updater(msgBot.token)

# # WhaleAlert
# updater.dispatcher.add_handler(CommandHandler('w', apiCallCommandHandler))

# updater.start_polling()
# updater.idle()
