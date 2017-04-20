from socket import *
from ctypes import *
 
STD_OUTPUT_HANDLE = -11
 
class COORD(Structure):
    pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]
 
def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
 
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
 


serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))

serverSocket.listen(2)

print("Server is online")


while True:
    connectionSocket,addr = serverSocket.accept()
   
    pos = connectionSocket.recv(1024).decode()
    
    print(addr)
    print_at(2,0,("Player is at: " + pos))


    connectionSocket.send(pos.encode())

    connectionSocket.close()
