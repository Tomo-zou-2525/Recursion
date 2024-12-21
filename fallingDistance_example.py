import math

# 各惑星の重力加速度 [m/s^2]
GRAVITY = {
    "Earth": 9.80665,
    "Jupiter": 24.79,
    "Neptune": 11.15,
    "Pluto": 0.0
}

# メートルをマイルに変換する関数
def meter_to_mile(meter):
    return meter * 0.000621371

# 落下距離を計算する関数
def falling_distance(planet, time):
    g = GRAVITY.get(planet, 0)  # 惑星の重力加速度を取得（デフォルトは0）
    h_meter = 0.5 * g * (time ** 2)  # 落下距離[m]を計算
    h_mile = meter_to_mile(h_meter)  # 距離をマイルに変換
    return math.floor(h_mile)  # 結果を切り捨て

# テスト
print(falling_distance("Earth", 5000))  # 76117 を期待
