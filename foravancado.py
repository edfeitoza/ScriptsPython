'''
var = list()
for x in range(1,11):
    var.append(x)
print var

var = list()
for x in range(1,11):
    resp = raw_input('Informe o valor: ')
    var.append(resp)
print var
'''
var = list()
for x in range(1,11):
    var.append(raw_input('Informe o valor: '))
print var
