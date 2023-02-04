import smtplib
from email.MIMEText import MIMEText

fromaddr = 'e-mailenvio@email.com'
toaddr = ['e-maildest@email.com','e-mail2dest@email.com']

#envio de corpo do e-mail que esta no arquivo email.txt
msg = MIMEText(open('email.txt','rb').read())
msg['From'] = 'Nome Envio'
msg['To'] = 'nome destino'
msg['Subject'] = 'Assunto e-mail'

#transformando o conteudo da variavel "msg" em string
msg = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, open('senha.txt').read().strip())
server.sendmail(fromaddr,toaddr.msg)
server.quit()
