import urllib.request, urllib.parse, urllib.error
import json

url=input('Enter: ')
s=0
data=urllib.request.urlopen(url).read()
jd=json.loads(data)

for i in jd['comments']:
    s+=int(i['count'])
print(s)