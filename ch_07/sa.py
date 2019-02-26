inp = input('Enter file name to open')

try:
    fh = open(inp)
except:
    print('Sorry! Can\'t open file ')
    quit()
for line in fh:
    sline=line.split()