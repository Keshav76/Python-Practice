class Car:
    wheels = 4              #Class Variable
    def __init__(self) -> None:
        self.Colour = 'White'       #Instance Variables
        self.Looks = 'Super'        #Instance Variables
    

c1 = Car()
c2 = Car()

c1.Colour = 'Blue'
c1.Looks = 'Bad'
c1.wheels = 5         # Not Recomended   It creates an instance variable


print(c1.Colour, c1.Looks, c1.wheels)
print(c2.Colour,c2.Looks,c2.wheels)