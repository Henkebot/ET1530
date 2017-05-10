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
expectedMessage = 1

print('Ready to recieve!')
while(True):
    
    # Frequency calculater
    transmission_timer_start = time.time()
    
    # Data collected
    message, sender_adress = socket.recvfrom(2048)

    transmission_timer_end = time.time()
    denominator = float(transmission_timer_end - transmission_timer_start)
    if(denominator > 0):
        fregz = 1 / denominator
    else:
        freqz = -1
    
    # Decoding counter
    decoded_message = message[0:8]
    integer = int.from_bytes(decoded_message, byteorder='big')
    
    if(integer > expectedMessage):
        nr_of_loses += (integer - expectedMessage) 
        print('******************WRONG ORDER**************************')
        print('Expected: ', expectedMessage, '\tGot:',integer, '\tdiff: ',(integer - expectedMessage) )
        print('Counter: ' , integer, '\tFrequency: ', fregz)
        print('*******************************************************')
    else:
        print('Counter: ' , integer, '\tFrequency: ', fregz)
        
    expectedMessage = integer+1

