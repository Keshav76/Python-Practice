from socket import *
s = socket()                        #it makes s a node
print("Socket Created")
s.bind(('localhost', 9999))         #it setups a socket or port in pc at port no 9999
s.listen(3)                         #it makes it server
print("Waiting for connections.")   

while True:
    c,ad = s.accept()               #it accepts connection from clients
    name = c.recv(1024).decode()    #it recieve msg frmo c and stores it in name after decoding it
    print("Connection Established with ", ad, name)
    c.send(bytes("Welcome to Server.", 'utf-8'))    #it sends msg to c
    c.close()                       #connection breaked