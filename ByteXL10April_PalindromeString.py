# reverse palindrome string
#Tcs que series
def ispalindrome(sum):
    return sum ==int(str(sum)[::-1])
def rev(n):
    return int (str(n)[::-1]) # for performing  reverse operation

n = int(input())
while(1):
    n=n+rev(n)
    if(ispalindrome(n)):
       print(n)
       break



