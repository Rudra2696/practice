while True:
    try:
        n=int(input("Enter any integer : "))
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

l=[]
for i in range(1,n+1):
    if i%2==0:
        l.append(i)
print(l)    
