print("Welcome to task tracker")


while True:
    try:
        n=int(input("Enter the number of task you want to add: "))
        break
    except (ValueError,TypeError,SyntaxError,KeyError):
        print("Invalid Input")    

l=[]
for i in range(1,n+1):
    while True:
        z=input(f"Enter your task {i} : ")    
        m=z.capitalize().strip()
        if m=="" :
            print("Please enter your task ")
        else:
            break
    l.append(m)
    

for i,j in zip(range(1,n+1),l):
    print(f"Your task {i} is {j}.")
        

with open("task.txt","w") as f:
    for i,j in zip(range(1,n+1),l):
        f.write(f"Your task {i} is {j}.\n")