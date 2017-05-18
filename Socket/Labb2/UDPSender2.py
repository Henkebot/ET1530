from socket import *

import time

port = 12000
UDPsocket = socket(AF_INET, SOCK_DGRAM)
UDPsocket.bind(('', port))

print ("receiving now")
lastInt = 0
nrOfLoses = 0
nrOfSuccess = 0

while True:
    lastTime = time.time()

    message, clientAddress = UDPsocket.recvfrom(2048)

    now = time.time()

    deMessage = message.decode()
    deMessage = int(deMessage[:-1])
    nowInt = deMessage


    if(float(now - lastTime) == 0):
        dt = 1/0.00000001
    else:
        dt = 1/float(now - lastTime)
    
        
   

    if(nowInt == (lastInt+1)):
        print("Packet freq " + str(dt))
    else:
        nrOfLoses+=1
    
    lastInt = nowInt
  