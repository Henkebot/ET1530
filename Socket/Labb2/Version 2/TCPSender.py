from socket import *
import time

# TCP
target_ip       = '192.168.1.8'
target_port     = 12000

TCP_socket      = socket(AF_INET,SOCK_STREAM)
TCP_socket.connect((target_ip,target_port))

# Message Settings
frequency           = 10
message_size        = 95
message_sent        = 0

# Timing Settings
last_time           = time.time()
sec_per_send        = 1 / frequency
unprocessed         = 0

# Program Runtime
current_time        = time.time()
transmission_time   = 15
start_send_time     = time.time()
finished_time       = start_send_time + transmission_time

while(current_time < finished_time):

    current_time = time.time()
    unprocessed += (current_time - last_time) / sec_per_send
    last_time = current_time

    while(unprocessed > 1):
        # Creating message with a counter
        message_sent += 1
        counter = (message_sent.to_bytes(8, byteorder='big'))
        final_message = counter + (';').encode() + bytes(message_size)

        # Cosmetic percentage
        percentage = int((current_time - start_send_time) / (finished_time - start_send_time) * 100)
        print(str(percentage), ' %')

        TCP_socket.send(final_message)

        unprocessed -= 1

TCP_socket.close()

end_send_time = time.time()
final_time = (end_send_time - start_send_time)

print('*****************************************************')
print('Total packets sent\t', str(message_sent))
print('Time taken\t\t', str(final_time))
