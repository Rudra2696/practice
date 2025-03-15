# check if any character is repeated more than once in the string

n=input("Enter any string : ")
z=n.lower().strip()
m=len(z)
x=len(set(z))
if m==x:
    print("repeating characters are not present")
else:   
    print("repeating characters are present")