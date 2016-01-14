# First excersise
print("First Exercise:")
raw_input("Press enter to continue...")
print("First Exercise:")
print ("Welcome to Python")
print ("Welcome Comp Sci")
print ("Programming is fun \n \n")

# Second excersise
raw_input("Press enter to continue...")
print("Second Exercise:")
x = 1
while x<=5:
	print ("Welcome to Python")
	x += 1
print ("\n \n")

# Third excersise
raw_input("Press enter to continue...")
print("Third Exercise:")
# Get input
distance = input("Enter distance ran: ") 
minutes = input("Enter time spent, minutes:")
seconds = input("Enter time spent, seconds:")
# Do the math
time = minutes*60 + seconds
miles = distance / 1.60
timeh = float(time) / 60 / 60
milesh = float(miles) / float(timeh)
# Print results
print("The runner ran %d kilometers in %d minutes and %d seconds") %(distance, minutes, seconds)
print("The distance in miles is %d and time spent in hours is %.4f") %(miles, timeh)
print("The average speed in miles per hour was consequently %d") %(milesh)
