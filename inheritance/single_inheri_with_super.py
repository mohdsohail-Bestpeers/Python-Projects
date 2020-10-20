#Single inheritance with super()

class Bird(object):
    def __init__(self):
        print("Bird")

    def Activity(self):
        print("This is bird which can not swim")

class Animal(Bird):
    def __init__(self):
        super().__init__()
        super().Activity()
        print("Animal")

    def Activity(self):
        print("THis is animal which can swim")

#create object
a1 = Animal()
a1.Activity()


