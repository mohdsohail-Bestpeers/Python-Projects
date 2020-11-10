
def decor(num):
    def inner():
        print("this is before exicution")
        num()
        print("this is after exicution")
    return inner

@decor
def num():
    print("this is enhance code")
num()
