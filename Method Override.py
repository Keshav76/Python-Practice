#Same concept as MRO => Method Resolution Order
class A: 
    def f1(self):
        print("A-1")

    def f2(self):
        print("A-2")


class B(A):
    def f1(self):
        print("B-1")


ob = B()
ob.f1()         #f1 of A is overridden by f1 of B
ob.f2()         #no overriding