# 言語 language を入力として受け取り、選択された言語によって、
# www.example.org のサブディレクトリにリダイレクトする、redirectionUrl という関数を作成します.
# 例えば、この関数では japanese が選択された時、www.example.org/ja を返します。
# また、指定された言語に対応していない場合は、www.example.org/を返します。

def redirectionUrl(language):
    url = "www.example.org/"

    if language == "Japanese":
        url += "ja"
        print(url)


redirectionUrl("Japanese")
