#how we can modifiy the privet veriable which is inside the class

class Employee:
    __empid=10

    def A(self,emp):
        self.__empid=emp
    

    def B(self):
        print(self.__empid)
        
obj=Employee()
obj.A(11)
obj.B()