import random

c=random.randint([1,2,3])

while True:
    try:
        n=int(input("Enter your choice : "))
        break
    except (ValueError,TypeError,SyntaxError,KeyError):
        print("Invalid Input")
        
            