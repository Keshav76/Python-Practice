# WE DONT HAVE OVERLOADING IN PYTHON
# We use some tricks to make overloaded functions
def sum(a = None, b = None, c = None):
    if a!= None and b!= None and c!= None:
        return a + b + c
    elif a!= None and b!= None:
        return a + b
    else:
        return a

print(sum(45,42,56))
print(sum(75,23))
print(sum(56))

#All 3 works

