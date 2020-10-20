# multi-level inheritance with super()

class shahruk():
    def __init__(self):
        print("shahruk teach Maths subject ")

class sanjay(shahruk):
    def __init__(self):
        super().__init__()
        print("sanjay teach English subject")

class student(sanjay):
    def __init__(self):
        super().__init__()
        print("student study English and Maths both")

#create object
obj=student()