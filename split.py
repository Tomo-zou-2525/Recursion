def isSubstring(s1,s2):
    is_text = s1.find(s2)
    print(is_text)
    if is_text != -1:
        return print(True)
    else:
        return print(False)

s1 = ("""Unko
# Tinko
# Anko""")    

s2 = ("Unko")

isSubstring(s1,s2)

# def split_blank(text,text2):
#     split_text = text.split("\n")
#     for x in split_text:
#         print(x,text2)
#         if x == text2:
#             return True
#         else:
#             return False
#     return split_text

# input_text = ("""Unko
# Tinko
# Anko""")

# print(split_blank(input_text, "Unko"))

# def isSubstring(s1,s2):
#     # 関数を完成させてください
#     split_text = s1.split("\n")
#     for paragraph in split_text:
#         if paragraph == s2:
#             return True
#         else:
#             return False
#     return split_text

# s1 = ("""Unko
# Tinko
# Anko""")

# s2 = ("Unko")

# print(isSubstring(s1,s2))

# # 検索対象の文字列
# text = "The quick brown fox jumps over the lazy dog."
 
# # foxを検索
# # index = text.find("fox")
# index = text.find("Unko")
# if index != -1:
#     print("found at", index)
# else:
#     print("not found", index)

