'''
for x in range(0,5):
    print x
####################################
for x in range(0,11):
    ip = '192.168.0.%d' % x
    print ip
    if ip == '192.168.0.5':
        break
####################################
'''
#y representa os ips dos hosts
#x representa as portas scaneadas
#print '##' acrescenta uma linha a cada FOR executado

for y in range(1,5):
    for x in range(20,24):
        print 'Scan no ip 192.168.0.%d na porta %d' %(y,x)
    print '##'
