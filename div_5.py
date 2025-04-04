#Write a program that prints numbers which divisible by 5

a=[]
l=[]

while True:
    try:
        n=int(input("Enter the number of elements : "))
        if n>0:
            break
        else:
            print("Please enter a positive number")
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")


for i in range(1,n+1): 
    while True:
        try:
            m=float(input(f"Enter any integer {i} : "))
            a.append(m)
            break
        except (ValueError,TypeError,SyntaxError):
            print("Invalid Input") 
    

print("The numbers divisible by 5 are : ",end="")     
for i in a:
    if i%5==0:
        l.append(i)

for i in l:
    if i!=l[-1]:
        print(i,end=",")  
    else:
        print(i,end=".")                       