def computepay(h,r):
    if h<=40:
        pay = h*r
    elif h>40:
        reg_pay=h*r
        ot_pay=(h-40)*0.5*r
        pay = reg_pay + ot_pay
    return pay

try:
    fhours= float(input('Enter Hours: '))
    frate= float(input('Enter Rate: '))
except:
    print('Please Enter A numeric Input')
    quit()

pay=computepay(fhours,frate)
print('Pay: ',pay)