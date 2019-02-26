def computegrade(fscore):
    if fscore>=0 and fscore<0.6:
        print('F')
    elif fscore>=0.6 and fscore<0.7:
        print('D')
    elif fscore>=0.7 and fscore<0.8:
        print('C')
    elif fscore>=0.8 and fscore<0.9:
        print('B')
    elif fscore>=0.9 and fscore<=1.0:
        print('A')
    else :
        print('Error! Please Enter a Valid Score ')
    return 0

inp = input('Enter a score: ')
try:
    score= float(inp)
except:
    print('Error!  Please Enter a Numeric Input')
    quit()
    
computegrade(score)
