# programme no 3
# a whole number greater than 1 that cannot be exactly divided by any whole number,
# other than itself and 1 (e.g. 2, 3, 5, 7, 11).
# "prime numbers are very useful in cryptography"
def check_prime(num):
    """
    Checks if a given number is prime.

    Args:
      num: The number to check.

    Returns:
      True if the number is prime, False otherwise.
    """

    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


# Get the number from the user.
num = int(input("Enter a number: "))

# Check if the number is prime.
if check_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")