user = raw_input('informe o nome do usuario: ')

if user == 'root':
    print 'Logado como, %s' % user
elif user == 'admin':
    print 'Logado como, %s' % user
else:
    print 'Usuario incorreto'
