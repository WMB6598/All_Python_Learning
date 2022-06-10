import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#this doesnt make the connection, is more like a file handle
mysock.connect (('data.pr4e.org', 80))#This connects the socket across the internet
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n' .encode() # this prepares the statement to get sent to the server
mysock.send(cmd)

while True :
    data = mysock.recv(512) # Receives 512 characters at a Time
    if (len(data) < 1) :
        break
    print(data.decode())#This is the opposite of the encode function we used earlier
mysock.close()