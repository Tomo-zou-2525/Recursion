# # import math
# # def vacationRental(people,day):
# #     if day <= 3:
# #         lodgingDay = day * 80
# #         print(lodgingDay)
# #     elif day < 5:
# #         lodgingDay = day * 60
# #         print(lodgingDay)
# #     elif day >= 10:
# #         lodgingDay = day * 50
# #         print(lodgingDay)
# #     addclearnpay = lodgingDay * 1.12
# #     addtax = addclearnpay * 1.08
# #     totalcost = people * addtax
# #     # print(totalcost)
# #     # print(type(totalcost))
# #     totalcostfix = math.floor(totalcost)
# #     return totalcostfix

# # print(vacationRental(1,10))

# import math
# def vacationRental(people,day):
#     if day < 3:
#         lodgingDay = day * 80
#     elif day < 5:
#         lodgingDay = day * 60
#     elif day >= 10:
#         lodgingDay = day * 50
#     addcleanpay = lodgingDay * 1.12
#     addtax = addcleanpay * 1.08
#     totalcost = math.floor(addtax)
#     return totalcost


# print(vacationRental(2,3))

import math
def vacationRental(people,day):
    if day < 3:
        lodgingDay = day * 80
        print(people,lodgingDay)
        return lodgingDay
    elif day < 5:
        lodgingDay = day * 60
        print(people,lodgingDay)
        return lodgingDay
    elif day >= 10:
        lodgingDay = day * 50
        print(people,lodgingDay)
        return lodgingDay
    print(lodgingDay)
    addcleanpay = lodgingDay * 1.12
    addtax = people * addcleanpay * 1.08
    totalcost = math.floor(addtax)
    return totalcost

print(vacationRental(2,3))
print(vacationRental(12,33))
print(vacationRental(42,1))
# print(vacationRental(1,5))
# print(vacationRental(1,15))