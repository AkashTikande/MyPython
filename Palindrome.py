# programme no 6:

# palindrome number defined as the number
# A palindromic number is a number that remains the same,
# when its digits are reversed. For example, 16461 is a palindromic number.

def is_palindrome(number):

    temp = number
    rev = 0
    while (number > 0):
        dig = number % 10
        rev = rev * 10 + dig
        number = number // 10
    if (temp == rev):
        return True
    else:
        return False
    # Driver code for palindrome

    # A palindrome number is a number that reads
    # the same forward and backward.
    # In other words, if you reverse the digits of a palindrome number,
    # you get the same number. For example, 121 is a palindrome number because
    # if you read it backward, it is still 121.
    # Another example of a palindrome number is 132231.

number = int(input("Enter a number: "))

if (is_palindrome(number)):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")