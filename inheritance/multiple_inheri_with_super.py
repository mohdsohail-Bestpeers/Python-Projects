#multiple inheritance with super()

class base:
    def __init__(self):
        print("this is base class")

class child1():
    def __init__(self):
        super().__init__()
        print("this is from child1 class")
     
class child2(child1,base):
    def __init__(self):
        super().__init__()
        print("this is from child2 class")

#create object
a1=child2()