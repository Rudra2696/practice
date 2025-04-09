# check if any character is repeating in the string

n=input("Enter any string : ")
z=n.lower().strip()

x=len(set(z))
if len(z)==x:
    print("repeating characters are not present")
else:   
    print("repeating characters are present")