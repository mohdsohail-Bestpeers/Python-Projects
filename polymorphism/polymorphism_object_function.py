class Cat():
    def age(self):
        print("Cat leves between 1 to 25")

    def eat(self):
        print("Cat eat Fish")

class Elephant():
    def age(self):
        print("Elephant leves between 1 to 70")

    def eat(self):
        print("Elephant eat Sugarcane")


def func(obj):
    obj.age()
    obj.eat()


obj_Cat=Cat()
obj_Elephant=Elephant()

func(obj_Cat)
func(obj_Elephant)
