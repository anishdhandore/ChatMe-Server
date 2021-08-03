import socket
import time

# CONSTANTS
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5051
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(client, msg):
    message = msg.encode('utf-8')
    client.send(message)

def start():
    inp = input("Do you want to connect to the chatroom (yes/no)? ").lower()
    if inp == "yes":
        while True:
            msg = input("Message (q to quit) ")
            if msg == "q":
                time.sleep(1)
                send_message(client, "!DISCONNECTED")
                break
            send_message(client, msg)
    else:
        return

start()
