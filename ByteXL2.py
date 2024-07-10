
# byte xl practice wednesday 3/04/2024
# PROBLEM STATEMENT 1 : #
# READ THE PROBLEM STATEMENT CAREFULLY UNDERSTAND PROBLEM STATEMENT 1ST, GET STEPS AND ALL ESSENTIAL DATA TO SOLVE PROBLEM STATEMENT
# GET FORMULLA'S AND TRY TO SOLVE IT UNDER REFFEReNCE, THEN BY YOUR SELF.
# imp for tcs exams too #
# 30min max time for 1 problem statement #
# solve problem statement on daily basis #
# maintain leat code and haker rank score.
# solve every kind of problem #


weight = int(input("ENTER THE WEIGHT OF CLOTHES PUT IN:"))
if weight <= 0:
    print("Invalid")

elif weight>=1 and weight <= 2000:
    print("Estimated 25 minutes")
elif weight < 2000 and weight <= 3000:
    print("Estimated 35 minutes")
elif weight < 3000 and weight <= 7000:
    print("Estimated 45 minutes")
else:
    print("Overloaded")

