fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  ls=line.rstrip().split()
  for i in ls:
    if i in lst:
        continue
    lst.append(i)
lst.sort()
print(lst)

