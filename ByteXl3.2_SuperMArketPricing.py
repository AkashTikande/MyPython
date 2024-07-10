# Tcs NQT EXAMPLE ON prepinsta prime #
# A SEQUJENCE MQAINTAIN A PRIXINBG FORMAT DOR ALL OF ITS PRODUCT,
# A value n is printed  on each product,
# when scanne reads the value N on the iteam ,
# the product of all the digits in the value N is thed priced of thed iteam
# the task here to design the softwere such that given the code of any iteam N the product (multiplication)
# of all the digits of value should be computed(price).
# e.g
# input as 5244
# output 166 ->price #


#same concept mujltiple statement for morepackge
#practice it daily,by yourself
#pripinsta prime

n=input() # 5244
p=1 # variabled to store digit
for i in n:
    p*=int(i)
print(p)

