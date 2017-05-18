from socket import *
from time import sleep
from time import *
serverIP = '193.11.184.212'
port = 80
frequency = 50
UDPSocket = socket(AF_INET, SOCK_DGRAM)
nrOfMessagesToSend = 100
message = ''
start = clock()

print('sending packets')
for x in range(0, nrOfMessagesToSend):
    message = '000000' + str(x)
    mNr = str(x + 1)
    nrOfChars = len(mNr)
    for y in range(0, nrOfChars):
        message = message[:-1]
    message = message + mNr + ';'
    UDPSocket.sendto(message.encode(), (serverIP, port))
    sleep(1 / frequency)
end = clock()

print(end - start)

UDPSocket.close()