# UDP Server

from socket import *
serverPort = 12000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))

print ("The UDP server is ready to recieve")

while True:
    # Read clients message and remember client's address (IP and Port)
    message, clientAdress = serverSocket.recvfrom(2048)

    # Print message and client adress
    print (message.decode())
    print (clientAdress)

    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAdress)
