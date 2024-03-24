# def middleSubstring(string):
#   """
#   文字列 string を受け取り、文字数の半分を文字列の真ん中から返す関数です。

#   Args:
#     string: 入力文字列

#   Returns:
#     文字列の真ん中の部分文字列
#   """
#   length = len(string)
#   if length <= 2:
#     return string
#   mid = length // 2
#   return string[mid - (length % 2) : mid + (length // 2) + (length % 2)]

def middleSubstring(string):
    length = len(string)
    
    if length <= 2:
        return string[0]
    
    middle_index = length // 2
    if length % 2 == 0:  # 文字列の長さが偶数の場合
        return string[middle_index - length // 4:middle_index + length // 4]
    else:  # 文字列の長さが奇数の場合
        return string[middle_index - length // 4:middle_index + length // 4 + 1]

# テスト用例
print(middleSubstring("ABCDEFGHIJKL"))  # 出力結果は "DEFGHI"

# 例
print(middleSubstring("ABCDEFGHIJKL"))  # 出力: DEFGHI
print(middleSubstring("ABCDEFG"))  # 出力: CDEF
print(middleSubstring("ABCDEFG"))  # 出力: CDE
print(middleSubstring("A"))  # 出力: A
print(middleSubstring("AB"))  # 出力: A