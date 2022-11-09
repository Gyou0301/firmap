''' #メモ
import json
json_open = open('Address.js','r')
json_load = json.load(json_open)
print(json_load)
'''


import re
import requests
import json


address='愛知県名古屋市熱田区千代田町６-７'
address=re.sub("[１-９].*","", address)


url1='http://zipcoda.net/api?address='+address
postal=str(requests.get(url1).json()['items'][0]['zipcode'])

url2 = 'http://geoapi.heartrails.com/api/json?method=searchByPostal&postal='
res_dict = requests.get(url2+postal).json()['response']['location'][0]
x=float(res_dict['x'])
y=float(res_dict['y'])

print(x)
print(y)

print(postal)
