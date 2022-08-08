import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter: ')
pos=input('Enter pos: ')
cnt=input('Enter cnt: ')
cnt=int(cnt)
pos=int(pos)-1
cnt1=0

while (cnt1<cnt):
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')

    tags=soup('a')
    url=tags[pos].get('href')
    name=tags[pos].contents[0]
    cnt1+=1
print(name)  