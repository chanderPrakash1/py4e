fh=open('mbox2.txt')
count=0
for x in fh:
    lx=x.strip()
    print(lx.upper())