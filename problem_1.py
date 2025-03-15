#check the sring has atleast one consecutive three same characters

n=input("Enter any string : ") 
z=n.lower().strip()
m=len(z)
l=[]
for i in range(0,m):
    l.append(z[i])

for i in range(0,m): 
    if (l[i]==l[i+1]==l[i+2]):
        print("yes")
        break
else:
    print("no")    
