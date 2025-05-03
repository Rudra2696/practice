n=input("Enter any long string with multiple words : ")
print(n.split()[::-1])
print(" ".join(n.split()[::-1]))