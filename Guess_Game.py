import random

c=random.randint(1,100)
print(c)

while True:
    try:
        n=int(input("Enter any integer : "))
        break
    except (ValueError,TypeError,SyntaxError): 
        print("Invalid Input")

if n==c:
    print("You won")
else:
    print("You lost")