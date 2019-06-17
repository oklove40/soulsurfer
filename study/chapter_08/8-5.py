# 8.5 데이터 유형에 맞는 연산 정의하기

class FruitJuice():
    valid_fruits = {'귤', '복숭아', '청포도', '딸기', '사과'}

    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if ingredient in self.valid_fruits:
            self.ingredients.append(ingredient)
        else:
            print(ingredient, ' 는 과일주스에 넣을수 없습니다.')
        
    def describe(self):
        print('이 주스는 ', len(self.ingredients), ' 개의 재료가 들어 있습니다.')
        print('넣은 재료 : ', end='')
        for ingredient in self.ingredients:
            print(ingredient, end=', ')


juice_1 = FruitJuice()
juice_1.add_ingredient('청포도')
juice_1.add_ingredient('복숭아')
juice_1.add_ingredient('도라지')
juice_1.describe()


