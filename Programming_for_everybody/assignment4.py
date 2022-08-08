import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=input('Enter: ')
data=urllib.request.urlopen(url).read()
tree=ET.fromstring(data)

ls=tree.findall("comments/comment")
s=0
print('count is: ',len(ls))
for i in ls:
    s+=int(i.find('count').text)
print(s)