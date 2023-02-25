from functools import reduce


class Student:
    # Class 

    School = 'St. Anthony School '
     
    def __init__(self, Name, Class, Marks):
        self.Name = Name
        self.Class = Class
        self.Marks = Marks
        self.Grade = reduce(lambda a, b: a + b, self.Marks) / len(Marks)

    def output(self):
        print("School : ", self.School)
        print("Name : ", self.Name)
        print("Class : ", self.Class)
        print("Marks : ", self.Marks)
        print("Grade : ", self.Grade)

    def compare(self, other):
        if self.Class == other.Class and self.Name == other.Name:
            print("They are Same.")
        else:
            print("They are different.")


Name = input("Enter your Name : ")
Class = input("Enter your Class : ")
Marks = [int(i) for i in input("Enter marks in all subject with a gap in b/w : \n").split()]
com1 = Student(Name,Class,Marks)

com1.output()

com2 = Student('Gauri', Marks= [98,95,87,96], Class = '9th A')

print("Other Data : ")
com2.output()

print("Now comparing with given data :  ")
com1.compare(com2)

