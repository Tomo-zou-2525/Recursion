# def canProcessOrder(beef, chicken, salad, coffee, tea):
#     # 関数を完成させてください
#     if beef == True and chicken == False or beef == False or chicken == True and coffee == True and tea == False or coffee == False and tea == True:
#         return True
#     else:
#         return False

def canProcessOrder(beef, chicken, salad, coffee, tea):
    # 関数を完成させてください
    if beef == True and chicken == False:
        return True
    elif beef == False or chicken == True:
        return True
    elif coffee == True and tea == False:
        return True
    elif coffee == False and tea == True:
        return True
    else:
        return False


print("--False--")
print(canProcessOrder(False, False, True, False, True))  # -> False
print("--True--")
print(canProcessOrder(False, True, True, False, True))  # -> True
print("")
print(canProcessOrder(False, False, True, False, True))  # ->
print("")
print(canProcessOrder(False, False, True, False, True))  # ->
print("")
print(canProcessOrder(False, False, True, False, True))  # ->
