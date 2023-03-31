import csv
import re
text=""
with open('SmallCorpus.txt','r', encoding='utf8') as txt_file:
    lines = txt_file.readlines()
    for line in lines:
        text=text+' '+line.strip()

#print(text)

sentences = re.split('[.?!]', text)
print(type(sentences))
print(sentences)
print(len(sentences))

words=[]
for sent in sentences:
    raw=re.split('\s',sent)

    clean_raw=[]
    for r in raw:
        if(len(r.strip())>0) and not(r.isdigit()):
            clean_raw.append(r.strip(' ,'))
    words.append(clean_raw)

frequency=[]
for i in words:
    for j in i:
        #print(j,text.count(j))
        frequency.append(list((j,text.count(j))))

print(frequency)

with open('frec.csv',mode='w',encoding='utf8') as file:
    writer=csv.writer(file)
    writer.writerow(['words','frequency'])
    for i in frequency:
        writer.writerow(i)

import pandas as pd
import openpyxl as xl
file=pd.read_csv('frec.csv')

print(file['words'])


excel=pd.read_excel('words.xlsx')
print(excel)

import xlsxwriter

wb=xlsxwriter.Workbook('asd.xlsx')
wt1=wb.add_worksheet()
wt2=wb.add_worksheet()
wt1.write(1,1,'sfdf')
wt1.write(1,2,'sdsf')
wt2.write(2,3,'1000000')
wb.close()

import json as js
mydict={
    'name':'dsfzg',
    'age':12,
}
print(type(mydict))
obj=js.dumps(mydict)
print(type(obj))
print(js.loads(obj))
