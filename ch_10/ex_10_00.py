file=input('Enter a file to open: ')
if len(file)<1 : file='mbox-short.txt'
dd=dict()
try:
    fh=open(file)
except:
    print('The file can not be opened')
    exit()
for line in fh:
    if line.startswith('From'):
        words=line.split()
        #print(words)
        if len(words)<2 or words[0] != 'From':continue
        #print('DEBUG: ',words)
        time=words[5].split(':')
        #print(time)
        hrs=time[0]
        dd[hrs]=dd.get(hrs,0)+1
for k,v in sorted(dd.items()):
    print(k,v)
        

   