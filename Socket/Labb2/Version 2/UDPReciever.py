from socket import *
import time
import struct

# UDP
my_port         = 12000
socket          = socket(AF_INET, SOCK_DGRAM)

socket.bind(('', my_port))

# Transmisson Variables
nr_of_loses     = 0
nr_of_success   = 0
expectedMessage = 0
while(True):
    
    # Frequency calculater
    transmission_timer_start = time.time()
    
    # Data collected
    message, sender_adress = socket.recvfrom(2048)

    transmission_timer_end = time.time()
    
    fregz = 1 / float(transmission_timer_end - transmission_timer_start)
    
    # Decoding counter
    decoded_message = message[0:8]
    integer = int.from_bytes(decoded_message, byteorder='big')
    
    if(integer > expectedMessage):
        nr_of_loses += 1
        print('******************PACKET LOSS**************************')
        print('Expected:\t', expectedMessage, 'Got:\t',integer)
    elif(integer < expectedMessage):
        print('******************WRONG ORDER**************************')
        print('Expected:\t', expectedMessage, 'Got:\t',integer)

    print('Counter: ' , integer, '\tFrequency: ', fregz)

    expectedMessage = integer+1
    
