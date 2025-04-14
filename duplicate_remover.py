n=input("Enter any string : ")

word=n.strip().split()

print(" ".join(set(word)))