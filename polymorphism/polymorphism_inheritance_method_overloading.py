class Person:
    def person_name(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# Create instance
obj = Person()
# Call the method without parameter
obj.person_name()
# Call the method with a parameter
obj.person_name('Rohan')

