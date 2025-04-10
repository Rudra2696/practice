while True:
    try:
        a=int(input("Enter the number of term : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")

a1=0
a2=1
print(a1,end=" ")
print(a2,end=" ")
for i in range(2,a):
    a3=a1+a2
    print(a3,end=" ")
    a1=a2
    a2=a3