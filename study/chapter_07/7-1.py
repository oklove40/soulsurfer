weather_list = []

def weatherList():
    weather_list.insert(0,['9월 1일','경기','맑음'     ,'27.2','0.4','0.1'])
    weather_list.insert(1,['9월 1일','강원','맑음'     ,'23.6','0.6','0.1'])
    weather_list.insert(2,['9월 1일','충청','맑음'     ,'24.4','0.35','0.1'])
    weather_list.insert(3,['9월 1일','경상','맑음'     ,'26','0.55','0.1'])
    weather_list.insert(4,['9월 1일','전라','맑음'     ,'27','0.4','0'])
    weather_list.insert(5,['9월 1일','제주','구름조금' ,'26.4','0.45','0.1'])

    print('날짜', '지역', '날씨', '기온', '습도', '강수확률')

    for i in weather_list:
        print(i[0], i[1], i[2], i[3], i[4], i[5])
    
#weatherList()

weather_list.clear()

def weatherListDictionary():
    weather_list.append({'day':'9월 1일','area':'경기','status':'맑음','temp':'27.2','mois':'0.4','rain':'0.1'})
    weather_list.append({'day':'9월 1일','area':'강원','status':'맑음'     ,'temp':'23.6','mois':'0.6','rain':'0.1'})
    weather_list.append({'day':'9월 1일','area':'충청','status':'맑음'     ,'temp':'24.4','mois':'0.35','rain':'0.1'})
    weather_list.append({'day':'9월 1일','area':'경상','status':'맑음'     ,'temp':'26','mois':'0.55','rain':'0.1'})
    weather_list.append({'day':'9월 1일','area':'전라','status':'맑음'     ,'temp':'27','mois':'0.4','rain':'0'})
    weather_list.append({'day':'9월 1일','area':'제주','status':'구름조금' ,'temp':'26.4','mois':'0.45','rain':'0.1'})

    print('')
    print('날짜', '지역', '날씨', '기온', '습도', '강수확률')
    for i in weather_list:
        print(i['day'], i['area'], i['status'], i['temp'], i['mois'], i['rain'])
        for k,v in i.items():
            print(k, v)

#weatherListDictionary()

def happy():
    happiness = {
        '호주': 7.95
    ,   '노르웨이': 7.9
    ,   '미국': 7.85
    ,   '일본': 6.2
    ,   '한국': 5.75
    }

    for k, v in happiness.items():
        print(k, '사람들은', v,' 만큼 행복합니다.')

#happy()

def sixteenYear():
    sky = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
    land = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']

    txt = ""

    for s in sky:
        for l in land:
            txt += " " + s + l
        print(txt)
        txt = ""

#sixteenYear()

def tourForSeason():
    seasons = ['봄','여름','가을','겨울']
    destinations = ['ICN','VVO','DPS','CGK','KTM']

    for i in range(0,4):
        print(seasons[i], ' 에는 ', destinations[i])

    for season, destination in zip(seasons, destinations):
        print(season, ' 에는 ', destination)

#tourForSeason()

def testZip():
    listOne = [1,2,3]
    listTwo = [4,5,6]
    listSum = []

    for one, two in zip(listOne, listTwo):
        listSum.append(one + two)

    print(listSum)

#testZip()

prices = [1500,2000,2500,3000,3500,4000,4500,5000]
print(prices)

tempPrice = []

#일반적인 방법
for price in prices:
    tempPrice.append(price + 50)
    
#print(tempPrice)
tempPrice.clear()

#[] 로 list 형태 생성
tempPrice = [price + 50 for price in prices]
#print(tempPrice)
tempPrice.clear()

#list 함수 사용
tempPrice = list(price + 50 for price in prices)
#print(tempPrice)
tempPrice.clear()

#list + map + lambda 사용
tempPrice = list(map(lambda price:price + 50, prices))
#print(tempPrice)
tempPrice.clear()

#평균
#print(int(sum(prices,0)/len(prices)))
#max
#print(max(prices))
#min
#print(min(prices))

#list 검색
tempPrice = list(price for price in prices if price <= 4000)
#print(tempPrice)
tempPrice.clear()

#list filter
tempPrice = list(filter(lambda price:price <= 2000, prices))
#print(tempPrice)
tempPrice.clear()

#연습문제 7-11 용의자 프로파일링
def profiling():
    suspects = [
        {'이름': '멍멍', '털': '흰색', '주둥이': '크다', '발': '크다'}
    ,    {'이름': '킁킁', '털': '검은색', '주둥이': '작다', '발': '크다'}
    ,    {'이름': '왈왈', '털': '흰색', '주둥이': '작다', '발': '크다'}
    ,    {'이름': '꿀꿀', '털': '검은색', '주둥이': '작다', '발': '작다'}
    ,    {'이름': '낑낑', '털': '흰색', '주둥이': '작다', '발': '작다'}
    ]

    tempPrice = list(filter(lambda dog:dog['털'] == '흰색' and dog['주둥이'] == '작다' and dog['발'] == '크다', suspects))
    for item in tempPrice:
        print(item['이름'])

#profiling()

#연습문제 7-12 불량율 계산
diameters = [0.985, 0.992, 1.004, 0.995, 0.899, 1.001, 1.002, 1.003, 1.009, 0.998]

def faultyRate(diameters):
    length = len(list(filter(lambda item:float(item) >= 0.99 and float(item) < 1.01, diameters)))
    print(length, '|', len(diameters), ' => ', len(diameters) - length)

#faultyRate(diameters)


#Algorithm
import copy

tempPrice = copy.deepcopy(prices)
tempPrice.append('1000')
# print(tempPrice)
#print(prices)

coll = [10, 5, 1, 9, 7, 3]
# print(coll)
# print(sorted(coll))
# print(coll)
coll = sorted(coll)
# print(coll)
coll = sorted(coll, reverse=True)
# print(coll)

#key로 sort
menus = [
  {'name': '아메리카노', 'price': 2000}
, {'name': '카페라테', 'price': 2500}
, {'name': '카푸치노', 'price': 2400}
]

sortedMenus = sorted(menus, key=lambda menu:menu['price'])
# print(sortedMenus)

# 연습문제 7-13 길이로 정렬하기
fruits = ['배', '사과', '복숭아', '블루베리']
# print(sorted(fruits))
# print(sorted(fruits, key=lambda v:len(v)))
# print(sorted(fruits, key=lambda v:len(v), reverse=True))
