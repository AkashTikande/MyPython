# Python program to
# compute sum of digits in
# number.

# Function to get sum of digits
def getSum(n):

    sum = 0  # initially sum is zero #
    for digit in str(n):
        sum += int(digit)
    return sum

n = int(input("Enter the numbers:"))    #user input number
print(getSum(n))   # Query : how to get repeated user input in terminal without rerun the programme?
                  # by using while or do-while loops
