#call privet method publicly to check what error we get
class private1:
    __rahul="Rahul have a private data "


    def base1(self):     
        print(self.__rahul)

#create object of class private and call the function of base1
obj=private1()
obj.base1()


print(private1.__rahul)   #so we can not access the privet class publicly 