var = list()
while True:
    msg = raw_input('Informe um valor ou nada pra sair ')
    if msg:
        var.append(msg)
    else:
        break
#print var
for valor in var:
    print valor