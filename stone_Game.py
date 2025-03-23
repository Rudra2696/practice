import random

c=random.choice([1,2,3])

print("Welcome to Stone Paper Sizer Game")


"""
Stone = 1
Paper = 2
Sizer = 3
"""

while True:
    try:
        n=input("Enter your choice : ")
        b=n.lower().strip()
        if (b=="stone" or b=="paper" or b=="sizer"):
            break
        else:
            print("Please enter stone/paper/sizer only")
    except (ValueError,TypeError,SyntaxError,KeyError):
        print("Invalid Input")


if b=="stone":
    b=1
elif b=="paper":
    b=2
elif b=="sizer":
    b=3

d1={ 1: "Stone",
    2 : "Paper",
    3 : "Sizer"
}

out=d1[c]

if (b==c):
    print("It's Draw!")
elif(b==1 and c==2):
    print("You Lost!")
elif(b==1 and c==3):
    print("You Won!")
elif(b==2 and c==1):
    print("You Won!")
elif(b==2 and c==3):
    print("You Lost!")
elif(b==3 and c==1):    
    print("You Lost!")
elif(b==3 and c==2):
    print("You Won!")
else:
    print("Something went wrong")

print(f"You chose {n} and computer chose {out}")    