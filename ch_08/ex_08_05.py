file=input('Enter a file name: ')
count = 0
fhand=open(file)
for line in fhand:
    if line.startswith('From:'):
        count = count+1
        words = line.split()
        print(words[1])
    
print('There are',count,'lines in file with From')
        