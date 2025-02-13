#Ángel Cervera Ronda
#Allow us to communicate with other device through sockets

import socket
import time

def run_client():
    # Server details
    ip = socket.gethostname()
    port = 12345
    buffersize = 1024
    delay = 5

    while True:
        try:
            soc = socket.create_connection((ip, port), timeout=5)
            print("Connection established")
            break
        except (socket.timeout, ConnectionRefusedError) as e:
            print(f"No se pudo conectar: {e}. Reintentando en {delay} segundos...")
            time.sleep(delay)

    while True:
        message = input("You: ")
        soc.sendall(message.encode('utf-8'))

        data = soc.recv(buffersize).decode(encoding='utf-8')
        if data.lower() == "bye":
            print("Server disconnected.")
            break
        print(f"Server: {data}")

    soc.close()

if __name__ == '__main__':
    print("Starting the client...")
    run_client()
