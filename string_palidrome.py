a=input("Enter any string : ")
c=a.lower().strip()
b=c[::-1]
if b==c:
    print(f"{a} is palidrome")
elif b!=c:
    print(f"{a} is not palidrome")
else:    
    print("Somethimg went wrong ...")