import requests

url = "https://gimmeproxy.com/api/getProxy?protocol=http"
r = requests.get(url).json()
proxy = r['curl']
proto = r['protocol']
print ({proto:proxy})

'''
Esqueleto de um sistema de voto automatizado    
url = "http://sitedevotacao"
r = requests.put(url)
r.status_code
204
r.content
''

while 1:
    r = requests.put(url)
    if r.status_code == 204:
        print 'Voto realizado!'
'''