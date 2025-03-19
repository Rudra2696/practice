def change_tracker():

    with open("task_tracker.txt","r") as f:
        print("Your tadk is given below")
        a=f.read()
        print(a)

    while True:
        try:
            n=int(input("Enter the number of task you want to change (integer only) : ")) 
            break
        except (ValueError,TypeError,SyntaxError,KeyError):
            print("Invalid Input")   

    c=input("Now enter new task : ")

    a.update({f"Task {n}" : c})   

def new_tracker():

    while True:
        try:
            n=int(input("Enter the number of task you want to add: "))
            break
        except (ValueError,TypeError,SyntaxError,KeyError):
            print("Invalid Input")    
    d={}
    for i in range(1,n+1):
        while True:
            z=input(f"Enter your task {i} : ")    
            m=z.capitalize().strip()
            if m=="" :
                print("Please enter your task ")
            else:
                break

    for i,j in zip(range(1,n+1),d):
        print(f"Your task {i} is {j}.")
            


    for i,j in zip(range(1,n+1),d):
        d.update({f"Task {i}":f"{j}"})
    print()  

    with open("task_tracker.txt","w+") as f:
        f.write(str(d))

def new_task():
    with open("task_tracker.txt","r") as f:
        print("Your task is given below")
        a=f.read()
        print(a)

    x=len(a)+1

    y=input("Now write the task you want to add (you can only add a single task in one time): ")  

    a.update({f"Task {x}" : y})  


print("Welcome to task tracker")    

while True:
        try:
            g=int(input("Enter what do you want \n If you want to make new task list (Enter 1) \n If  you want to change task list (Enter 2) \n If you want to add new task (Enter 3) : ")) 
            if (g==1 or g==2 or g==3):
                break
            else:
                print("Please enter 1/2/3 only")
        except (ValueError,TypeError,SyntaxError,KeyError):
            print("Invalid Input")  

if g==1 :     
    new_tracker()
elif g==2 :
    change_tracker()
elif g==3 :
    new_task()
else :
    print("Something Went Wrong")    