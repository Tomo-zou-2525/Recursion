# 文字列の長さが 5 より大きいかどうかチェックします
def isLongerThan5(s):
    # s.length で文字列の長さを取得します
    textlength = len(s)
    print(textlength)
    # 2 で割ったときの余りが 1 かどうかチェックします
    return textlength % 6 == 0
    # return len(s) > 5


print(isLongerThan5("abcdef"))
print(isLongerThan5("abcde"))
