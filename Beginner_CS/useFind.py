# 例題 1
# recursion@info.com の @ のインデックスの位置
email = "recursion@info.com"

# 出力
print(email.find('@')) #9

# 例題 2
# 変数 atLocation
atLocation = email.find('@')
print(atLocation) #9
print(atLocation+1) #10
print(len(email)) #18

# recursion@info.com の @ より後ろを切り取り
domain = email[atLocation+1:len(email)]
print(domain) # info.com
