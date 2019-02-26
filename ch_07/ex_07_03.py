file=input('Please enter a file name to open: ')
if file=='na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
else:
    try:
        fh=open(file)
    except:
        print('File cannot be opened:',file)
        quit()
count = 0
for line in fh:
    if line.startswith('Subject'):
        count=count+1
print('There were',count,'subject lines in',file)