name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith("From "): continue
    line = line.split()
    line=line[5]
    line=line[:2]
    d[line]=d.get(line,0)+1

for key,val in sorted(d.items()):
    print(key,val)