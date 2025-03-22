def change_tracker():
    with open("task_tracker.txt", "r") as f:
        print("Your task is given below")
        a = f.read()

    try:
        tasks = eval(a)
    except (SyntaxError, NameError):
        tasks = {}
        print("Error: Unable to read tasks from file. Starting with an empty task list.")

    print(a)
    while True:
        try:
            o = int(input("Enter the number of task you want to change (integer only): "))
            if f"Task {o}" not in tasks:
                print("Task number does not exist. Please enter a valid task number.")
                continue
            break
        except ValueError:
            print("Invalid Input. Please enter an integer.")

    c = input("Now enter new task: ").strip()

    if c:
        tasks[f"Task {o}"] = c

        with open("task_tracker.txt", "w") as f:
            f.write(str(tasks))
        print(f"Your task is changed\nYour new task is given below\n{tasks}")
    else:
        print("No new task entered. Task not updated.")
def remove_tracker():

    with open("task_tracker.txt", "r") as f:
        a = f.read()

    try:
        tasks = eval(a)
    except (SyntaxError, NameError):
        tasks = {}
        print("Error: Unable to read tasks from file. Starting with an empty task list.")

    print(f" Your task was given below\n{a}")

    while True:
        try:
            o = int(input("Enter the number of task you want to remove (integer only): "))
            if f"Task {o}" not in tasks:
                print("Task number does not exist. Please enter a valid task number.")
                continue
            break
        except ValueError:
            print("Invalid Input. Please enter an integer.")   
    b=dict(tasks)
    del b[f"Task {o}"]
    print(f"Your task was updated\n. Your new task is given below\n{b}")

    with open("task_tracker.txt", "w") as f:
        f.write(str(b))

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
                d.update({f"Task {i}" : z})
                break
    print("Your task is given below")
    for i,j in zip(range(1,n+1),d):
        print(f"Your task {i} is {j}.")

    with open("task_tracker.txt","w+") as f:
        f.write(str(d))

def add_tracker():
    print("Reading the task_tracker.txt file")

    with open("task_tracker.txt","r") as f:
        print("Your task is given below")
        a=f.read()
        print(a)

    try:
        tasks = eval(a)
    except (SyntaxError, NameError):
        tasks = {}
        print("Error: Unable to read tasks from file. Starting with an empty task list.")
    b=dict(tasks)

    o=len(b.keys())+1    

    c = input("Now enter new task: ").strip()
    print(o)
    if c:
        tasks[f"Task {o}"] = c
        print(tasks)

        with open("task_tracker.txt", "w") as f:
            f.write(str(tasks))
        print(f"Your task is changed\nYour new task is given below\n{tasks}")
    else:
        print("No new task entered. Task not updated.")    


print("Welcome to task tracker")    

while True:
        try:
            g=int(input("Enter what do you want \n If you want to make new task list (Enter 1) \n "
            "If  you want to change task list (Enter 2) \n If you want to add new task (Enter 3) \n"
            "IF youn want tpo remove any task (Enter 4): ")) 
            if (g==1 or g==2 or g==3 or g==4):
                break
            else:
                print("Please enter 1/2/3 only")
        except (ValueError,TypeError,SyntaxError,KeyError):
            print("Invalid Input") 


if g==1 :     
    new_tracker()
elif (g==2 or g==3 or g==4):
    try:
        with open("task_tracker.txt","r") as f:
            if g==2:
                change_tracker()
            elif g==3:
                add_tracker()
            elif g==4:
                remove_tracker()    
    except FileNotFoundError:
        print("task_tracker.txt file not found")
else :
    print("Something Went Wrong")    