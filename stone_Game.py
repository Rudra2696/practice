import random

c=random.choice([1,2,3])

print("Welcome to Stone Paper Sizer Game")


"""
Stone = 1
Paper = 2
Sizer =3
"""

while True:
    try:
        n=input("Enter your choice : ")
        break
    except (ValueError,TypeError,SyntaxError,KeyError):
        print("Invalid Input")

b=n.lower().strip()

d={"stone" : 1 ,
   "paper" : 2,
   "sizer" : 3}
d1={ 1: "Stone",
    2 : "Paper",
    3 : "Sizer"
}

user=d[b]
out=d1[c]

if (user==c):
    print("It's Draw!")
elif(user==1 and c==2):
    print("You Lost!")
elif(user==1 and c==3):
    print("You Won!")
elif(user==2 and c==1):
    print("You Won!")
elif(user==2 and c==3):
    print("You Lost!")
elif(user==3 and c==1):    
    print("You Lost!")
elif(user==3 and c==2):
    print("You Won!")
else:
    print("Something went wrong")

print(f"You chose {n} and computer chose {out}")    