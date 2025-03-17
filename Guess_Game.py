import random

c=random.randint(1,100)
print(c)

while True:
    try:
        n=int(input("Enter any integer : "))
        break
    except (ValueError,TypeError,SyntaxError): 
        print("Invalid Input")
