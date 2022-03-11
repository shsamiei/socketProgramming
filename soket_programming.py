import socket

soc  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
port = 1234 

soc.bind(('', port))
soc.listen()

while True : 
    client , address = soc.accept()
    print(type(client) , address)
    client.sendall(b'Hello welcome to the server but get out bitch ! :((\n')
    # client.close()

