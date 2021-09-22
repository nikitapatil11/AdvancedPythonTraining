import socket

msgfromclient = "hello udp server"

bytesTosend = str.encode(msgfromclient)

serverAddressPort = ('127.0.0.1', 20001)

buffersize = 1024

UPDCLIENTSOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UPDCLIENTSOCKET.sendto(bytesTosend, serverAddressPort)

msgfromserver = UPDCLIENTSOCKET.recvfrom(buffersize)

msg = "message from server{}".format(msgfromclient[0])

print(msg)

