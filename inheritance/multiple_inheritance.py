#Multiple inheritance:

class parent1():
    def function1(self):
        print("this is parent class")

class parent2():
    def function2(self):
        print("this is secound parent class ")

class child(parent1,parent2):
    def function3(self):
        print("this is secound child class")

#create Object
obj=child()
obj.function1()
obj.function2()
obj.function3()

