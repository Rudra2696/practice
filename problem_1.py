#check the sring has atleast one consecutive three same characters

n=input("Enter any string : ") 
z=n.lower().strip()

l=[]
for i in range(0,len(z)):
    l.append(z[i])

for y in range(0,len(z)-2): 
    if (l[y]==l[y+1]==l[y+2]):
        print(f"{n} has consecutive three same characters")
        break
else:
    print(f"{n} has no consecutive three same characters")    
