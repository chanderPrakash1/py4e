file=input('Enter a file to open: ')
dd=dict()
try:
    fh=open(file)
except:
    print('The file can not be opened')
    exit()
for line in fh:
    if line.startswith('From'):
        words=line.split()
        if len(words)<2 or words[0]!='From':continue
        #print('DEBUG: ',words)
        pos=words[1].find('@')
        addr=words[1][pos+1:]
        dd[addr]=dd.get(addr,0)+1
print(dd)
            
        
        
    