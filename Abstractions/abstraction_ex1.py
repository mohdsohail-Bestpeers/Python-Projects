from abc import ABC,abstractmethod

class boss(ABC):
    @abstractmethod
    def work(self):   #this is abstract class
        pass
   
    def home(self):
        print("some boss leaves in banglore")

class employee(boss):
    def work(self): 
        print("this is employe class")




obj=employee()
obj.work()
obj.home()

