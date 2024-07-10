# Program to display the Fibonacci sequence up to n-th term
# define fibonacci series :-

# The Fibonacci series is a sequence of numbers where each number is the sum of the two numbers before it.

# Explanation :-

# The first two numbers in the series are 0 and 1.
# The Fibonacci series is named after Italian mathematician Leonardo Pisano Bogollo,
# who later became known as Fibonacci.
# The Fibonacci series can be defined by the formula:F = F + F,
# where F is the N-th term or number.
# The first six terms of the Fibonacci sequence are 0, 1, 1, 2, 3, 5.

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    print("You calculated fibonacci sequence for 1st ", nterms, "terms")

    # n = int(input("Enter a number"))
    # n1,n2 =0,1
    # print(n1,n2)
    # for (i in the range (n-2)):
    # n3=n1+n2
    # print(n3)
    # n2=n3
    # n1=n2#