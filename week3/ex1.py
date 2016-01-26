name = input('Give employee\' name: ')
hours = eval(input('Enter number of hours worked in a week: '))
rate = eval(input('Enter hourly pay rate: '))
tax = eval(input('Enter tax witholding rate (0-1): '))
tax2 = eval(input('Enter other tax witholding rate (0-1): '))

#Do the math
gpay = hours * rate
#deductions
ded1 = gpay * tax
ded2 = gpay * tax2
dedt = ded1 + ded2

#stuf for printing
taxp = tax * 100
tax2p = tax2 * 100
netp = gpay - ded1 - ded2

#print sheet
print('Employee name: {:s}\nHours worked: {:d}\nPay rate: {:.2f}\nGross pay: {:.2f}\n'.format(name, hours, rate, gpay))
print('Deductions:\nTax Witholding ({:<1.1%})%: {:.2f}\nOther Tax Witholding ({:<1.1%})%: {:.2f}\nTotal deduction:  {:.2f}\n\nNet pay:{:.2f}'.format(tax,ded1,tax2,ded2,dedt,netp))

