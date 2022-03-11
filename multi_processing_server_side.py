
import socket , threading

def threaded(client , addr):
    while True :
        data = client.recv(1024)
        if data == b'exit': 
            print('Conncetion to', addr[0], ':', addr[1], 'lost.') 
            break
        data = b'gooooor amat :(((('
        client.sendall(data) 

    client.close() 
    pass




host = ''
port = 12345

soc = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
soc.bind((host , port))
print('socket binded to post', port)

soc.listen()
print('socket is listening...')


for i in range(10):
    client , addr = soc.accept()
    print('Connected to :', addr[0], ':', addr[1]) 
    threading.Thread(target= threaded , args =(client , addr)).start()

