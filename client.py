#Ángel Cervera Ronda
#Allow us to communicate with other device through sockets

import socket

def run_client():
    # Server details
    ip = socket.gethostname()
    port = 12345
    buffersize = 1024
    
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((ip, port))

    print("Connected to the server")

    while True:
        message = input("You: ")
        soc.sendall(message.encode('utf-8'))

        data = soc.recv(buffersize).decode(encoding='utf-8')
        if (data == "bye"):
            print("Server disconnected.")
            break
        print(f"Server: {data}")

if __name__ == '__main__':
    print("Starting the client...")
    run_client()