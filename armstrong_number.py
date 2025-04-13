while True:
    try:
        a=int(input("Enter any integer : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

b=str(a)

c=len(b)

d=0

for i in range(0,c):
    d=d+int(b[i])**c

if d==a:    
    print(f"{a} is armstrong number")
else:
    print(f"{a} is not armstrong number")    