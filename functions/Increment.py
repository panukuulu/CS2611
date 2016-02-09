#pass by val, x is a reference, not x

def increment(x):
    x += 1
    print("\tn inside the function is", x)
    #add return x

def main():
    x = 1
    print("Before the call, x is", x)
    increment(x) # change this to x = increment x to pass x as value, not as a reference
    print("After the call, x is", x)



main() # Call the main function
