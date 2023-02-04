import smtplib
import mimetypes

#Permite que seja usado diversos tipos de anexos em um e-mail
from email.MIMEMultipart import MIMEMultipart
#Biblioteca para adicionar texto
from email.MIMEText import MIMEText
#Biblioteca para adicionar anexo
from email.MIMEBase import MIMEBase

#Faz com que o anexo seja "encodado" para se tornar legivel para quem receber
from email import encoders

fromaddr = "e-mailenvio@email.com"
toaddr = "e-mailrecebe@email.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Assunto do e-mail"

body = "Corpo do e-mail"
msg.attach(MIMEText(body))

#Armazena o anexo na variavel "Filename"
filename = 'imagem.gif'
#Anexa no e-mail, abrindo o anexo como leitura binaria
attachament = open(filename,"rb")

#Informacao sobre o MIMEType do objeto a ser anexado
mimetype_anexo = mimetypes.guess_type(filename)[0].split('/')
part = MIMEBase(mimetypes_anexo[0],mimetype_anexo[1])

part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, open('senha.txt').read().strip())
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()
