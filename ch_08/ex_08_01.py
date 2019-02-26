inp = input('Enter file name to open: ')
mylist = list()
try:
    fh = open(inp)
except:
    print('Sorry! Can\'t open file ')
    quit()
for line in fh:
    words=line.split()
    for word in words:
        if word not in mylist:
            mylist.append(word)
        else:
            continue
mylist=sorted(mylist) 
print(mylist)