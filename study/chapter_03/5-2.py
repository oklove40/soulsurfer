def getArrayByIndex(index):
    list = ['A','B','C','D','E','F','G','H']
    if index < len(list):
        print('선택한 값은 ', list[index], '입니다.')
    else:
        print(len(list), ' 보다 작은수를 입력하세요.')

print('수를 선택하세요.')

index = int(input())
getArrayByIndex(index)

listArray = ['A','B','C','D','E','F','G','H']
print(listArray[:])
listArray.append('123')
print(listArray[:])
listArray.insert(7,'777')
print(listArray[:])
listArray.extend(['1','2','3','4'])
print(listArray[:])
listArray.remove('777')
print(listArray[:])
listArray.pop()
print(listArray[:])
#list.clear()
#print(list[:])
print('reversed',listArray[::-1])

print(list('파이썬'))
print(tuple('파이썬'))

print(''.join(['가난하다고','외로움을','모르겠는가']))
print(''.join(('가난하다고','외로움을','모르겠는가')))
print('.'.join('가난,하다,고'.split(',')))
print('.'.join(listArray))
print('/'.join(listArray))
print('-'.join(listArray))