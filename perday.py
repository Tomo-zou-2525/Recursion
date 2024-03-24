import math

def vacationRental(people, day):
    # 宿泊料金の計算
    if day <= 3:
        lodging_rate = 80
    elif day < 10:
        lodging_rate = 60
    else:
        lodging_rate = 50

    # 清掃費の加算
    cleaning_fee = 1.12 * lodging_rate
    total_lodging_cost = people * cleaning_fee
    total_cost_before_tax = (total_lodging_cost * day) * 1.08
    total_cost = math.floor(total_cost_before_tax)

    return total_cost

print(vacationRental(2,3))
print(vacationRental(12,10))