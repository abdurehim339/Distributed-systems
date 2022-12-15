import socket
import threading #create multiple threads

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #gets the ip address of the computer by name
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT = "!disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):  #handles individual connections 1v1
    print(f"NEW CONNECTION {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #blocking line of code
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT:
                connected = False

            print(f"[{addr}] {msg}")
    conn.close()

def start(): #Handles new connections
    server.listen()
    while(True):
        conn, addr = server.accept() #wait for a new connection     conn=an object used to communicate back to the client   addr=stores ip address and port
        Thread = threading.Thread(target = handle_client, args=(conn, addr))
        Thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

print("[STARTING] server is starting....")
start()
