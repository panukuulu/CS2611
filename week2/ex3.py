fval = input("Input final account value: ")
rannual = input("Input annual interest rate: ")
years = input("Input number of years: ")

rannual = float(rannual)
r = rannual / 12
years = float(years)
p = years / 12

ival = (fval) / (1+r)^p
print('Intial deposti value is: {:f}'.format(ival))
