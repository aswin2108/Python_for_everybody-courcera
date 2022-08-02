# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ans=0
cnt=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line=line.rstrip()
    x=line.find("X-DSPAM-Confidence:") 
    y=float(line[x+19:])
    ans+=y
    cnt+=1
print("Average spam confidence:",ans/cnt)
