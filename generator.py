#It is a easier concept for iterator : It basically gives us a iterator
#Uses: If we have to iterate through a huge database and we create a iterator, our memory will be used, 
# we can prevent it by using generator as it stores and operates one value at a time

def gen():
    i = 1
    while(i <= 10):
        yield i * i     #yeild returns a value so it is similar to return but it does not exit from the function 
        i += 1

val = gen()
for i in val:
    print(i)