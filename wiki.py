import requests
from bs4 import BeautifulSoup

url='https://uz.wikipedia.org/wiki/Maxsus:AllPages/A'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
#print(type(soup))

ul=soup.find('ul', attrs={'class':'mw-allpages-chunk'})

li=ul.find_all('li')


global_link='https://uz.wikipedia.org'

for l in li:

    file_name=l.text
    #print(file_name)
    #print(l.find('a')['href'])
    local_link=global_link+l.find('a')['href']
    print(local_link)
    local_r = requests.get(local_link)
    local_soup = BeautifulSoup(local_r.content, 'html.parser')
    text=local_soup.find('div', attrs={'class':'mw-parser-output'}).text


    try:
        with open('corpus/'+str(file_name)+".txt",'w',encoding='utf8') as f:
            f.write(text)

    except:
        continue

