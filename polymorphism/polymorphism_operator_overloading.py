class addition():

    def int_addition(self):
        add=2+6
        print("addition of intiger is ",add)

    def str_addition(self ,name, surname):
        self.name=name
        self.surname=surname
        print("addition of string is ",self.name+self.surname)

    def str_addition2(self):
        add2="2"+"6"
        print("addition of string is ",add2)

# Create instance
obj=addition()
# Call the method of int_addition# Call the method of str_addition
obj.int_addition()
# Call the method of str_addition
obj.str_addition("Aadil","Khan")
# Call the method of str_addition2
obj.str_addition2()