#print below pattern
# *
# **
# ***
# ****
# *****


# for i in range(1,6):                
#     print("*"*i)

#print below pattern
#     *
#    **
#   ***
#  ****    
# *****


# for i in range(1,6):                
#     print(" "*(5-i)+"*"*i)  

#print below pattern
# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):                
#     print("*"*i)

#print below pattern
#    *
#   ***
#  *****
# *******

for i in range(1,6,2):
    print(" "*(5-i-1),end="")
    for j in range(1,i+1):
        print("*",end="")
    print()