import re
handle=input('Enter file name:')
file=open(handle)
line=file.read()
n=re.findall('[0-9]+',line)
tot=0
for num in n:
    num=int(num)
    tot+=num
print(tot)

