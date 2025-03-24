import random

while True:
    try:
        n=int(input("Enter the length of password : "))
        if n>0:
            break
        else:
            print("Please enter a positive number")
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

a1=random.randint(0,9)
a2=random.randint(97,122)
a3=random.randint(65,90)
a4=random.randint(33,47)
a5=random.randint(58,64)
a6=random.randint(91,96)
a7=random.randint(123,126)

b1=str(a1)
b2=chr(a2)
b3=chr(a3)
b4=chr(a4)
b5=chr(a5)
b6=chr(a6)
b7=chr(a7)

for i in range(n):
    c=random.choice([b1,b2,b3,b4,b5,b6,b7])
    print(c,end="")