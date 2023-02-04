import smtplib

#e-mail de envio
email_from = "edfeitoza@gmail.com"
#e-mail de destino
email_to = "edfeitoza_cert@hotmail.com"

#Servidor SMTP
smtp = "smtp.gmail.com"
#Inicia a instancia SMTP na porta 587
server = smtplib.SMTP(smtp, 587)
#Criptografia de envio de e-mail
server.starttls

#Login e senha no serviço de SMPT
#server.login(email_from, open('V:\\git\\Python_Script\\Scripts\\senha.txt').read().strip())
server.login(email_from,'#Gomes40')
#Corpo de e-mail
msg = "Nova mensagem"

#Envio do e-mail
server.sendmail(email_from,email_to,msg)
#Fecha a conexao
server.quit()