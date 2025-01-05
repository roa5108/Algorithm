grades={'A+':4.5,
'A0':4.0,
'B+':3.5,
'B0':3.0,
'C+':2.5,
'C0':2.0,
'D+':1.5,
'D0':1.0,
'F':0.0}
sum=0
credit_sum=0
for i in range(20):
    subject,credit,grade=input().split()
    credit=float(credit)
    if grade=='P':
        pass
    else:
        credit_sum+=credit
        sum+=credit*grades[grade]

gpa=sum/credit_sum
print(gpa)