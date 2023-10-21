from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Received message:" + message.decode())
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

#use UDP section in SOCKETTEST for client not the normal one

    #difference between TCP and UDP is that TCP is connection oriented and UDP is connectionless which means that TCP is reliable and UDP is not reliable and TCP is slower than UDP
    #use udp when you don't need to make sure that the message is received and use tcp when you need to make sure that the message is received