thisdict = {}
a=""
content=""

file1 = open("file.txt","r") 

content1=file1.read()
for i in content1:
    content=content+i.replace("\n"," ").replace("."," ").replace(","," ").replace("'", " ")
    
for i in content:
    if i==" ":
        b=a.lower()
        if b not in thisdict:
            thisdict[b]=1
        if b in thisdict:
            thisdict[b]=thisdict[b]+1
        a=""
    a=a+i

print (thisdict)

orgdict = sorted(thisdict, key=thisdict.get, reverse=True)
for i in orgdict:
    if thisdict[i]>50:
        print(i, thisdict[i])
        

