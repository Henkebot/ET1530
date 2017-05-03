from socket import *

print("Creating socket..")
conn = socket(AF_INET, SOCK_STREAM)

adress = "ingonline.nu"
port = 80

print("Connecting socket to " + adress + " with port " + str(port) + "..")
conn.connect((adress,port))

h_message  = "GET /tictactoe/index.php?board=eeeeeeeee HTTP/1.1\r\n"
h_message += "Host: " + adress + "\r\n"
h_message += "Connection: close\r\n\r\n"

print("Sending message..")
conn.send(h_message.encode())

print("Receiving server response..")
# Går att använda .decode() för att få ut responsen i bättre format
s_reply = conn.recv(2048)

print("Server response\r\n\r\n" + str(s_reply))