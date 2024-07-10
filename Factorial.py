# Python program to find the factorial of a number provided by the user.

# In mathematics, a factorial is a function that multiplies a number by every number below it until 1.
# For example, 3! = 3 × 2 × 1 and is equal to 6

#num = 7  default input

# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)