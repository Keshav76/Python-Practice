#Defalut One

vals = [1,2,3,4,5,6]
it = iter(vals)             #creating an iterator by iter function
a = next(it)                #going to next value and returning current value(i.e. vals[0])    a will get 1
b = next(it)                #repeating same thing                                             b will get 2


#Self Created (By using Class)     doing for same result i.e. 1-6

class values:
    def __init__(self):         #Setting default value of iterator it at start as 1
        self.it = 1

    def __iter__(self):         #These function need not to be called ; But we can call it          Can also be accessed as iter(a)
        return self
    
    def __next__(self):         #Same as above      Can also be accesed as next()
        if self.it > 6:
            raise StopIteration
        else:
            val = self.it
            self.it += 1
            return val

ob = values()

print('Outside : ', ob.__next__())
print('Outside : ', next(ob))              #Both Works

for i in ob:            #iterable starts from where we left
    print('Inside : ', i) 



# Infact for loop even does the same thing; Creates an iterable