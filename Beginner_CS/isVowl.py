# 例題
# 小文字が与えられるので、母音なら true、子音なら false を返す、isVowel という関数を作成してください。
def isVowel(word):
    return word == "a" or word == "i" or word == "u" or word == "e" or word == "o"


# isVowel('a')  # -> true
# isVowel('e') -> true
# isVowel('z') -> false
print(isVowel('a'))
print(isVowel('k'))  # -> false
