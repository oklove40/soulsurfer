class Cake:
    coat = '생크림'

    def describe(self):
        print('이 케익은', self.coat, '(으)로 덮여 있다.')

# 클래스 확인
#print(Cake)

cake1 = Cake()
cake2 = Cake()

# 인스턴스확인
#print(type(cake2))

# 인스턴스비교
#print(isinstance(cake1, Cake))

# 연습문제 8-5 좌표 클래스 정의하기
class Coordinate:
    x = 0
    y = 0

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

coordinate1 = Coordinate()
coordinate1.x = -1
coordinate1.y = 2

coordinate2 = Coordinate()
coordinate2.x = 2
coordinate2.y = 3

# print(coordinate1.x)
# print(coordinate2.x)
# print(Coordinate.x)

# 연습문제 8-7 좌표 인스턴스의 거리 계산하기
# import math
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

print(cake1.describe())



