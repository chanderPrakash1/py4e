high=None
low=None
while True:
    inp=input('Enter a number: ')
    if inp == 'done':
        break
    try:
        finp=float(inp)
    except:
        print('Invalid Input')
        continue
    if high is None:
        high = finp
    elif finp>high:
        high = finp
    if low is None:
        low = finp
    elif finp<low:
        low=finp

print(high,low)    