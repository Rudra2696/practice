while True:
    try:
        a=int(input("Enter any integer : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

b=str(a)

c=b[::-1]

if b==c:
    print(f"{a} is palidrome")                                                                                         
elif b!=c:
    print(f"{a} is not palidrome")
else:
    print("Something went wrong")