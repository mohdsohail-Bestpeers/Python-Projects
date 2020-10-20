#Hybride Inheritance

class parent1():
    def function1(self):
        print("this is parent class")

class child1(parent1):
    def function2(self):
        print("this is first child class ")

class child2(parent1):
    def function3(self):
        print("this is secound child class")

class child3(child2):
    '''here i inherit only class child2 becouse child2 have class parent1. 
    thats way dont need to inherit parent1 in child3'''    
    def function4(self):
        print("this is third child class")

#create object
obj=child1()
obj.function1()
obj.function2()
print("-"*50)

obj1=child2()
obj1.function1()
obj1.function3()
print("-"*50)

obj2=child3()
obj2.function1()
obj.function2()
obj2.function3()
obj2.function4()