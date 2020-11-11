class decor:
    def __init__(self,func):
        self.func=func

    def __call__(self, *args,**kwargs):
        if args[1]==0:
            return "you cant devide by 0 please change the value"
        else:
            self.func(*args,**kwargs)
@decor
def division(a,b):
    return a/b

print(division(10,0))


