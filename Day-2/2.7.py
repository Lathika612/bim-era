marks = int(input("enter marks:"))
attendence = int(input("enter attendence:"))
income = int(input("enter income:"))
if(marks>=85 and attendence>=90 and income<300000):
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")