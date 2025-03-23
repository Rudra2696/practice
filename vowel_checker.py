n=input("Enter any string : ")
n=n.lower().strip()
m=len(n)
c=0
for i in range(0,m):
    if n[i] in "aeiou":
        c=c+1
print(f"{n} has {c} vowels")        