while True:
    try:
        n=int(input("Enter any integer : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

c=0
for i in range(2,n):
    if n%i==0:
        c=c+1

if c==0:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")            