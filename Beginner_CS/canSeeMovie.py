def canSeeMovie(age):
    if age >= 13:
        return True
    else:
        return False


# 関数の呼び出しをコンソールに出力します
print(canSeeMovie(20))
print(canSeeMovie(10))

# 例題
# 年齢 age が 20 未満の場合、False を返し、20 歳以上なら True を返す、canDrinkSake という関数を作成してください
# 関数に 21 を入力して、print で出力してください (True)
# 関数に 8 を入力して、print で出力してください (False)


def canDrinkSake(age):
    if age >= 20:
        return True
    else:
        return False


# 関数の呼び出しをコンソールに出力します
print(canDrinkSake(21))
print(canDrinkSake(8))
