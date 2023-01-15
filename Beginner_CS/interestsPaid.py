# 支払い方法としてローンを選択すると利子が元の金額に上乗せされます。
# 期日までに払われた場合、利子は 2% で、払われなかった場合、利子は 15% になります。
# また、どちらの場合でも手数料は $2.5 かかります。
# ローンの金額 initialLoan、期日までに払われたかどうかをブーリアンで表した
# didPayOnTime を入力として受け取り、合計金額を返す interestsPaid という関数を作成してください。

def interestsPaid(initailLoan, didPayOnTime):
    if didPayOnTime == True:
        initailLoan = 2.5 + initailLoan * 1.02
    else:
        initailLoan = 2.5 + initailLoan * 1.15
    print(initailLoan)
    return initailLoan  # 合計金額


interestsPaid(100, True)  # 104.5
interestsPaid(100, False)  # 117.5
