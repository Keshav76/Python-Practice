a = 23
b = 2           #change it to zero and you will get ZeroDivisionError



try:                                           #it tries to execute everything in its block
    print('File open')
    print(a/b)
    k = int(input("Enter a number : "))
    print(k)


except ZeroDivisionError as e:                 #if exception of type ZeroDivisionError is found, this block is executed
    print("Can't divide by zero.")
except ValueError as e:                        #if exception of type Value error is found, this block is executed
    print("Wrong Input")
except Exception as e:                         #if some other exception, this block is executed
    print("Something Went Wrong. Error: ", e)


finally:                                       #this block is executed wether exception is found or not
    print("File Close")