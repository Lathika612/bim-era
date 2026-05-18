maths = int(input("enter maths marks:"))
science = int(input("enter science marks:"))
english = int(input("enter english marks:"))
if((maths+science+english)>=270):
    print("topperr")
elif((maths+science+english)>=180):
     print("aveage")
else:
    print("needs improvement")