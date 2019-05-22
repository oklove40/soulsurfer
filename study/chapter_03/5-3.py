dicMenu = {
    'coffee'  :   2500
    ,   'juice'   :   3500
    ,   'milk'    :   2000
    ,   'late'    :   3500
    ,   'cake'    :   4000
}

print(dicMenu)
#Dictionary내부에 존재여부
print('coffee' in dicMenu)
print('steem' in dicMenu)

#길이
print(len({}))
print(len(dicMenu))

#key호출
print(dicMenu['cake'])
print(dicMenu.get('milk'))

#없는key호출
try:
    print(dicMenu['cakes'])
except Exception as e:
    print(type(e))

print(dicMenu.get('cakes'))

print(dicMenu)
#값변경
dicMenu['cake'] = 4500
print(dicMenu)

#추가
dicUpdate = {
        'apple'  :   1500
    ,   'mango'  :   2500
}
print(dicUpdate)
dicMenu.update(dicUpdate)
print(dicMenu)

#키값
print(dicMenu.keys())
#값
print(dicMenu.values())

#append
dicMenuList = []
dicMenuList.append(dicMenu)
print(dicMenuList)
dicMenuList.append(dicUpdate)
print(dicMenuList)

print(dicMenuList[0])
print(dicMenuList[1])


