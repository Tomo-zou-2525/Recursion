import math

def calculateInterestRate (capital):
    annual_interest_rate = 0
    # 関数を完成させてください
    if capital % 2 == 0:
        annual_interest_rate =+ float(0.02)
        print("%2")
        print(annual_interest_rate)
        return annual_interest_rate
    else:
        annual_interest_rate =+ float(0.03)
        print("%3")
        print(annual_interest_rate)
        return annual_interest_rate
    
def calculateGoalMoney(capital,year):
    # 関数を完成させてください
    output = capital * pow(1 + calculateInterestRate(capital), year)
    goal_money = math.floor(output)
    return goal_money

# # 2
# print("anser:2")
# print(calculateGoalMoney(2,3))

# # 25
# print("anser:25")
# print(calculateGoalMoney(16,24))

# 140
print("anser:140")
print(calculateGoalMoney(35,47))