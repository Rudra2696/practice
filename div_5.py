#Write a program that prints numbers which divisible by 5

a=[]

while True:
    try:
        n=int(input("Enter the number of elements : "))
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")


for i in range(1,n+1):  
    m=int(input(f"Enter any integer {i} : "))
    a.append(m) 
for i in a:
    if i%5==0:
        print(i)