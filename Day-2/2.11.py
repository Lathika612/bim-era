age = int(input("enter age:"))
weight = int(input("enter weight:"))
height = float(input("enter height:"))
if(age>18 and weight>50 and height>5.5):
    print("Fitness Category A")
elif(age>18 and height>5.5):
    print("Fitness Category B")
else:
    print("Basic Category ")