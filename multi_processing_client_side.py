import socket


host = '127.0.0.1'
port = 12345
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

soc.connect((host,port)) 

while True : 

    message = input("Enter your massage : \n")
    soc.sendall(message.encode('ascii')) 

    if message == "exit":
        break


    data = soc.recv(1024) 
    print('Received from the server :',str(data.decode('ascii')), '\n') 

    ans = input('Do you want to continue(y/n) :') 
    if ans == 'y' :
        continue
    else : 
        soc.sendall(b'exit')
        break
    

soc.close()
