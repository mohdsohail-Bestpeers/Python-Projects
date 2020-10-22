#can acess privet variable in class indirectly using method 

class Employee:
    __empid=10

    def A(self,emp):
        self.__empid=emp
    

    def B(self):
        print(self.__empid)
        


obj=Employee()
obj.B()