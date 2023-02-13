from asyncio import format_helpers


# def canProcessOrder(beef, chicken, salad, coffee, tea):
#     # 関数を完成させてください
#     if beef == True or chicken == False and salad == True or salad == False:
#         return True
#     elif beef == False or chicken == True:
#         return True
#     elif beef == True and chicken == True:
#         return False
#     elif coffee == True or tea == False:
#         return True
#     elif coffee == False or tea == True:
#         return True
#     elif coffee == True and tea == True:
#         return False
#     else:
#         return False

# def canProcessOrder(beef, chicken, salad, coffee, tea):
#     # 関数を完成させてください
#     if beef == True or chicken == False and salad == True or salad == False and beef == False or chicken == True and beef == True or chicken == True and coffee == True or tea == False and coffee == False or tea == True and coffee == True and tea == True:
#         return True
#     else:
#         return False

# def canProcessOrder(beef, chicken, salad, coffee, tea):
#     return True if beef + chicken == 1 and coffee + tea == 1 else False

def canProcessOrder(beef, chicken, salad, coffee, tea):
    return beef ^ chicken and coffee ^ tea


# def canProcessOrder(B, C, S, O, T): - which(B, C), nor(S, S), which(O, T).


# which(X, Y): - X \== Y.
# nor(X, X): - X == X.


print(canProcessOrder(False, False, True, False, True))

print(canProcessOrder(False, False, True, False, True))  # --> False

print(canProcessOrder(False, True, True, False, True))  # --> True

print(canProcessOrder(True, True, True, False, True))  # --> False

print(canProcessOrder(True, False, True, True, True))  # --> False

print(canProcessOrder(True, False, False, False, False))  # --> False

print(canProcessOrder(False, True, False, False, True))  # --> true
