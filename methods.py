class Student:
    School = "ACA"
    def __init__(self):         #instance method ( Use Instance Variables )
        self.a = 2
        self.b = 3

    @classmethod                #class method    ( Use Class Variables ): We need to add '@classmethod'
    def change_school(cls,value):
        cls.School = value

    @staticmethod               #static method   (Use No Variable)
    def Say_hello():
        print("Hello")


s1 = Student()
 
Student.Say_hello()

print(s1.a, s1.b, s1.School)

Student.change_school('SAS')

print(s1.a, s1.b, s1.School)