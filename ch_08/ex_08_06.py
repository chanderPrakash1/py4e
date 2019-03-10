mylist = list()
while True:
    inp_num=input('Enter a number: ')
    if inp_num=='done':
        break
    try:
        number=float(inp_num)
    except:
        print('Please enter a valid number.')
        continue
    mylist.append(number)
high=max(mylist)
low=min(mylist)

print('Maximum number is',high,'Minimum number is',low)
