class Student:
    def __init__(self, name, qualification):
        self.name=name
        self.qualification=qualification

    def Info(self):
        print("Hello my name is" ,self.name ,"and i am the student of ", self.qualification ,"standerd")

class Teacher:
    def __init__(self, name, qualification):
        self.name=name
        self.qualification=qualification

    def Info(self):
        print("Hello i am a Teacher of 10th standerd, My name is ",self.name, "and i am " ,self.qualification )

s=Student("Raz",10)
t=Teacher("Rahul","Graduate")
for school in (s,t):
    school.Info()
