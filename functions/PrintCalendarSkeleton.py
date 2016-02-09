#The % (modulo) operator yields the remainder from the division of the first argument by the second. The numeric arguments are first converted to a common type. A zero right argument raises the ZeroDivisionError exception. The arguments may be floating point numbers, e.g., 3.14%0.7 equals 0.34 (since 3.14 equals 4*0.7 + 0.34.) The modulo operator always yields a result with the same sign as its second operand (or zero); the absolute value of the result is strictly smaller than the absolute value of the second operand [2].

# A stub for printMonth may look like this
def printMonth(year, month): 
    print("printMonth")
  
# A stub for printMonthTitle may look like this 
def printMonthTitle(year, month): 
    print("printMonthTitle")

# A stub for getMonthBody may look like this 
def printMonthBody(year, month): 
    print("printMonthBody")

# A stub for getMonthName may look like this 
def getMonthName(month): 
    print("getMonthName")

# A stub for getStartDay may look like this 
def getStartDay(year, month): 
    print("getStartDay")

# A stub for getTotalNumberOfDays may look like this 
def getTotalNumberOfDays(year, month): 
    print("getTotalNumberOfDays")

# A stub for getNumberOfDaysInMonth may look like this 
def getNumberOfDaysInMonth(year, month): 
    print("getNumberOfDaysInMonth")

# A stub for isLeapYear may look like this 
def isLeapYear(year): 
    print("isLeapYear")

def main():
    # Prompt the user to enter year and month 
    year = eval(input("Enter full year (e.g., 2001): "))
    month = eval(input((
        "Enter month as number between 1 and 12: ")))

    # Print calendar for the month of the year
    printMonth(year, month)
 
main()
