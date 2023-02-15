from itertools import count


# def rollingDice(countA, countB):
#     for i in range(countA):
#         judge = 6 * countA
#         if 0 < countB < judge:
#             print("うんこ")


# rollingDice(10, 61)
def rollingDice():
    A, B = map(int, input().split())
    print(A)
    print("---")
    print(B)
    if B <= A*6 and B >= A:
        print('Yes')
    else:
        print('No')


rollingDice()
