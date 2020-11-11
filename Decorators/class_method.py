#create a decorator to check name is similar or not
def decor(method):
    def inner(my_decor):
        if my_decor.name == "faiz":
            print("my name is also faiz!!")
        else:
            return method(my_decor)
    return inner

class myclass:
    def __init__(self,name):
        self.name=name
    @decor
    def myfunc(self):
        print(self.name)

call=myclass("faiz")
call.myfunc()