from socket import *
import time

# UDP 
target_ip       = '192.168.1.10'
target_port     = 12000
socket          = socket(AF_INET,SOCK_DGRAM)

# Message Settings
frequency       = 20
messages        = 200
message_size    = 95
message_sent    = 0

# Timing Settings
last_time       = time.time()
sec_per_send    = 1 / frequency
unprocessed     = 0



start_send_time   = time.time()
while (message_sent < messages):

    current_time = time.time()
    unprocessed += (current_time - last_time) / sec_per_send
    last_time = current_time

    while(unprocessed > 1):
        message_sent += 1
        counter = (message_sent.to_bytes(8, byteorder='big')) 
        finalMessage = counter + (';').encode() + bytes(message_size)

        print(str((message_sent/messages) * 100) , ' %')
        socket.sendto(finalMessage, (target_ip, target_port))

        unprocessed -= 1

socket.close()

end_send_time = time.time()
final_time = (end_send_time - start_send_time)
expected_time = (messages / frequency)
difference = float(final_time - expected_time)

print('******************************************************')
print('Total packets sent\t', str(message_sent))
print('Time taken\t\t', str(final_time))
print('Time expected\t\t', str(expected_time))
print('Difference\t\t', str(difference))
    
