while True:
    try: 
       n=input("Enter any string : ")
       b=n.lower().strip()
       if b=="":
           print("Please enter any string")
       else:    
           break
    except (ValueError,TypeError,SyntaxError,KeyError):
        print("Something went wrong")


c=0
for i in range(0,len(b)):
    if b[i] in "aeiou":
        c=c+1
print(f"{n} has {c} vowels")        