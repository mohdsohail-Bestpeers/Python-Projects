#Basic example of inheritance:

#Single inheritance:
class parent():
    def func1(self):
        print("this is my parent class")

class child(parent):
    def func2(self):
        print("this is my child class")


print("-"*50)
#create object
obj=child()
obj.func1()
obj.func2()
print("-"*50)





