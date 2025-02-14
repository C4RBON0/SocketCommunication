#Ángel Cervera Ronda
#Allow us to communicate with other device which will be the server through sockets via text messages

import socket
import time

def run_client():
    # Server details
    ip = socket.gethostname()
    port = 12345
    buffersize = 1024
    delay = 5

    #The client waits for the server to connect, without this if the server isn't already plugged in the connection will fail instantly
    while True:
        try:
            soc = socket.create_connection((ip, port))
            print("Connection established")
            break
        except (socket.timeout, ConnectionRefusedError) as e:
            print(f"No se pudo conectar: {e}. Reintentando en {delay} segundos...")
            time.sleep(delay)

    #Here is the chat connection with the server, inputs and outputs will be displayed
    while True:
        try:
            message = input("You: ")
            soc.sendall(message.encode('utf-8'))
            data = soc.recv(buffersize).decode(encoding='utf-8')
            if data.lower() == "bye":
                print("Server disconnected.")
                break
            print(f"Server: {data}")
        except (ConnectionResetError, BrokenPipeError):
            print("Connection lost.")
            break

    soc.close()

if __name__ == '__main__':
    print("Starting the client...")
    run_client()
