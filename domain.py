def upperCaseDomain(email):
    return email.split("@")[1].upper()    

# def upperCaseDomain(email):
#     # 関数を完成させてください
#     find_context = email.find("@")
#     print(find_context)

#     serch_context = email[find_context:]
#     print(serch_context)

#     upper_text = serch_context.upper()
#     print(upper_text)

print(upperCaseDomain("www.example@com"))