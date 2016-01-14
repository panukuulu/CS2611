# First excersise. There must be a more elegant way of doing this? 
print("First Exercise:")
raw_input("Press enter to continue...")
print("FFFFFFF\t U   U NN\tNN\nFF\t U   U NNN\tNN\nFFFFFFF  U   U NN N\tNN\nFF\t  U U  NN  N    NN\nFF\t  UUU  NN  NNNNNN")
print ("\n \n")
# Second excersise
print("Second Exercise:")
raw_input("Press enter to continue...")
import math
# Get input
radius = input("Radius of the circle:")

# Do the math
area = float(radius * radius * math.pi)
perimiter = float(2.0 * radius * math.pi)

# Print stuff
print ("The area of a circle with a radius of %d is %d and the perimiter is %d") % (radius, area, perimiter)

print ("\n \n")
# Third excersise
print("Third Exercise:")
raw_input("Press enter to continue...")
print("Calcluate as (9.5 * 4.5 - 2.5 * 3) / (45.5-3.5)")
resulta = float((9.5 * 4.5 - 2.5 * 3) / (45.5-3.5))
print resulta

print("Lets make sure this work and calculate denominator, numerator separately and then divide.")
# lets make sure this works
den = 45.5-3.5
num = 9.5 * 4.5 - 2.5 * 3
print("Denominator: %d. Numerator: %d") % (den, num)
resultb = float(num/den)
print ("Result: %0.12f") %(resultb) #  Not sure why %d doesn't work. resultb should be a float, resulta should be a float yet %d returns a integer?
error = abs(resulta-resultb)
print("First result minus second result equals %d") % (error)
if error == 0:
	print("Huzzah great success, both methods bring the same result")
else:
	print("fail")
print ("\n \n")


# 4th excersise
print("4th Exercise:")
raw_input("Press enter to continue...")
# 1 birth every 40 seconds, 1 death every 60 seconds, 1 immigrant every 100 seconds

# how many seconds in a year? 
ysec = 365*24*60*60

#How many births in a year?
bannual = ysec/40

#How many deaths in a year?
dannual = ysec/60

#How many immigrants in a year?
iannual = ysec/100

net = bannual + iannual - dannual
print ("Every year there are %d births, %d deaths and %d immigrants. Annual net growth is %d") % (bannual, iannual, dannual, net)

net5y = 64596800 + net*5

print ("In five years the population will be %d") % (net5y)
