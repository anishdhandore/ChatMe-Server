import socket
import threading

PORT = 5050
# SERVER = "192.168.0.108"
SERVER_IP = socket.gethostbyname(socket.gethostname()) # does the same thing. gets ipv4 address for your device
ADDR = (SERVER_IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setting up the server 
server.bind(ADDR) # binds the server: ipv4 + port

def handle_client(conn, addr):
    pass

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count - 1}")

print("[STARTING] ...")
start()