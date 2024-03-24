# def insertUnderscoreAt(s, i):
#     if i >= len(s):  # iが文字列の長さ以上の場合、文字列をそのまま返す
#         return s
#     else:
#         return s[:i] + '_' + s[i:]  # i番目の位置にアンダースコアを挿入して文字列を返す

# # テスト用例
# s = "example"
# i = 3
# result = insertUnderscoreAt(s, i)
# print(result)  # 出力結果は "exa_mple" となる

print("-----------------------------------")

# def lastFourHint(stringInput):
#     # 関数を完成させてください
#     if stringInput > 5:
#         return "There is no Hint"
#     else:
#         return print("Hint is" + [4:stringInput])````

def lastSixHint(stringInput):
    if len(stringInput) < 6:
        return "There is no Hint"
    else:
        return "Hint is:" + stringInput[4:]
    
print(lastSixHint("Sky is the blue      "))
print(lastSixHint("unko"))