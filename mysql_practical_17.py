import pymysql

my=pymysql.connect(host="localhost",user="root",password="",database="Hello")

cur=my.cursor()
print("{:<15}{:<15}{:<15}".format("ID","Name","Surename"))

try:
    sql="select * from parents as p1, parents as p2 where p1.id=p2.cat"

    cur.execute(sql)

    data=cur.fetchall()

    for i in data:
        print(i)

except :
    print("Error") 