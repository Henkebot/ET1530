from socket import *
import time

# UDP 
target_ip       = '193.11.185.201'
target_port     = 12000
socket          = socket(AF_INET,SOCK_DGRAM)

# Message Settings
frequency       = 10
message_size    = 95
message_sent    = 0

# Timing Settings
last_time       = time.time()
sec_per_send    = 1 / frequency
unprocessed     = 0

transmission_time = 15

start_send_time   = time.time()

finished_time = start_send_time + transmission_time

current_time = time.time()

while (current_time < finished_time):

    current_time = time.time()
    unprocessed += (current_time - last_time) / sec_per_send
    unprocessed = 1
    last_time = current_time

#    while(unprocessed > 0):
    message_sent += 1
    counter = (message_sent.to_bytes(8, byteorder='big')) 
    finalMessage = counter + (';').encode() + bytes(message_size)
    percentage = int((current_time - start_send_time) /(finished_time - start_send_time) * 100)
    print(str(percentage) , ' %')
    socket.sendto(finalMessage, (target_ip, target_port))

    unprocessed -= 1

socket.close()

end_send_time = time.time()
final_time = (end_send_time - start_send_time)

print('******************************************************')
print('Total packets sent\t', str(message_sent))
print('Time taken\t\t', str(final_time))
    
