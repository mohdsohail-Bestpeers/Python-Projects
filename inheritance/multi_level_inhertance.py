#Multi-level Inheritance :

class parent():
    def function1(self):
        print("this is parent class")

class child1(parent):
    def function2(self):
        print("this is first child class ")

class child2(child1):
    def function3(self):
        print("this is secound child class")

#create object
obj=child1()
obj.function1()
obj.function2()
print("-"*50)
obj1=child2()
obj1.function1()
obj1.function2()
obj1.function3()
