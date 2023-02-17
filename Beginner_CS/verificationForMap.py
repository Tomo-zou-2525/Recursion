# map(callable. *iterable)
# List(配列)の各要素毎に処理をしたい場合に使用する関数の種類
# 戻り値はmapオブジェクト
# イテレータの一種（forループで回せるやつ）

a = [100, 200, 300]
# next(a) <- エラー！
print(next(a))
a_iter = iter(a)
print(next(a_iter))  # 100が取り出される
print(a_iter)
