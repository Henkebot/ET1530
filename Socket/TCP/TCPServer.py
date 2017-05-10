# TCP Server
from socket import *
serverPort = 12000

# Create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))

# Server starts listening for incoming TCP requests
serverSocket.listen(1)

print("The TCP server is ready to receive")

while True:
    # Server waits for incoming requests; new socket created on return
    connectionSocket, addr = serverSocket.accept()
    
    sentence = connectionSocket.recv(1024).decode()

    print (sentence)

    capitalizedSentence = sentence.upper()

    connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()
