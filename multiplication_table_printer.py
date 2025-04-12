while True:
    try:    
        n=int(input("Enter the table you want : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")