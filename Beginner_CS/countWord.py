def countWord(word):
    if len(word) == 0:
        return -1
    else:
        return len(word)

# def countWord(word):
#    if word == "": return -1
#    else: return len(word)


print(countWord("Hello"))
print(countWord("Good Morning"))
print(countWord(""))
