# 8.4 클래스의 포함 관계 나타내기

class Cake():
    coat = '케익'

    def __init__(self, candles, price, topping):
        self.candles = candles
        self.price = price
        self.topping = topping
    
    def describe(self): #self는 인스턴스 로 호출할때 발생됨. static처럼 사용하면 에러남
        print('이 케익은', self.coat, '(으)로 덮여 있다.')
        print('초가', self.candles, '개 꼽혀있습니다.')
        print('가격은', self.price, '원 입니다.')
        print('토핑은', self.topping, ' 입니다.')

class ChocolateCake(Cake):
    coat = '초콜릿'
    cacao_percent = 32.0

# print(ChocolateCake.coat)
# print(ChocolateCake.cacao_percent)

# chocolateCake1 = ChocolateCake(5, 12000, '딸기')
# print(chocolateCake1.describe())

class IceCreamCake(Cake):
    coat = '아이스크림'
    flavor = '정해지지 않은 맛'

    def __init__(self, flavor, price, topping, candles=0):
        self.flavor = flavor
        # print(self.flavor, ' 맛입니다.')
        super().__init__(candles, price, topping)

# ice_cream_cake_1 = IceCreamCake('바닐라맛', 12000, '딸기')
# print(ice_cream_cake_1.describe())

class FruitIceCreamCake(IceCreamCake):
    fruit_percent = 30

    def __init__(self, fruit_percent, flavor, price, topping, candles=0):
        self.fruit_percent = fruit_percent
        # print('과일 함유량은 ', self.fruit_percent, ' 입니다.')
        super().__init__(flavor, price, topping, candles=candles)

# fruit_ice_cream_cake1 = FruitIceCreamCake(95, '오레오', 25000, '쿠키')
# print(fruit_ice_cream_cake1.describe())

# Cake.radius = 20
# print(IceCreamCake.radius)

# IceCreamCake.radius = 16
# print(Cake.radius)
# print(IceCreamCake.radius)



# 연습문제 8-10 도형 클래스 정의하기 1

class Shape():
    sides=0

    def __init__(self, sides):
        self.sides = sides

    def describe(self):
        print('이 도형은 ', self.sides, ' 개의 변을 가지고 있습니다.')

class Triangle(Shape):
    def __init__(self, sides=3):
        super().__init__(sides)

class Ractangle(Shape):
    def __init__(self, sides=4):
        super().__init__(sides)

triangle1 = Triangle()
print(triangle1.describe())

ractangle1 = Ractangle()
print(ractangle1.describe())


