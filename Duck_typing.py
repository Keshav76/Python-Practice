#It means variable overloading or overriding 
a = 5               #a is an int
a = 4.3             #a becomes float
a = 'Keshav'        #a becomes string
a = [1,2,3,4]       #a becomes list         Still No error


class Aadhar:
    def put(self):
        print("I am verified.")

class PAN:
    def put(self):
        print("I am verified. Also I am tax payer")

class Acc:
    def __init__(self,id) -> None:
        id.put()

id = Aadhar()       #id of type Aadhar
A = Acc(id)         #id of type Aadhar can be used as argument for class A constructor as it has method put 
id = PAN()          #id of type PAN
A = Acc(id)         #Here also      No problem; Condition: this type of id does have a put method