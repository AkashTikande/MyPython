# airport security problem
# get input string from user, as ABNY random numbers
# use sorting algorithm to sort given numbers in sorted manner


# look at sorting array


# TCS PROBLEM
    # AITPORT SECURITY OFFICIALS HAVE CONFISCATED SEVERSAL ITEAM OF THE PASSENGER AT THE SECURITY check point.
    # All the iteams have been dumped into a box (array). Each iteam posseses a certsain amount of risk[0,1,2]
# here the risk severity items represents an array[] of N number of integer values.
# The risk here is to sort the items based upon their levels of risk in the array.
# the risk value rang from 0 to 2#
n = int(input("Enter the range of number:"))
arr = []
for i in range(n):
    arr.append(int(input()))
for i in sorted(arr):
    print(i, end="")


# alternate code#
# #
