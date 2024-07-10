#
li=[20,30,40,50,2,3,14]
price=0
patient_no=len(li)
if(patient_no<=20):
    for i in li:
        if i>0 and i<17:
            price+=200
        elif i>=17 and i<40:
            price+=400
        elif i>=40 and i<=120:
            price+=300

        print(price)
