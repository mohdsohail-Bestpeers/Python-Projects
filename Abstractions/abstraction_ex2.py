from abc import *


class KKR_Team(ABC):
    def Morgan(self):
        pass
    
    def Rusle(self):
        print("Aprox Total Run in IPL 2020 :  50")
  
class MI_Team(KKR_Team):

    def Rohit(self):
        print("Aprox Total Run in IPL 2020 :  200")


obj=MI_Team()
obj.Rusle()
obj.Rohit()