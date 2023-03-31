import requests
import json
x = requests.get('https://uz.wikipedia.org/wiki/Amir_Shohmurod')
print(x.status_code)
print((x.text))