# Python program to display all the prime numbers within an interval

# a whole number greater than 1 that cannot be exactly divided by any whole number,
# other than itself and 1 (e.g. 2, 3, 5, 7, 11).
# "prime numbers are very useful in cryptography"

lower = int(input("Enter starting range of number:"))
upper = int(input("Enter Ending range of number:"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        # prime logic
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)