#Hybride inheritance with super()

class rahul():
    def __init__(self):
        print("rahul is a principle of school ")

class sanjay(rahul):
    def __init__(self):
        super().__init__()
        print("sanjay teach English subject")

class salman(rahul):
    def __init__(self):
        super().__init__()
        print("salman teach maths subject")

class student(salman):
    def __init__(self):
        super().__init__()
        print("student study only Maths subject")

#create object of student
obj=student()