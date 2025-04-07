import random

a=random.randint(0,100)

with open ("score.txt","r") as f:
    b=f.read()

if b=="":   
    b=0    
b=int(b)
print(a)
if a>b :
    with open ("score.txt","w") as f:
        f.write(str(a))

