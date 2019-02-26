hours = input('Enter Hours:')
rate = input('Enter Rate:')
fhours=float(hours)
frate=float(rate)
if fhours>40:
    pay = fhours*frate
    epay = (fhours-40)*0.5*frate
    tpay = pay+epay
else:
    tpay=fhours*frate
print('Pay:',tpay)
