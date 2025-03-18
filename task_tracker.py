print("Welcome to task tracker")


while True:
    try:
        n=int(input("Enter the number of task you want to add: "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")    

l=[]
for i in range(1,n+1):
    z=input(f"Enter task {i} : ")
    m=z.capitalize().strip()
    l.append(m)
    

print(f"Your task list is {l}")       

