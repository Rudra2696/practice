while True:
    try:
        n=float(input("Enter any  number : "))
        b=float(input("Enter which type of root you want : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

print(n**(1/b))