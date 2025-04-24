def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c    
   
while True:
    try:    
        a=int(input("Enter 1st number : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")
   
while True:
    try:    
        b=int(input("Enter 2nd number : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")   

while True:
    try:    
        c=int(input("Enter 3rd number : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

print(max(a,b,c))       