#Write a program that prints numbers which divisible by 5

a=[]

n=int(input("Enter the number of elements : "))

for i in range(1,n+1):  
    m=int(input(f"Enter any integer {i} : "))
    a.append(m) 
for i in a:
    if i%5==0:
        print(i)