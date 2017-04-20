import sys
from socket import *

try:
    conn = socket(AF_INET, SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()

print("Socket Created")


server = "ingonline.nu"
serverPort = 80

try:
    serverip = gethostbyname(server)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

conn.connect((serverip,serverPort))

print("Socket connected to " + server) 

message = "GET /tictactoe/index.php?board=eeeeeeeee HTTP/1.1\r\nHost: " + server + "\r\nConnection: close\r\n\r\n"

try:

    conn.send(message.encode())
except socket.error:
    print("[ 0 ] Send failed")
    sys.exit()

print("[ ok ] Message send successfully\r\n")

reply = conn.recv(4096).decode()

print("Server response\r\n" + reply)


