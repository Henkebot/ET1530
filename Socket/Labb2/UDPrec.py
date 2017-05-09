from socket import *

import time
Port = 12000

UDPSocket = socket(AF_INET, SOCK_DGRAM)
UDPSocket.bind(("",Port))

print("Ready for recieve")
nrOfMessages = 0
accumlator = 0
nrOfLoses = 0
nrOfSucess= 0
lastInt = 0
anticipate = 2000


for x in range(0,int(anticipate)):
	lastTime = time.time()

	message, clientAddress = UDPSocket.recvfrom(2048)
	nrOfMessages += 1
	now = time.time()
	deMessage = int.from_bytes(message, byteorder='big')
	
	
	nowInt = deMessage
	dt = 0
	if(float(now - lastTime) > 0):
		dt = 1/float(now-lastTime)
		accumlator += dt
	if(nowInt ==(lastInt+1)):
		nrOfSucess+=1
	else:
		nrOfLoses+=1
	
	print("Freg\t" + str(dt) + " \tMsg: " + str(nowInt) )

	average = float(accumlator) / float(nrOfMessages)
	lastInt = nowInt

print("***********************************************")
print("Freg average\t\t" + str(average))
print("Recieved packets\t" + str(nrOfSucess))
print("Packet loses\t\t" + str(nrOfLoses))
