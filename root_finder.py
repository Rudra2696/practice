while True:
    try:
        n=int(input("Enter any integer : "))
        b=int(input("Enter which type of root you want : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

print(n**(1/b))