from operator import *

def smart(func):
    def inner(a,b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner


diff = smart(sub)
div = smart(truediv)

print(diff(3,5))
print(div(2,4))
