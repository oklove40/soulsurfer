import math

class Cake:
    coat = '생크림'

    def __init__(self, candles, price, topping):
        self.candles = candles
        self.price = price
        self.topping = topping
    
    def describe(self): #self는 인스턴스 로 호출할때 발생됨. static처럼 사용하면 에러남
        print('이 케익은', self.coat, '(으)로 덮여 있다.')
        print('초가', self.candles, '개 꼽혀있습니다.')
        print('가격은', self.price, '원 입니다.')
        print('토핑은', self.topping, ' 입니다.')

# 클래스 확인
#print(Cake)

cake1 = Cake(12, 30000, '딸기')
cake2 = Cake(5, 45000, '딸기 + 파인애플')

# 인스턴스확인
#print(type(cake2))

# 인스턴스비교
#print(isinstance(cake1, Cake))

# 연습문제 8-5 좌표 클래스 정의하기
class Coordinate:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #
    def distance(self, coordinate):
        return math.sqrt(
            ((self.x - self.y)*(self.x - self.y)) +
            ((coordinate.x - coordinate.y)*(coordinate.x - coordinate.y))
        )


# print(Coordinate)
# 멤버확인
# print(Coordinate.x, '/', cake1.coat)

cake1.price = 4000
cake1.coat = '쵸코'

# print(cake1.price)
# print(cake2.price)

# 클래스 속성확인
# import pprint
# pprint.pprint(dir(Cake))

# 연습문제 8-6 좌표 클래스의 인스턴스 생성하기

coordinate1 = Coordinate(1, 2)
coordinate1.x = -1
coordinate1.y = 2

coordinate2 = Coordinate(3, 4)
coordinate2.x = 2
coordinate2.y = 3

# print(coordinate1.x)
# print(coordinate2.x)
# print(Coordinate.x)

# 연습문제 8-7 좌표 인스턴스의 거리 계산하기

# def square(x):
#     return x * x

# def distance(pointA, pointB):
#     return math.sqrt(
#         square(pointA.x - pointA.y) +
#         square(pointB.x - pointB.y)
#     )

# print(distance(coordinate1, coordinate2))

# 클래스 메서드 정의
# print(Cake.describe())
# print(cake1.describe())

# 연습문제 8-8 좌표 인스턴스의 거리를 메서드로 계산하기
# print(coordinate1.distance(coordinate2))


# 8.3.4 인스턴스 초기화하기 - 부터 볼것!!!
# cake1 = Cake(12, 30000, '딸기')
# print('cake 1')
# print('cake 1 : ', cake1.candles)

# cake2 = Cake(5, 45000, '딸기 + 파인애플')
# print('cake 2')
# print('cake 2 : ', cake2.describe())

# cake3 = Cake(45, 30000, '사과 + 딸기')
# print('cake 3')
# print(cake3.describe())

# 연습문제 8-9 좌표 인스턴스 초기화하기

# coordinate1 = Coordinate(-1, 2)
# print(coordinate1.x, coordinate1.y)

# coordinate2 = Coordinate(y=3, x=2)
# print(coordinate2.x, coordinate2.y)

# # 이하 에러
# # coordinate3 = Coordinate()
# # print(coordinate3.x, coordinate3.y)

# # coordinate4 = Coordinate(10)
# # print(coordinate3.x, coordinate3.y)


