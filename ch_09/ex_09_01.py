inp = input('Enter afile name')
try:
    fh=open(inp)
except:
    print('SOrry! cant Open File')
d =dict()
for line in fh:
    words=line.split()
    for word in words:
        d[word]=d.get(word,0)+1
print(d)