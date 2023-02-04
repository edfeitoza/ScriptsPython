import socket

#IP e porta de conexao
ip = ''
porta = 5000
#Informa qual protocolo sera a conexao
#socket.AF_INET = IPV4
#socket.SOCK_DGRAM = UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (ip,porta)
#Abrindo para as conexoes
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    print cliente[0],msg
    if msg:
        try:
            result = socket.gethostbyname(msg.strip())
        except Exception as e:
            result = str(e)
        udp.sendto(result+'\n',cliente)
udp.close()