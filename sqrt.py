import math

def isRationalNumber(number):
    # 関数を完成させてください
    sqrt_root = math.sqrt(number)
    if sqrt_root % 1 == 0:
        return True
