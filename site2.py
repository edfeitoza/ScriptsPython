import requests
from lxml import html

url = input('Informe o Site: ')

r = requests.get(url)
tree = html.fromstring(r.content)

#print (tree)

v1 = tree.xpath(
    '//*[@id="deviceStatusPage"]/div[4]/table/tbody/tr/td[1]/div/span/text()[2]')  # [0].strip()

print(v1)
'''
v1 = tree.xpath(
    '//*[@id="api"]/div/div[4]/div/table/tbody/tr[9]/td[1]/text()')[0].strip()
v2 = tree.xpath(
    '//*[@id="api"]/div/div[4]/div/table/tbody/tr[9]/td[2]/text()')[0].strip()
v3 = tree.xpath(
    '//*[@id="q"]/div/div[2]/div/p/a/text()')[0].strip() #Pode-se usar o atributo do /a, no caso o @href
print(v1)
print(v2)
print(v3)
'''
