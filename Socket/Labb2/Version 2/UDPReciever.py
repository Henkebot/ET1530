from socket import *
import time
import struct

# UDP
my_port         = 12000
socket          = socket(AF_INET, SOCK_DGRAM)

socket.bind(('', my_port))

# Transmisson Variables
anticipate      = 200
message_count   = 0
freq_counter    = 0
nr_of_loses     = 0
nr_of_success   = 0

for x in range(0, int(anticipate)):
    message, sender_adress = socket.recvfrom(2048)
#    decoded_message = message.decode()
    decoded_message = message[0:8]
    integer = int.from_bytes(decoded_message, byteorder='big')
    print(integer)
#    decoded_message = decoded_message[0:decoded_message.find(';')]
#    decoded_message = decoded_message.strip('\\x')

    
#    print(decoded_message)

