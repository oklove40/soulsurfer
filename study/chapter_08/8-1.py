coordinate_1 = {
    'x':5, 'y':3
}
triangle_1 = {
    'type':'triangle'
,   'point_a':{'x':0, 'y':0}
,   'point_b':{'x':0, 'y':3}
,   'point_c':{'x':4, 'y':3}
}

ractangle_1 = {
    'type':'ractangle'
,   'point_a':{'x':2, 'y':2}
,   'point_b':{'x':2, 'y':6}
,   'point_c':{'x':6, 'y':6}
,   'point_d':{'x':6, 'y':2}
}

import math

def square(x):
    return x * x

def distance(pointA, pointB):
    return math.sqrt(
        square(pointA['x'] - pointB['y'])   +
        square(pointA['y'] - pointB['y'])
    )

def circumferenceOfTriangle(shape):
    aToB = distance(shape['point_a'], shape['point_b'])
    bToC = distance(shape['point_b'], shape['point_c'])
    cToA = distance(shape['point_c'], shape['point_a'])

    return aToB + bToC + cToA

def circumferenceOfRactangle(shape):
    aToB = distance(shape['point_a'], shape['point_b'])
    bToC = distance(shape['point_b'], shape['point_c'])
    cToD = distance(shape['point_c'], shape['point_d'])
    dToA = distance(shape['point_d'], shape['point_a'])

    return aToB + bToC + cToD + dToA

# 둘레계산
# print(circumferenceOfTriangle(triangle_1))
# print(circumferenceOfRactangle(ractangle_1))

# 연습문제 8-1 체스말, 바둑돌 정의하기

# 이곳에 체스말 데이터 유형 정의하기
# x, y : 좌표
# color : 색깔
# role : 역할
chess1 = {
  'type': 'chess'
, 'x': 'A'
, 'y': '8'
, 'color': 'black'
, 'role': '룩'
}
chess2 = {
  'type': 'chess'
, 'x': 'E'
, 'y': '1'
, 'color': 'white'
, 'role': '킹'
}

# 이곳에 바둑돌 데이터 유형 정의하기
# x, y : 좌표
# order : 순서
# color : 색깔
baduk1 = {
  'type': 'baduk'
, 'x': 8
, 'y': 14
, 'order': 83
, 'color': '흑'
}
baduk2 = {
  'type': 'baduk'
, 'x': 12
, 'y': 3
, 'order': 84
, 'color': '백'
}

# 둘레 계산 함수를 일반 함수로 정의하기
def circumference(shape):
    if type(shape['type'] == 'triangle'):
        aToB = distance(shape['point_a'], shape['point_b'])
        bToC = distance(shape['point_b'], shape['point_c'])
        cToA = distance(shape['point_c'], shape['point_a'])

        return aToB + bToC + cToA
    elif type(shape['type'] == 'ractangle'):
        aToB = distance(shape['point_a'], shape['point_b'])
        bToC = distance(shape['point_b'], shape['point_c'])
        cToD = distance(shape['point_c'], shape['point_d'])
        dToA = distance(shape['point_d'], shape['point_a'])

        return aToB + bToC + cToD + dToA
    else:
        return None

# print(circumference(triangle_1))
# print(circumference(ractangle_1))

def printPiece(boardGame):
    if boardGame['type'] == 'chess':
        printMsg(boardGame['color'] + ' ' + boardGame['role'] + '이 ' + boardGame['x'] + '' + boardGame['y'] + '위치에 놓여 있습니다.')
    elif boardGame['type'] == 'baduk':
        printMsg('제 ' + str(boardGame['order']) + '수 : ' + boardGame['color'] + '이 (' + str(boardGame['x']) +', '+ str(boardGame['y']) + ') 위치에 두었습니다.')

def printMsg(msg):
    print(msg)

# print(printPiece(chess1))
# print(printPiece(chess2))
# print(printPiece(baduk1))
# print(printPiece(baduk2))

