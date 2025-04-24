   
l=[]

while True:
    try:    
        a=int(input("Enter number of elements : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

for i in range(1,a+1):   
    while True:
        try:    
            i=int(input(f"Enter {i} number : "))
            l.append(i)
            break
        except (ValueError,TypeError,SyntaxError):
            print("Invalid Input")   

print(max(l))