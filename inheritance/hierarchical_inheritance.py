#hierarchical inheritance

class parent1():
    def function1(self):
        print("this is parent class")

class child1(parent1):
    def function2(self):
        print("this is first child class ")

class child2(parent1):
    def function3(self):
        print("this is secound child class")

#create object of child1
obj=child1()
obj.function1()
obj.function2()
print("-"*50)

#create object of child2
obj2=child2()
obj2.function1()
obj2.function3()
