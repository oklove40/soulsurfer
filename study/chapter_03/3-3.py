def order(orderCnt):
    print('please order')

    drinkPrice = 2500

    drink = input()

    totalPrice = drinkPrice * orderCnt

    print(drink, '를', orderCnt, '잔 주문하셨습니다.')
    orderPrint(drink, '치즈케익')
    return totalPrice

def orderPrint(drink, cake):
    print('음료:', drink, '/', '케익:', cake)


result = order(5)

print('금액은 ', result, ' 입니다.')

#orderPrint('카페라테', '치즈케익')

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alphabet_list[3:6])
print(alphabet_list[:3])
print(alphabet_list[5:])
print(alphabet_list[:])

copied_list = alphabet_list[:]

print(alphabet_list == copied_list)

copied_list[0] = 'A'

print(alphabet_list == copied_list)

copied_list[1:3] = ['300','400']

print(copied_list[:])

numberList = [1,2,3,4,5,6,7,8,9]

print(sum(numberList))