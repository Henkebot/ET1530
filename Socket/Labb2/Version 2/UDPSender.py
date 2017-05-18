from socket import *
import time

# UDP 
target_ip           = '192.168.1.8'
target_port         = 12000
socket              = socket(AF_INET,SOCK_DGRAM)

# Message Settings
frequency           = 10
message_size        = 95
message_sent        = 0

# Timing Settings
last_time           = time.time()
sec_per_send        = 1 / frequency
unprocessed         = 0

# Program runtime
current_time        = time.time()
transmission_time   = 5
start_send_time     = time.time()
finished_time       = start_send_time + transmission_time

while (current_time < finished_time):

    current_time = time.time()

    last_time = current_time


    # Convert message to bytes
    message_sent += 1
    counter = (message_sent.to_bytes(8, byteorder='big')) 
    finalMessage = counter + (';').encode() + bytes(message_size)

    # Cosmetic percentage
    percentage = int((current_time - start_send_time) /(finished_time - start_send_time) * 100)
    print(str(percentage) , ' %')
    
    # Send
    socket.sendto(finalMessage, (target_ip, target_port))

    unprocessed -= 1

socket.close()

end_send_time = time.time()
final_time = (end_send_time - start_send_time)

print('******************************************************')
print('Total packets sent\t', str(message_sent))
print('Time taken\t\t', str(final_time))
    
