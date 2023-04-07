import re

text=''
list_msg=[]
with open('msg.txt','r',encoding='utf8') as f:
    raws=f.readlines()
    #print(raws)

    for raw in raws:
        raw_text = ''
        if('msg:' in raw):
            index=raw.index('msg:')
            if (len(raw[index+4:].strip())>0):
                raw_text=raw_text+raw[index+4:].strip()
        else:
            raw_text=raw_text+raw.strip()

        if len(raw_text.strip())>0 and raw_text[-1]=='.':
            list_msg.append(raw_text)

i=1
for msg in list_msg:
    #matnni chiqarish:
    print(i, '-matn : ', msg)


    #o' O' g' G' larni aniqlash:
    list_og=([(x[1]) for x in re.findall("[o-og-gO-OG-G]\W[a-z]",msg) if not x[1] in ' -'])
    print(list_og)

    #tutuq belgilarni aniqlash
    list_tutuq=([(x[1]) for x in re.findall("[a-fh-np-zA-FH-NP-Z]\W[a-z]",msg) if not x[1] in ' -.'])
    print(list_tutuq)

    # probel, nuqta, vergul chiziqchadan tashqari boshqa ortiqcha belgilarni aniqlash:
    for_remove = ([(x) for x in re.findall("\W", msg) if not (x in ' .,-!?')])
    print([(x) for x in for_remove if x not in list_og])

    i=i+1
    print('_________________________________________________________')

