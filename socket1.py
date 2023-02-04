import socket

ip = '127.0.0.1'
porta = 2222

#cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Define porta que vai ser aberta
s.bind((ip, porta))

#Armazenado em uma fila antes de receber o accept()
s.listen(5)

while True:
	conn, addr = s.accept() #Aceita a conexao removendo da lista do listen()
	conn.send('Servidor TCP\n')
	print 'conexo de %s:%d' %(addr[0],addr[1])
	conn.send('>>>')
	msg = conn.recv(1024)
	print 'Recebido: %s' %msg
	conn.close()
	break

s.close