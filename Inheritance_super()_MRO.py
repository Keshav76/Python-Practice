class A:
    def f1(self):
        print("a-1")
    def f2(self):
        print("a-2")

class B:
    def f1(self):
        print("b-1")
    def f2(self):
        print("b-2")

class C(A,B):   	        #Talking about order of (... , ...) i.e. (A,B) or (B,A)
    def f2(self):
        super().f1()        # also calls f1 of super class : Priority of choosing f1 Left to Right  
        print("C-2")
    def f3(self):
        print("C- 3")

ob = C()
ob.f1()         #f1 of sub class; If not available f1 of class derived  with priority from left to right   o/p a-1
ob.f2()         #f2 of sub class; If not available f1 of class derived  with priority from left to right   o/p C-2
ob.f3()         #f3 of sub class; If not available f1 of class derived  with priority from left to right   o/p C-3


''' This concept is called Method Resolution Order(MRO)
    This prefers sub class first then super class in order left to right'''

