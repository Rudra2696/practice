import pymysql

my=pymysql.connect(host="localhost",user="root",password="",database="Hello")

cur=my.cursor()

print("{:<15}{:<15}".format("ID","Name","Marks"))

try:
    sql="Select * from student"

    cur.execute(sql)

    data=cur.fetchone()

    print("{:<15}{:<15}{:<15}".format(data[0],data[1],data[2]))

except Exception:   
    print("Error")