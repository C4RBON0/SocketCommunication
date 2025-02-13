#Ángel Cervera Ronda
#This program enables us to receive and send messages to other device

import socket

def run_server():
    ip = socket.gethostname()
    port = 12345
    buffersize = 100

    soc = socket.socket()
    soc.bind((ip, port))
    soc.listen()

    print('The server is ready...')
    
    while True:
        con, addr = soc.accept()
        print(f"The client address is; {addr}")

        data = con.recv(buffersize).decode(encoding='utf-8')
        print(f"{data}")
        
        break
    
    soc.close()
    print("Socket closed")
    
    soc = socket.socket()
    soc.connect((ip,port))
    prompt = input()
    soc.send(prompt.encode())
    
    
if __name__ == '__main__':
    run_server()
    
        