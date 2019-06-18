class Food():
    # 음식을 나타내는 클래스
    def __init__(self, taste, calorie, name):
        # 인스턴스 초기화
        self._taste = taste     #   맛
        self._calorie = calorie #   칼로리
        self._name = name       #   이름

    def __str__(self):
        # 음식 설명
        return self._name + ' 은 ' + str(self._taste) + ' 이런 맛이고 ' + str(self._calorie) + ' 칼로리 입니다.'

    def __add__(self, other):
        # 맛을 더함
        taste = self._taste + other._taste          #   맛을 더함
        calorie = self._calorie + other._calorie    #   칼로리를 더함
        return Food(taste, calorie, self._name + ' / ' + other._name + ' 이 합쳐진')                 #   새로운 인스턴스 반환

    def __ge__(self, other):
        # >=
        #   음식평가, 맛이 좋으면 더큼. 같은맛이면 칼러리가 적은것이 큼. 모두 같으면 같음.
        gapTaste = self._taste - other._taste
        gapCalorie = self._calorie - other._calorie
        foodName = ''
        
        if(gapTaste > 0):
            foodName = self._name
        elif(gapTaste < 0):
            foodName = other._name
        elif(gapTaste == 0 and gapCalorie > 0):
            foodName = self._name
        elif(gapTaste == 0 and gapCalorie < 0):
            foodName = other._name
        elif(gapTaste == 0 and gapCalorie == 0):
            foodName = self._name + '|' + other._name

        print(foodName + ' 이 더 좋은 평가를 받았습니다. ', str(gapTaste), str(gapCalorie))
        
        return foodName

    def __lt__(self, other):
        # <
        #   음식평가, 맛이 좋으면 더큼. 같은맛이면 칼러리가 적은것이 큼. 모두 같으면 같음.
        gapTaste = self._taste - other._taste
        gapCalorie = self._calorie - other._calorie
        foodName = ''
        
        if(gapTaste > 0):
            foodName = self._name
        elif(gapTaste < 0):
            foodName = other._name
        elif(gapTaste == 0 and gapCalorie > 0):
            foodName = self._name
        elif(gapTaste == 0 and gapCalorie < 0):
            foodName = other._name
        elif(gapTaste == 0 and gapCalorie == 0):
            foodName = self._name + '|' + other._name

        print(foodName + ' 이(가) 더 좋은 평가를 받았습니다. ', str(gapTaste), str(gapCalorie))
        
        return foodName





        


# food1 = Food(7, 68)
# print(food1.to_string())

# food2 = Food(1, 250)
# print(food2.to_string())

# food3 = food1.add(food2)
# print(food3.to_string())

# 아래 코드는 이중밑줄 메소드를 사용했을때 사용가능
# https://python.bakyeono.net/chapter-8-5.html 참고
# print(Food(7,85) + Food(3, 256))

# 코드 8-60 연산자 대신 이중 밑줄 메서드로 연산하기

# number = 10
# print('equal : ',number.__eq__(20))
# print('multiply : ',number.__mul__(5))
# print('less then : ',number.__lt__(20))
# print('isFloat : ',number.__float__())
# print('toString : ',number.__str__())
# print('isBool : ',number.__bool__())


# 연습문제 8-13 음식 클래스에 연산 추가하기
# <     =>  __lt__
# >=    =>  __ge__
# + <   =>  __add__    __lt__
# ==    =>  __eq__

strawberry = Food(9, 32, '딸기')
potato = Food(6, 66, '감자')
sweet_potato = Food(12, 131, '고구마')
pizza = Food(13, 266, '핏자')

print('딸기 < 감자: ', strawberry < potato)
print('감자 + 감자 < 고구마: ', potato + potato < sweet_potato)
print('피자 >= 딸기: ', pizza >= strawberry)
print('피자 >= 피자: ', pizza >= strawberry)
print('감자 + 딸기 < 피자: ', potato + strawberry < pizza)
print('딸기 == 딸기: ', potato == potato)
