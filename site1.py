import requests
from lxml import html

r = requests.get(
    "https://10.0.2.38/hp/device/this.LCDispatcher?nav=hp.Usage")

tree = html.fromstring(r.content)

#print (tree)

v1 = tree.xpath(
    '//*[@id="tbl-9160"]/tbody/tr[6]/td[2]/div')#[0].strip()
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

#for v2 in v1:
#    print (v2)


from lxml import html
import requests

url ="https://en.wikipedia.org/wiki/Outline_of_the_Marvel_Cinematic_Universe"

resp = requests.get(url)

tree = html.fromstring(resp.content)

elements = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[*]/th/i/a/text()')
for var in elements:
    print (var)

base_url = "https://en.wikipedia.org"

links = [base_url+element.attrib['href'] for element in elements]

print(links)
'''
