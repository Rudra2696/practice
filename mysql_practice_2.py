import pymysql

my = pymysql.connect(host="localhost", user="root", password="", database="Hello")

cur = my.cursor()

try:
    t = "insert into student(name,marks) values(%s,%s)"

    ins = ("Virat", 78)

    cur.execute(t, ins)

    my.commit()

    print("Data inserted successfully")
    
except Exception:
    print("Error")
