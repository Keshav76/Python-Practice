#We dont have Abstract classes or methods by default in python
#We import it by a module ABC (Abstract Base Class)


#Abstract Method means a method having no declaration(it is not allowed so use pass)
#Abstract Class means a class having atleast 1 abstract method

#Need of abstract class and method : When we want to neccesarily have a function in a class
#We just inherit it by a class having that (necessary) function as abstract method
#This will make an error if we dont create that function in our sub class
#Thus our neccesity resolved


from abc import abstractmethod, ABC

class Computer(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass


class Laptop(Computer):
    def __init__(self) -> None:
        print("Working")

class Whiteboard(Computer):
    def show(self):
        print("Working")
    
a = Laptop()                       # no error
'b = Whiteboard()'                 # will give error if runned

