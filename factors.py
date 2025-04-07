while True:
    try:
        n=int(input("Enter any integer : "))
    except (ValueError,SyntaxError,TypeError)
    print("please enter integer only")
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)

print(f"The factors of {n} are {l}")        