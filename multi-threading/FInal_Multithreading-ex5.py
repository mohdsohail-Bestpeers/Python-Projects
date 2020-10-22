from threading import *

class processor1(Thread):
    def run(self):
        for i in range(10):
            print("the is processor 1")


class processor2(Thread):
    def run(self):
        for i in range(10):
            print("this is processor 2")

#if we call start() then we get acurate result  
obj=processor1()
obj1=processor2()
obj.start()
obj1.start()
print("main thread")