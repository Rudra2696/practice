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

n=n.lower().strip()

d={"stone" : 1 ,
   "paper" : 2,
   "sizer" : 3}
d1={ 1: "Stone",
    2 : "Paper",
    3 : "Sizer"
}

user=d[n]
out=d1[c]

if (n==c):
    print("It's Draw!")
elif(n==1 and c==2):
    pass
elif(n==1 and c==3):
    pass
elif(n==2 and c==1):
    pass
elif(n==2 and c==3):
    pass
elif(n==3 and c==1):    
    pass
elif(n==3 and c==2):
    pass
else:
    print("Something went wrong")