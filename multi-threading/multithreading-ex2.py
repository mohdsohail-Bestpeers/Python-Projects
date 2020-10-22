#here i will use time module for get the acurate result
from time import sleep
from threading import *

class processor1(Thread):
    def run(self):
        for i in range(10):
            print("the is processor 1")
            sleep(2)


class processor2(Thread):
    def run(self):
        for i in range(10):
            print("this is processor 2")
            sleep(2)

 #even it is excuting first class and then secound class 
obj=processor1()
obj1=processor2()
obj.run()
obj1.run()