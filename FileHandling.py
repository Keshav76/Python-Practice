f = open('D:\Projects\Python\MyFile', 'r')

print(f.readline() , end ='')
a = f.read()         #this will read from 2nd line as file pointer has already shifted to 2nd line by last line of code
f.close()
f1 = open(r'D:\Projects\Python\NewFile', 'w')
f1.write(a)
f1.close()

f = open(r'D:\Projects\Python\img.jpg', 'rb')       #r = read  a for append  w for write    
a = f.read()                                        #rb for read in binary   wb for write in binary
fi = open(r'D:\Projects\Python\NewImg.jpg', 'wb')
fi.write(a)