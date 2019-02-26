file=input('Please enter a file name to open: ')
try:
    fh=open(file)
except:
    print('File cannot be opened')
    quit()
count = 0
total = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        y=line.find(':')
        count=count+1
        total=total+float(line[y+1:])
print(total,count,total/count)
        