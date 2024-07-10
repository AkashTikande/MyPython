
# give an integer array of size n the task is to find the count
# of element whose value is greater that all of its prior elemnt
# Note 1st element is considered in  the count of the element

n=int(input())
li=[]
count=1

for i in range(n):
    value=int(input())
    li.append(value)

max_ele=li[0]

for i in range(1,n):
    if li[i]>max_ele:
        count+=1
        max_ele=li[i]

print(count)