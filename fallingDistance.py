# 重力加速度 g[m/s2] で、高さ h[m] から物体をそっと落下させ、地上に到達するまで t 秒を要するとき、h = 1/2 gt2 が成り立つとします。惑星 planet、落下時間 time[s] が与えられるので、落下距離[mile]を返す、fallingDistance という関数を作成してください。各惑星の重力加速度は以下の表を参考にしてください。

import math

def planetGravityMpss(planet):
    if planet == "Earth":
        return 9.8
    if planet == "Jupiter":
        return 24.79
    if planet == "Mercury":
        return 3.7
    if planet == "Pluto":
        return 0
    return 0

def meterTomile(meter):
    print(meter)
    return meter * 0.000621371

def fallingDistance(planet,time):
    meter = 0.5 * (planetGravityMpss(planet) * (time ** 2)) 
    mile = meterTomile(meter)
    return math.floor(mile)

# print(planetGravityMpss("Earth") * 5000)

print(fallingDistance("Earth",5000))

# print("meterTomile")
# print(meterTomile(5000))

# print("Earth")
# print(planetGravityMpss("Earth"))

# print("calclation result")
# print(meterTomile(5000) * planetGravityMpss("Earth"))

# print(planetGravityMpss("Earth") ** 2)

# print(planetGravityMpss("Earth") * planetGravityMpss("Earth"))

# print("-------------")

# print((planetGravityMpss("Earth") * meterTomile(5000)) ** 2)