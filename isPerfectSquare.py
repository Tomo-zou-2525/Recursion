import math

def isPerfectSquare(x,y):
    # 関数を完成させてください
    return distance(x,y)

def hadDecimal(v):
    if v % 1 == 0:
        return True
    else:
        return False

def distance(x,y):
    val = x ** 2 + y ** 2
    # print(val)
    val2 = math.sqrt(val)
    # print(val2)
    return hadDecimal(val2)

print(isPerfectSquare(7,24))