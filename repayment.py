import math
def howMuchIsYourDebt(year):
    # 関数を完成させてください
    borrowing = 10000
    debts = borrowing * pow(1.2, year) 
    # print(debts)
    # repayment = debts + borrowing
    total = math.ceil(debts)
    return total

# print(howMuchIsYourDebt(2))
print(howMuchIsYourDebt(17))