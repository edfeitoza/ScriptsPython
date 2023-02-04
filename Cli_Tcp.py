import socket

ip = '127.0.0.1'
port = 2222

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (ip,port)
tcp.connect(dest)
print tcp.recv(1024)
while True:
    msg = raw_input('>>>')
    tcp.send(msg)
tcp.close()
