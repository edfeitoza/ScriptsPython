import socket

ip = '127.0.0.1'
port=5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (ip,port)

while True:
    msg = raw_input('>>>')
    udp.sendto(msg,dest)
    msg,conn = udp.recvfrom(1024)
    print msg

udp.close()