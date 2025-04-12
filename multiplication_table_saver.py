while True:
    try:    
        n=int(input("Enter the table you want : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

with open("table","a") as f:  
    for i in range(1,11):
        f.write(f"{n} * {i} = {n*i}\n")