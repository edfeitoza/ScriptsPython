import socket
from threading import Thread

def agent(conn):
    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        print 'Recebido: %s' %msg
    conn.close()

ip = '127.0.0.1'
port = 2222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(5)

while True:
    conn, addr = s.accept()
    conn.send('conexao realizada')
    print 'Conexao de %s:%d' %(addr[0],addr[1])
    t = Thread(target=agent, args=(conn,))
    t.start()

s.close