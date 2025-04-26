#Replace vowel by *

word=input("Enter any word : ")
vowel=["a","e","i","o","u","A","E","I","O","U"]
for i in word:
    if i in vowel:
        print("*",end="")
    else:
        print(i,end="")