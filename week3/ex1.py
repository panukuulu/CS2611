name = input('Give employee\' name: ')
hours = input('Enter number of hours worked in a week: ')
rate = input('Enter hourly pay rate: ')
tax = input('Enter tax witholding rate (0-1): ')
tax2 = input('Enter other tax witholding rate (0-1): ')

'Do the math
gpay = float(hours) * rate
'deductions
ded1 = gpay * tax
ded2 = gpay2 * tax
dedt = ded1 + ded2

print('Employee name: {:s}\n\nHours worked: {:d}\n\n Pay rate: {:f} \n\n Gross pay: {:f} \n\n'.format(name, hours, rate, gpa))