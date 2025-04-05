import pymysql

my = pymysql.connect(host="localhost", user="root", password="", database="Hello")

cur = my.cursor()

while True:
    try:
        marks=float(input("Enter the marks : "))
        break
    except (ValueError,TypeError,SyntaxError):  
        print("Invalid Input")

while True: 
    try:    
        id=int(input("Enter the ID : "))
        break    
    except (ValueError,TypeError,SyntaxError):      
        print("Invalid Input")

name=input("Enter the name : ")

data="update student set name=%s,marks=%s where id=%s"

try:

    cur.execute(data,(name,marks,id))

    my.commit()

    print("Data updated successfully")

except Exception:
    print("Error")