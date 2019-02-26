str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(':')
nstr = str[start+1:]
nstr1= nstr.strip()
numbr=float(nstr1)
print('the number in floating point is: ',numbr)