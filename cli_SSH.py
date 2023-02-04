import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="127.0.0.1",username= "root", password = open('pass.txt').read().strip())
stdin,stdout,stderr=ssh.exec_command('ls -l')
print stdout.read()
ssh.close()

