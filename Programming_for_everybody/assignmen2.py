from re import X
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter: ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('span')
s=0
print(tags)
for num in tags:
    x=int(num.contents[0])
    s+=x
print(s)
   