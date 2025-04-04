import pymysql

my=pymysql.connect(host="localhost",user="root",password="",database="Hello")

cur=my.cursor()

t="insert into student(name,marks) values(%s,%s)"

ins=("Rohit",78)

cur.execute(t,ins)

my.commit()