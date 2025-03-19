print("Welcome to task tracker")

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
        l.append(m)
        

    for i,j in zip(range(1,n+1),l):
        print(f"Your task {i} is {j}.")
            


    for i,j in zip(range(1,n+1),l):
        d[f"Task {i}"] = j
    print(d)  

    with open("task_tracker.txt","w+") as f:
        f.write(str(d))