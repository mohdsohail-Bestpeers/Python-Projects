import functools

def decor(func):
    @functools.wraps(func)
    def inner():
        str1=func()
        return str1.upper()
    return inner

@decor
def wish():
    return"Happy birthday"
print(wish.__name__)