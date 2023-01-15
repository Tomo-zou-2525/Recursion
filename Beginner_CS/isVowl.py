# 例題
# 小文字が与えられるので、母音なら true、子音なら false を返す、isVowel という関数を作成してください。
def isVowel(word):
    if word == "a" or "i" or "u" or "e" or "o":
        print(word)
        return print("true")
    else:
        print("false")


# isVowel('a')  # -> true
# isVowel('e') -> true
# isVowel('z') -> false
isVowel('k')  # -> false
