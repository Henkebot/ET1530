# TCP Client

from socket import *
# serverName = 'hostname' - Ip adress
serverName = "192.168.1.69"
serverPort = 12000

# Create TCP socket on client to use for connecting
# AF_INET is for ipv4
# SOCK_STREAM is TCP 
clientSocket = socket(AF_INET, SOCK_STREAM)

# Open the TCP connection
clientSocket.connect((serverName, serverPort))

# Simple input from keyboard
sentence = input("Input lowercase sentence: ")

# send text over the TCP connection
# there's no need to specify server name & port
# sentence converted to bytes
clientSocket.send(sentence.encode())

# get modififed sentence back from server
modifiedSentence = clientSocket.recv(1024)
print ("From server: ", modifiedSentence.decode())

clientSocket.close()

