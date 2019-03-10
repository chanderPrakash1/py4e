file=input('Enter a file name: ')
count = 0
fhand=open(file)
for line in fhand:
        words = line.split()
        if len(words)<2 or words[0]!='From': continue
        print(words[2])
    
