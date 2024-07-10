#In math, an Armstrong number is a number that is equal to the sum of its digits,
# each raised to a power.
# For example, 153 is an Armstrong number because
# 1^3 + 5^3 + 3^3 equals 153

#code
# This Python program checks if the given number is an Armstrong number

# A number is an Armstrong number if the sum of its own digits each raised to the power of the number of digits is equal to the number itself.

# take input from the user
num = int(input("Enter a number: "))

# initialize sum of all digits
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")