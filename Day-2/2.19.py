salary = int(input("enter salary:"))
credit = int(input("enter credit:"))
experience = int(input("enter experience:"))
if(salary>50000 and credit>750 and experience>3):
    print("lone appoved")
elif(salary>100000 and experience>3):
    print("pending ")
else:
    print("rejected")