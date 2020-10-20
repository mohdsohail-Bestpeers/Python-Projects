
#hierarchiacal inheritance with super()

class Boss():
    def __init__(self):
        print("this is Boss class")

class HumanResource(Boss):
    def __init__(self):
        super().__init__()
        print("this is humanresource class")

class Employee(Boss):
    def __init__(self):
        super().__init__()
        print("this is employee class")
    
#create object of HumanResource
obj=HumanResource()
print('-'*30)
#create object of HumanResource
obj1=Employee()