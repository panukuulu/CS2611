n1 = eval(input("enter the first number: "))
n2 = eval(input("enter the 2 number: "))
n3 = eval(input("enter the 3 number: "))
vector = [n1,n2,n3]
lenght = len(vector)
average = ((float(vector[0]) + float(vector[1]) + float(vector[2])) / lenght)
print('{:f} and {:f} and {:f} with an average of {:f}'.format(n1,n2,n3,average))

#what is going on with floats and ints here :(? 
