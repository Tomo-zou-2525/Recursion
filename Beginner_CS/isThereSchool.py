from unittest import removeResult


def isThereSchool(day, isHoliday):
    # 関数を完成させてください
    if day == "Sunday" or day == "Saturday" or isHoliday == True:
        return False
    else:
        return True


print(isThereSchool("Sunday", True))
print(isThereSchool("Monday", True))
print(isThereSchool("Monday", False))
print(isThereSchool("Unko", False))
print(isThereSchool("Unko", True))
