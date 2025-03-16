#Problem 1

def merger(sent):
    cap=sent.capitalize()
    question=("How","Why","Where","When","What")
    if cap.startswith(question):
        return f"{cap}?"
    else:
        return f"{cap}."
    
l=[]
while True:
    n=input("Type something : ")
    if n=="/end":
        break
    else:
        l.append(merger(n))

print(" ".join(l))        
