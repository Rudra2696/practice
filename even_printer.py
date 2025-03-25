while True:
    try:
        n=int(input("Enter any integer : "))
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

l=[]
for i in range(1,n+1):
    while True:
        try:
            m=int(input(f"Enter any integer {i} : "))
            l.append(m)
            break
        except (ValueError,TypeError,SyntaxError):  
            print("Invalid Input")

even=[]

for i in l:
    if i%2==0:
        even.append(i)
print(even)
