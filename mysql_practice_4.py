import pymysql

my=pymysql.connect(host="localhost",user="root",password="",database="Hello")

cur=my.cursor()

print("{:<15}{:<15}{:<15}".format("ID","Name","Marks"))

try:
    sql="select * from student"

    cur.execute(sql)

    data=cur.fetchall()

    for i in data:
        print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

except Exception:
    print("Error")        