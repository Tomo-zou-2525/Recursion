from itertools import count


def rollingDice(countA, countB):
    for i in range(countA):
        judge = 6 * countA
        if 0 < countB < judge:
            print("うんこ")


rollingDice(10, 61)
