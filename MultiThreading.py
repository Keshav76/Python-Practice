from threading import *
from time import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.5)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.5)

ob1 = Hello()
ob2 = Hi()

ob1.start()         #We use start instead  of run function
sleep(1)          #0.1 sec delay so that they dont get sync
ob2.start()

ob1.join()          #waiting for ob1 thread to join ; then only further execution
ob2.join()

print("Bye")        #after Both thread join then only this will execute
