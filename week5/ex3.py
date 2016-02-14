def isLeapYear(year):
	isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
	if isLeapYear is True:
		return True
	else:
		return False

def days(year):
	test = isLeapYear(year)
	if test is True:
		days = 366
	else:
		days = 365
	return days

def main():
	for i in range(2010,2020):
		days(i)
		i+=1
		print("The number of days in {:d} is {:d}".format(i,days(i)))

main()

def isLeapYear(year):
	isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
	if isLeapYear is True:
		return True
	else:
		return False

def days(year):
	test = isLeapYear(year)
	if test is True:
		days = 366
	else:
		days = 365
	return days

def main():
	for i in range(2010,2020):
		days(i)
		i+=1
		print("The number of days in {:d} is {:d}".format(i,days(i)))

main()

