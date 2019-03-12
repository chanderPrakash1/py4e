file=input('Enter afile to open')
dd=dict()
try:
    fh=open(file)
except:
    print('The file can not be opened')
lst=list()
for line in fh:
    if line.startswith('From'):
        words=line.split()
        lst.append(words[2])
        print(lst)
            
            
