#lets take join() for the acurate result
from time import sleep
from threading import *

class processor1(Thread):
    def run(self):
        for i in range(10):
            print("this is processor 1")
            sleep(2)


class processor2(Thread):
    def run(self):
        for i in range(10):
            print("this is processor 2")
            sleep(2)

 #Now its giving acurate result 
obj=processor1()
obj1=processor2()
sleep(0.2)
obj.start()
obj1.start()

obj.join()
obj1.join()
print("we got acurate result")