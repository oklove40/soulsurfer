def weekOfHobby(weather):
    do = ""

    if weather == "r":  #비
        do = "building program at home"
    elif weather == "c":    #구름
        do = "play guitar at rehearsals"
    elif weather == "s":    #해
        do = "im going to skateboard"

    print(do)

    return ""

def weekOfHobbyForTemp(temp):
    do = ""

    if 28 < int(temp):
        do = "on the surfboard"
    elif 28 >= int(temp) and int(temp) > 16:
        do = "ride the cycle"
    elif 16 >= int(temp):
        do = "running"
        
    print(do)

def testRambda(num):
    do = ""

    do = "큼" if 10 > int(num) else "작음"

    print(do)

print("주중에 뭐하지?")
#weather = input()
#weekOfHobby(weather)

print("이 온도에선 뭐하지?")
#temp = input()
#weekOfHobbyForTemp(temp)

print("숫자")
#num = input()
#testRambda(num)

def obesity(height, weight):
    do = ""
    obesityNum = float(weight) / (float(height) * float(height))

    if(float(obesityNum) >= 25):
        do = "비만"
    elif(float(obesityNum) < 25 and float(obesityNum) >= 23):
        do = "과체중"
    elif(float(obesityNum) < 23 and float(obesityNum) >= 18.5):
        do = "정상"
    elif(float(obesityNum) < 18.5):
        do = "저체중"
    else:
        do = "else"

    print(do)

print("키를 입력하세요.(m)")
height = input()
print("몸무게를 입력하세요.(kg)")
weight = input()

obesity(height, weight)
