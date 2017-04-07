# UDP Client

from socket import *

serverName = "192.168.1.69"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input ("Input lowercase sentence: ")

clientSocket.sendto(message.encode(), (serverName,serverPort))

modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

print ("Received from server: ", modifiedMessage.decode())

clientSocket.close()
