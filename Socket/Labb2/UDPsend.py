from socket import *
from time import sleep
import time

IP = "193.11.184.65"
Port = 12000

freqz = 50
messages = 500
sleepAddition = freqz * -0.05
UDPSocket = socket(AF_INET, SOCK_DGRAM)

print("Sending Packets")
now = time.time()
for x in range(1,messages+1):

	byteMessage = x.to_bytes(8, byteorder='big');print(byteMessage)
	UDPSocket.sendto(byteMessage,(IP,Port))
	
	sleepTime = (1/(freqz+sleepAddition))

	sleep(sleepTime)
done = time.time()
finalTime = (done - now)
expect = (messages / freqz) + sleepTime
print("***********************************************")
print("Should have taken\t" + str(expect))
print("Took\t\t\t" + str(finalTime))
print("Difference\t\t" + str(expect - finalTime))
UDPSocket.close()
