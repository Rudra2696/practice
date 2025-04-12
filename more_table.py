while True:
    try:
        n=int(input("Enter starting table : "))
        break
    except(ValueError,SyntaxError,TypeError):
        print("Enter integer only")

while True:
    try:
        z=int(input("Enter ending table : "))
        break
    except(ValueError,SyntaxError,TypeError):
        print("Enter integer only")        


for i in range(n,z+1):
    with open (f"table {i}","a") as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}\n")       