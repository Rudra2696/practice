import pymysql

c=pymysql.connect(host="localhost",user="root",password="",database="Hello")

cur=c.cursor()

table="create table student(id int primary key auto_increment,name varchar(20),marks int)"

cur.execute(table)

