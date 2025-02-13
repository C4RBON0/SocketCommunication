#Ángel Cervera Ronda
#Allow us to communicate with other device through sockets

import socket

def server_connect():
    ip = socket.gethostname()
    port = 12345
    buffersize = 100
    
    soc = socket.socket()
    soc.connect((ip,port))
    
    msg = "I would like to scan your ports, do I have the authoritation? (yes/no)"
    soc.send(msg.encode())
    soc.close()
    #------------------------------------------------
    soc = socket.socket()
    soc.connect((ip,port))
    soc.bind((ip, port))
    soc.listen()
    print("Waiting for server's response")
    
    while True:
        con, addr = soc.accept()
        print(f"The server address is; {addr}")

        data = con.recv(buffersize).decode(encoding='utf-8')
        #print(f'the received data is\n{data}')
        break
    
    if (data == "yes"):
        print("Permition conceded")
    else:
        print("Access denied")

        


    
    #s.close()
        
if __name__ == "__main__":
    
    print("Connecting to server...")
    server_connect()