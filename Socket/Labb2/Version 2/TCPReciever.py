from socket import *
import time

# TCP
port = 12000
TCP_socket = socket(AF_INET,SOCK_STREAM)
TCP_socket.bind(('',port))
TCP_socket.listen(1)

expected_message = 1

fregz = 0
print('Ready to recieve')
connection_socket, addr = TCP_socket.accept()
while(True):

    transmission_timer_start = time.time()

    message = connection_socket.recv(2024)
    
    transmission_timer_end = time.time()

    denominator = float(transmission_timer_end - transmission_timer_start)
    if(denominator > 0):
        freqz = 1 / denominator
    else:
        fregz = -1

    # Decoding counter
    decoded_message = message[0:8]
    integer = int.from_bytes(decoded_message, byteorder='big')
    if(integer == 0):
        break
    #If there the messages came in the wrong order
    if(integer > expected_message or integer < expected_message):
        print('******************WRONG ORDER**************************')
        print('Expected: ', expected_message, '\tGot:',integer, '\tdiff: ',(integer - expected_message) )
        print('Counter: ' , integer, '\tFrequency: ', fregz)
        print('*******************************************************')
    else:
        print('Counter: ' , integer, '\tFrequency: ', fregz)

    expected_message = integer+1
connection_socket.close()




