count =0
total=0
while True:
    inp=input('Enter a number: ')
    if inp == 'done':
        break
    try:
        finp=float(inp)
    except:
        print('Invalid Input')
        continue
    count=count+1
    total = total + finp

print(total,count,total/count)    