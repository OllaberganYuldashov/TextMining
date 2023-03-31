import requests
from bs4 import BeautifulSoup

url='https://uz.wikipedia.org/wiki/Bosh_Sahifa'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
#print(soup)
table=soup.find('table', attrs={'id':'mp-upper'})


print(table.text)