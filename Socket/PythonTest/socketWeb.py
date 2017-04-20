from socket import *

conn = socket(AF_INET, SOCK_STREAM)

print("Socket created")

adress = "ingonline.nu"
port = 80

conn.connect((adress,port))

print("Socket connected to " + adress + " with port " + str(port) )

h_message  = "GET /tictactoe/index.php?board=eeeeeeeee HTTP/1.1\r\n"
h_message += "Host: " + adress + "\r\n"
h_message += "Connection: close\r\n\r\n"

conn.send(h_message.encode())

print("Message sent successfully\r\n")
 

s_reply = conn.recv(2048).decode()

print("Server response\r\n\r\n" + s_reply)