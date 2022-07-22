#This program will display the most occoured word and its count in a file
#Getting the file name
#Enter the file name as test.txt or intro.txt. test & intro contains random paragraphs
name=input('Enter file name: ')
handle=open(name)

#Getting the count of each word into the dictionary
counts=dict()
for lines in handle:
    lines=lines.rstrip()
    words=lines.split()
    for i in words:
       counts[i]=counts.get(i,0)+1 #Getting the counts into the dictionary

#Determining the most occoured word and its count
bigCount=-1
#bigWord=-1
for x,y in counts.items():
    if y>bigCount:
        bigCount=y
        bigWord=x

#Printing the desired output
print('Most occoured word is:',bigWord)
print('The number of times it occoured is:',bigCount)