#getting problem in this code. class processor1 or class processor2 is not working simultaneously
#it is excuting class processor1 first then after first thread exicution complete then class processor2 exicute

from threading import *

class processor1(Thread):
    def run(self):
        for i in range(10):
            print("the is processor 1")


class processor2(Thread):
    def run(self):
        for i in range(10):
            print("this is processor 2")

#here by this program we are getting first processor1 output and then processor2 become exicute 
obj=processor1()
obj1=processor2()
obj.run()
obj1.run()
print("main thread")