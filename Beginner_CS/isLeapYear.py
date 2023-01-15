def isLeapYear(year):
    # 関数を完成させてください
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        return True
    else:
        return False


print(isLeapYear(2000))
print(isLeapYear(2011))
