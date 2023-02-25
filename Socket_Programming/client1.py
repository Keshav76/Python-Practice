from socket import*
c = socket()                    #it makes c a socket
name = input("Enter your name: ")
c.connect(('localhost',9999))   #it connects with port number 9999
c.send(bytes(name, 'utf-8'))    #it sends to connected port
res = c.recv(1024).decode()     #it recieves data from server
print(res)