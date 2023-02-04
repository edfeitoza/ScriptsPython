#Modulo para trabalhar com protocolos de rede
import socket
#Modulo para capturar os argumentos na chamada do programa
import sys

#Argumento 1 e o site
#Argumento 2 e percorrer todo o caminho da path principal do site
host = sys.argv[1] #Essa condicional checa se a chamada do programa tem pelo menos 3 argumentos, caso contrario retorna nulo. 
path = sys.argv[2] if len(sys.argv) >= 3 else ''
msg = 'GET /%s HTTP/1.1\nHost: %s\n\n' % (path,host)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)

print 'Conectando...'
s.connect((socket.gethostbyname(host),80))

print 'Enviando...'
s.send(msg)

print 'Recebendo...'
data=''
while 1:
    try:
        buf = s.recv(1024)
        data += buf
    except:
        s.close
        break
print data