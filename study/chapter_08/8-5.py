# 8.5 데이터 유형에 맞는 연산 정의하기

# class 멤버를 정의할때 _표시가 붙으면 private 으로 정의됨

class FruitJuice():
    _valid_fruits = {'귤', '복숭아', '청포도', '딸기', '사과'}

    def __init__(self):
        self._ingredients = []

    def add_ingredient(self, ingredient):
        if ingredient in self._valid_fruits:
            self._ingredients.append(ingredient)
        else:
            print(ingredient, ' 는 과일주스에 넣을수 없습니다.')
        
    def describe(self):
        print('이 주스는 ', len(self._ingredients), ' 개의 재료가 들어 있습니다.')
        print('넣은 재료 : ', end='')
        for ingredient in self._ingredients:
            print(ingredient, end=', ')


# juice_1 = FruitJuice()
# juice_1.add_ingredient('청포도')
# juice_1.add_ingredient('복숭아')
# juice_1.add_ingredient('도라지')
# juice_1.describe()

# juice_2 = FruitJuice()
# juice_2.ingredients.append('도라지')
# juice_2.describe()

# 연습문제 8-12 주사위

import random

class Dice():
    _dice_sides = {'1','2','3','4','5','6'}

    def __init__(self):
        self._side = 1

    def top(self):
        # self._side = random.sample(self._dice_sides,1)
        self._side = random.randint(1,6)
        print('처음 나온 명 : ', self._side)

    def role(self):
        # self._side = random.sample(self._dice_sides,1)
        self._side = random.randint(1,6)
        print('다시 굴리기 : ', self._side)

# dice_1 = Dice()
# dice_1.top()
# dice_1.role()
# dice_1.role()
