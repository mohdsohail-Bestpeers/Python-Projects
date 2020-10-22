#call privet method using pulic method 

class calling_private:

    def __private_method(self):
        print("this is private method ")

    def public_method(self):
        print("this is public method")
        self.__private_method()

#create a object
obj=calling_private()
#call the public_method and we will get both method data becouse public_method using a private_method
obj.public_method()

#obj.__private_method()    #this is not correct 
