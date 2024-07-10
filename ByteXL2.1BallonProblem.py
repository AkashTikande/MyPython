# ballobe problem 2
# to getting odd numnber of ballon
# i.e non reapeted number of ballons.
# wednesday 3/04/2024
# bytexl
# #

num = int(input("Number"))
ballons=[]

for i in range(num):
    value=input()
    ballons.append(value)

freq=[0 for i in range(num)]

for i in range(num):
    for j in range(num):
        if ballons[i]==ballons[j]:
            freq[i]+=1

for i in range(num):
    if freq[i]==1:
        print(ballons[i]);




