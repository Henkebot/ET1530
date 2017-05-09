from socket import *
import time

IP              = "193.11.185.173"
Port            = 12000

freqz           = 128
messages        = 2000
messageCounter  = 0
UDPSocket       = socket(AF_INET,SOCK_DGRAM)

lastTime        = time.time()
nsPerTick       = 1/freqz
unprocessed     = 0

nowT = time.time()

while(messageCounter < messages):

    now = time.time()
    unprocessed += (now - lastTime) / nsPerTick
    lastTime = now

    while (unprocessed > 1):
        byteMessage = messageCounter.to_bytes(8, byteorder='big')
        UDPSocket.sendto(byteMessage,(IP,Port))
        messageCounter+=1
        unprocessed -= 1

doneT = time.time()
finalTime = (doneT - nowT)
expect = (messages / freqz)
print("***********************************************")
print("Should have taken\t" + str(expect))
print("Took\t\t\t" + str(finalTime))
print("Difference\t\t" + str(expect - finalTime))
UDPSocket.close()