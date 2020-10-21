class Project_manager():
    def work(self,name):
        self.name=name
        print(self.name,"is Project Manager of Bestpeers")

class Empolyee(Project_manager):
    def work(self,name):
        self.name=name
        print(self.name,"is Empolyee of Bestpeers")


class humanresource(Empolyee):       
    def work(self,name):
        self.name=name
        print(self.name,"is a  HR of Bestpeers")

#create the method
HR=humanresource()
# Call the method 
HR.work("Priya")
'''Em=Empolyee()
Em.work("Zek")'''