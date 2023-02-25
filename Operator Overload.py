# Every operator is a method in Python 
# For example a+b represent a.__add__(b) It has different function overload for diff. type of arguments         See line 10
# When we print something a.__str__() is executed . We cant print class ussually but we can overload it too     See line 16

class Student:
    def __init__(self, m1, m2) -> None:
        self.m1 = m1 
        self.m2 = m2 

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __str__(self) -> str:
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(98,84)
s2 = Student(88,95)

s3 = s1 + s2          #to make it run we need to define + operator in our class
print(s3)