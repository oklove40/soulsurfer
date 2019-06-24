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

class coinness:
    def __init__(self, title, date, description, link, oriLink, html, type):
        self.title = title
        self.keyDate = keyDate
        self.description = description
        self.link = link
        self.oriLink = oriLink
        self.html = html
        self.type = type    #   1:자금흐름보기, 2:시황 전문 보기, 3:실시간 암호화폐 자금 흐름, 4:이 시각 핫 코인

rss = requests.get('https://kr.coinness.com/newsflash.rss')
# print(rss.text)

coinnessList = []

soup = BeautifulSoup(rss.text, 'lxml-xml')

for feed in soup.select('item'):
    keyDate = list(datefinder.find_dates(feed.pubDate.text.replace('0800','8')))[0]
    oriLink = feed.link.text

    # 자금흐름보기
    valueTransactionView = feed.description.text.find('자금흐름보기')
    if valueTransactionView > 0:
        # print(feed.title.text, feed.link.text, feed.pubDate.text)

        link = feed.description.text[valueTransactionView + 8:]
        # print(link)
        # print(keyDate)

        # 페이지 크롤링
        html = requests.get(link)
        print(html)

        bs = BeautifulSoup(html.text, 'html.parser')
        tags = bs.findAll('img', attrs={'alt': 'image.png'})
        detailImg = ''

        for tag in tags :
            # 검색된 태그에서 a 태그에서 텍스트를 가져옴
            # print(tag)
            # detailImg = str(tag).replace('<','&lt;').replace('>','&gt;')
            detailImg = tag['src']
            break

        coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, link, oriLink, detailImg, 1))
        
    # 시황
    valueSituration = feed.description.text.find('시황 전문 보기')
    if valueSituration > 0:
        # print(feed.title.text, feed.link.text, feed.pubDate.text)
        link = feed.description.text[valueSituration + 10:]
        # print(link)

        coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, link, oriLink, '', 2))

    # 암호화폐 자금 흐름
    valueTransaction = feed.title.text.find('실시간 암호화폐 자금 흐름')
    if valueTransaction > 0:
        # print(feed.title.text, feed.link.text, feed.pubDate.text)
        # print(feed.description.text)

        coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, '', oriLink, '', 3))

    # 이 시각 핫 코인
    hotCoin = feed.title.text.find('이 시각 핫 코인')
    if hotCoin > 0:
        print(feed.title.text, feed.link.text, feed.pubDate.text)
        # print(feed.description.text)

        coinnessList.append(coinness(feed.title.text, keyDate, feed.description.text, '', oriLink, '', 4))


# print(root)
# print(list(datefinder.find_dates(feed.pubDate.text.replace('0800','8')))[0])

for item in coinnessList:
    print(item)

# Telegram 알림
import MessageApi
# import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import Setting
config = Setting.Config("bot.ini", debug=True)

msgBot = MessageApi.MessageModule(config.mongodb.connString, config.telegram.key, config.whalealert.key)

# apiCall
# def apiCallCommandHandler(bot, update):
#     update.message.reply_text('없음.')

import telegram
bot = telegram.Bot(msgBot.token)
for item in coinnessList:
    # print(item)
    if item.type == 1:
        bot.sendMessage(65708965, item.title)
        bot.sendMessage(65708965, item.html.replace("'",""), 'HTML')
        # bot.sendMessage(65708965, '자금흐름보기:' + item.link)
    elif item.type == 2:
        bot.sendMessage(65708965, item.title + '\n' + item.description + '\n\n 원문보기 : ' + item.oriLink + '\n\n시황 전문 보기:' + item.link)
    elif item.type == 3:
        bot.sendMessage(65708965, item.title + '\n' + item.description + '\n\n 원문보기 : ' + item.oriLink)
    elif item.type == 4:
        bot.sendMessage(65708965, item.title + '\n' + item.description + '\n\n 원문보기 : ' + item.oriLink)


# updater = Updater(msgBot.token)

# # WhaleAlert
# updater.dispatcher.add_handler(CommandHandler('w', apiCallCommandHandler))

# updater.start_polling()
# updater.idle()
