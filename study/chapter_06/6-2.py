def whileTest():
    num = 0
    i = 100

    while i < 10000:
        if (i % 5) == 0:
            num += 5
        i += 1

    print(num)

#whileTest()

def forTest():
    num = 0
    for k in range(100, 10000):
        if (k % 5) == 0:
            num += 5

    print(num)

#forTest()

def maxNum():
    lists = [1,2,3,4,5,6,7,8,9,0]
    num = 0
    for i in lists:
        if i > num:
            num = i

    print(num)

#maxNum()

