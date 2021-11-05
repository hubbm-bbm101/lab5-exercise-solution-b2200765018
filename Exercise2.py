def check() :
    mail = input("Write your mail : ")
    if "@" in mail and "." in mail :
        return True
    else :
        return False

print(check())


