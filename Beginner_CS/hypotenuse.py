# 数学ライブラリ（名前空間）をロードします
# mathライブラリの中の関数を自由に使うことができます
import math
 
# 小数点以下切り捨て
print(math.floor(3.3))
print(math.floor(10.9))
 
# 小数点以下切り上げ
print(math.ceil(3.3))
print(math.ceil(10.9))
 
# 累乗を計算することができる pow 関数
# 3^4 を計算 (3 * 3 * 3 * 3)
print(math.pow(3,4))
 
# 2^5 を計算 (2 * 2 * 2 * 2 * 2)
print(math.pow(2,5))
 
# √2 を計算
print(math.sqrt(2))

# ライブラリと関数を組み合わせます
def pythagoreanTheorem(a,b):
# sqrt 関数 (平方根を計算する関数)
    return math.sqrt(a*a + b*b) 

# (3^2 + 4^2) の平方根を出力 (√25)
print(pythagoreanTheorem(3,4))

# (3^2 + 10^2) の平方根を出力 (√109)
print(pythagoreanTheorem(3,10))
 
# 例題 1
# 式　3 * 4 / 5 の結果に対して小数点以下の切り捨てを行い、出力してください (2)
print("---")
print(3 * 4 / 5)
print(5 / 3 * 4)
print(math.ceil(3 * 4 / 5))
# 式 3 * 4 / 5 の結果に対して小数点以下の切り上げを行い、出力してください (3)
print(math.floor(3 * 4 / 5))
# 例題 2
# 直角三角形において、横、縦の長さを受け取って、斜辺の長さを返す、hypotenuse という関数を sqrt 関数を使って、定義してください
# 横 4、高さ 3 を関数に入力して、コンソールに結果を出力してください (5.0)
def hypotenuse(weight, height):
    print(math.sqrt(weight ** 2 + height ** 2))
 
hypotenuse(4,3)

# 例題 3
# ある整数を受け取って、2^x を計算する、exponentialOfTwo という関数を pow 関数を使って作成してください
# 3 を関数に入力して、コンソールに結果を出力してください (8.0)
# 10 を関数に入力して、コンソールに結果を出力してください (1024.0)
def exponentialfOfTwo(val):
    print(math.pow(2,val))

exponentialfOfTwo(3)
exponentialfOfTwo(10)
