#Ángel Cervera Ronda
#This program enables us to receive and send messages to other device

import socket
import time

def run_server():
    ip = socket.gethostname()
    port = 12345
    buffersize = 1024

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((ip, port))
    soc.listen()

    print('Waiting for the client to connect...')
    con, addr = soc.accept()
    print(f"Connected to client at: {addr}")

    with con:
        while True:
            data = con.recv(buffersize).decode(encoding='utf-8')
            if (data == "bye"):
                print("Client disconnected.")
                break
            print(f"Client: {data}")

            response = input("You: ")
            con.sendall(response.encode('utf-8'))

if __name__ == '__main__':
    print("Starting the server...")
    run_server()