import random

c=random.randint(1,100)
print(c)

while True:
    try:
        n=int(input("Enter any integer (1-100): "))
        if n==c:
            print("You won")
            break
        elif n>c:
            print("Too high")
        else:
            print("Too low")
    except (ValueError,TypeError,SyntaxError): 
        print("Invalid Input")

